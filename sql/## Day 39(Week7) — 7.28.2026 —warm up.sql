--#    Run these against AdventureWorks2022.
--# 1. Total revenue (SUM of TotalDue) per SalesTerritory name, highest first.
--#    (JOIN Sales.SalesOrderHeader to Sales.SalesTerritory, GROUP BY + ORDER BY)
SELECT	st.name,
		SUM(so.totaldue) AS TotalRevenue
FROM	sales.SalesOrderHeader so
INNER JOIN	sales.SalesTerritory st ON so.TerritoryID = st.TerritoryID
GROUP BY	st.Name
ORDER BY	TotalRevenue



--# 2. Each product plus its subcategory's average ListPrice on the same row.
--#    (Production.Product — window function; which one?)
WITH averagecategory AS

(
	SELECT	ps.ProductSubcategoryID AS SubcategoryID,
			ps.name AS Subcategory,
			AVG(p.listprice) AS AverageByCat
	FROM	Production.Product p
	INNER JOIN Production.ProductSubcategory ps ON p.ProductSubcategoryID = ps.ProductSubcategoryID
	WHERE	p.ListPrice > 0
	GROUP BY	ps.ProductSubcategoryID, ps.Name
)

SELECT	p.name AS Product,
		ac.Subcategory AS Subcategory,
		p.listprice AS listprice,
		ac.AverageByCat AS categoryaverage
FROM	Production.Product p
INNER JOIN	averagecategory ac ON p.ProductSubcategoryID = ac.SubcategoryID


--# 3. Products that have never been ordered.
--#    (Production.Product vs Sales.SalesOrderDetail — anti-join; which trap do you avoid?)

SELECT	p.name
FROM	Production.Product p
WHERE NOT EXISTS (	SELECT	1
					FROM	sales.SalesOrderDetail sd
					WHERE	p.ProductID = sd.ProductID);


SELECT	p.name
FROM	Production.Product p
LEFT JOIN	sales.SalesOrderDetail sd ON p.ProductID = sd.ProductID
WHERE sd.ProductID IS NULL

