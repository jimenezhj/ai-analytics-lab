USE cre_portfolio_db;
GO

--CREATE OR ALTER VIEW dbo.vw_activeleases AS

--SELECT	l.leaseid,
--		p.propertyid,
--		p.propertyname,
--		p.city,
--		p.assetclass,
--		t.tenantid,
--		t.tenantname,
--		t.industry,
--		t.anchortenant,
--		l.leasestartdate,
--		l.leaseenddate,
--		DATEDIFF(MONTH, GETDATE(), l.leaseenddate) AS MonthsRemaining,
--		l.basemonthlyrent,
--		l.basemonthlyrent*12 AS AnnualRent,
--		l.squarefeetleased,
--		CASE WHEN l.squarefeetleased > 0 THEN CAST((l.basemonthlyrent*12.0)/l.squarefeetleased AS decimal(10,2)) ELSE NULL END AS RentPerSqft,
--		l.renewaloptions,
--		l.status
--FROM	dbo.lease l
--INNER JOIN dbo.property p ON l.PropertyID = p.propertyid
--INNER JOIN dbo.tenant t ON l.TenantID = t.tenantid
--WHERE	l.Status = 'active';
--GO

--CREATE OR ALTER VIEW dbo.vw_LeaseExpirationSchedule AS
--SELECT
--    LeaseID, PropertyName, TenantName, Industry, AnchorTenant,
--    LeaseEndDate,
--    YEAR(LeaseEndDate) AS ExpirationYear,
--    DATEPART(QUARTER, LeaseEndDate) AS ExpirationQuarter,
--    'Q' + CAST(DATEPART(QUARTER, LeaseEndDate) AS VARCHAR) + ' ' + CAST(YEAR(LeaseEndDate) AS VARCHAR) AS ExpirationLabel,
--    MonthsRemaining,
--    CASE
--        WHEN MonthsRemaining <= 6 THEN 'Critical (<=6mo)'
--        WHEN MonthsRemaining <= 12 THEN 'Urgent (6-12mo)'
--        WHEN MonthsRemaining <= 24 THEN 'Upcoming (1-2yr)'
--        WHEN MonthsRemaining <= 60 THEN 'Future (2-5yr)'
--        ELSE 'Long-term (>5yr)'
--    END AS UrgencyTier,
--    BaseMonthlyRent, AnnualRent, SquareFeetLeased, RenewalOptions
--FROM dbo.vw_ActiveLeases;
--GO

SELECT *
FROM dbo.vw_leaseexpirationschedule

--CREATE OR ALTER VIEW dbo.vw_PropertyPerformance AS
--SELECT
--    p.PropertyID, p.PropertyName, p.City, p.AssetClass, p.TotalSquareFeet,
--    COUNT(DISTINCT CASE WHEN l.Status = 'Active' THEN l.LeaseID END) AS ActiveLeaseCount,
--    ISNULL(SUM(CASE WHEN l.Status = 'Active' THEN l.SquareFeetLeased ELSE 0 END), 0) AS LeasedSqFt,
--    p.TotalSquareFeet - ISNULL(SUM(CASE WHEN l.Status = 'Active' THEN l.SquareFeetLeased ELSE 0 END), 0) AS VacantSqFt,
--    CAST(ISNULL(SUM(CASE WHEN l.Status = 'Active' THEN l.SquareFeetLeased ELSE 0 END), 0) * 100.0
--        / NULLIF(p.TotalSquareFeet, 0) AS DECIMAL(5,2)) AS OccupancyPct,
--    ISNULL(SUM(CASE WHEN l.Status = 'Active' THEN l.BaseMonthlyRent * 12 ELSE 0 END), 0) AS AnnualRent,
--    p.AcquisitionCost, p.AcquisitionDate
--FROM dbo.Property p
--LEFT JOIN dbo.Lease l ON p.PropertyID = l.PropertyID
--GROUP BY p.PropertyID, p.PropertyName, p.City, p.AssetClass, p.TotalSquareFeet, p.AcquisitionCost, p.AcquisitionDate;
--GO

--CREATE OR ALTER VIEW dbo.vw_TenantConcentration AS
--WITH tenant_exposure AS (
--    SELECT
--        t.TenantID, t.TenantName, t.Industry, t.AnchorTenant,
--        COUNT(DISTINCT l.PropertyID) AS PropertyCount,
--        SUM(l.BaseMonthlyRent * 12) AS TotalAnnualRent
--    FROM dbo.Lease l
--    INNER JOIN dbo.Tenant t ON l.TenantID = t.TenantID
--    WHERE l.Status = 'Active'
--    GROUP BY t.TenantID, t.TenantName, t.Industry, t.AnchorTenant
--)
--SELECT
--    TenantName, Industry, AnchorTenant, PropertyCount, TotalAnnualRent,
--    CAST(TotalAnnualRent * 100.0 / SUM(TotalAnnualRent) OVER () AS DECIMAL(5,2)) AS PctOfPortfolioRent,
--    RANK() OVER (ORDER BY TotalAnnualRent DESC) AS RentRank
--FROM tenant_exposure;
--GO

-- Verify
SELECT 'vw_ActiveLeases' AS ViewName, COUNT(*) AS Numberofrows FROM dbo.vw_ActiveLeases
UNION ALL SELECT 'vw_LeaseExpirationSchedule', COUNT(*) FROM dbo.vw_LeaseExpirationSchedule
UNION ALL SELECT 'vw_PropertyPerformance', COUNT(*) FROM dbo.vw_PropertyPerformance
UNION ALL SELECT 'vw_TenantConcentration', COUNT(*) FROM dbo.vw_TenantConcentration;

-- Sample consumer queries
SELECT * FROM dbo.vw_TenantConcentration WHERE RentRank <= 10;

SELECT * FROM dbo.vw_LeaseExpirationSchedule
WHERE UrgencyTier IN ('Critical (<=6mo)', 'Urgent (6-12mo)')
ORDER BY MonthsRemaining;

SELECT * FROM dbo.vw_PropertyPerformance WHERE OccupancyPct < 90 ORDER BY OccupancyPct;
	