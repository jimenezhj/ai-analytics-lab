--USE cre_portfolio_db;
--GO

---- Procedure 1: Property snapshot at a point in time
--CREATE OR ALTER PROCEDURE dbo.usp_GetPropertySnapshot
--    @PropertyID INT,
--    @AsOfDate DATE = NULL
--AS
--BEGIN
--    SET NOCOUNT ON;
--    IF @AsOfDate IS NULL SET @AsOfDate = GETDATE();

--    -- Property facts
--    SELECT PropertyID, PropertyName, City, AssetClass, TotalSquareFeet,
--        AcquisitionDate, AcquisitionCost, @AsOfDate AS SnapshotDate
--    FROM dbo.Property WHERE PropertyID = @PropertyID;

--    -- Active leases on snapshot date
--    SELECT
--        l.LeaseID, t.TenantName, t.Industry,
--        l.LeaseStartDate, l.LeaseEndDate, l.BaseMonthlyRent, l.SquareFeetLeased,
--        DATEDIFF(MONTH, @AsOfDate, l.LeaseEndDate) AS MonthsRemaining
--    FROM dbo.Lease l
--    INNER JOIN dbo.Tenant t ON l.TenantID = t.TenantID
--    WHERE l.PropertyID = @PropertyID
--      AND l.LeaseStartDate <= @AsOfDate
--      AND l.LeaseEndDate >= @AsOfDate
--    ORDER BY l.BaseMonthlyRent DESC;

--    -- 12-month collection trend
--    SELECT
--        SnapshotMonth,
--        SUM(BilledAmount) AS Billed,
--        SUM(CollectedAmount) AS Collected,
--        CAST(SUM(CollectedAmount) * 100.0 / NULLIF(SUM(BilledAmount), 0) AS DECIMAL(5,2)) AS CollectionPct
--    FROM dbo.RentRoll rr
--    INNER JOIN dbo.Lease l ON rr.LeaseID = l.LeaseID
--    WHERE l.PropertyID = @PropertyID
--      AND rr.SnapshotMonth >= DATEADD(MONTH, -12, @AsOfDate)
--      AND rr.SnapshotMonth <= @AsOfDate
--    GROUP BY SnapshotMonth
--    ORDER BY SnapshotMonth;
--END;
--GO

--EXEC dbo.usp_getpropertysnapshot @propertyid = 1

--CREATE OR ALTER PROCEDURE dbo.usp_GetExpirationsByDateRange
--    @StartDate DATE, @EndDate DATE,
--    @AssetClass NVARCHAR(50) = NULL,
--    @MinAnnualRent MONEY = 0
--AS
--BEGIN
--    SET NOCOUNT ON;
--    SELECT
--        l.LeaseID, p.PropertyName, p.City, p.AssetClass,
--        t.TenantName, t.Industry, t.AnchorTenant,
--        l.LeaseEndDate,
--        l.BaseMonthlyRent * 12 AS AnnualRent,
--        l.SquareFeetLeased, l.RenewalOptions,
--        CASE WHEN l.RenewalOptions > 0 THEN 'Has renewal options'
--             ELSE 'No renewal — must renegotiate' END AS RenewalStatus
--    FROM dbo.Lease l
--    INNER JOIN dbo.Property p ON l.PropertyID = p.PropertyID
--    INNER JOIN dbo.Tenant t ON l.TenantID = t.TenantID
--    WHERE l.Status = 'Active'
--      AND l.LeaseEndDate BETWEEN @StartDate AND @EndDate
--      AND (@AssetClass IS NULL OR p.AssetClass = @AssetClass)
--      AND l.BaseMonthlyRent * 12 >= @MinAnnualRent
--    ORDER BY l.LeaseEndDate, AnnualRent DESC;
--END;
--GO

--EXEC  dbo.usp_GetExpirationsByDateRange @startdate = '2026-01-01', @enddate = '2026-12-31'

-- Procedure 3: Full tenant history
--CREATE OR ALTER PROCEDURE dbo.usp_GetTenantHistory
--    @TenantID INT
--AS
--BEGIN
--    SET NOCOUNT ON;

--    SELECT TenantID, TenantName, Industry, AnchorTenant, ContactEmail, CreatedDate
--    FROM dbo.Tenant WHERE TenantID = @TenantID;

--    SELECT l.LeaseID, p.PropertyName, p.City,
--        l.LeaseStartDate, l.LeaseEndDate, l.BaseMonthlyRent,
--        l.SquareFeetLeased, l.Status, l.RenewalOptions
--    FROM dbo.Lease l
--    INNER JOIN dbo.Property p ON l.PropertyID = p.PropertyID
--    WHERE l.TenantID = @TenantID
--    ORDER BY l.LeaseStartDate DESC;

--    SELECT a.AmendmentID, l.LeaseID, p.PropertyName,
--        a.AmendmentDate, a.AmendmentType, a.NewMonthlyRent, a.NewEndDate, a.Notes
--    FROM dbo.LeaseAmendment a
--    INNER JOIN dbo.Lease l ON a.LeaseID = l.LeaseID
--    INNER JOIN dbo.Property p ON l.PropertyID = p.PropertyID
--    WHERE l.TenantID = @TenantID
--    ORDER BY a.AmendmentDate DESC;

--    SELECT
--        SUM(rr.BilledAmount) AS LifetimeBilled,
--        SUM(rr.CollectedAmount) AS LifetimeCollected,
--        CAST(SUM(rr.CollectedAmount) * 100.0 / NULLIF(SUM(rr.BilledAmount), 0) AS DECIMAL(5,2)) AS LifetimeCollectionPct,
--        COUNT(*) AS RentRollMonths
--    FROM dbo.RentRoll rr
--    INNER JOIN dbo.Lease l ON rr.LeaseID = l.LeaseID
--    WHERE l.TenantID = @TenantID;
--END;
--GO


--exec dbo.usp_GetTenantHistory @tenantid = 1
