-- Top 5 products by revenue
SELECT Description, SUM(TotalPrice) AS Revenue
FROM data
GROUP BY Description
ORDER BY Revenue DESC
LIMIT 5;

-- Monthly sales trend
SELECT Month, SUM(TotalPrice) AS TotalSales
FROM data
GROUP BY Month
ORDER BY Month;

-- Top countries by sales
SELECT Country, SUM(TotalPrice) AS Revenue
FROM data
GROUP BY Country
ORDER BY Revenue DESC;

-- Average order value
SELECT AVG(TotalPrice) FROM data;