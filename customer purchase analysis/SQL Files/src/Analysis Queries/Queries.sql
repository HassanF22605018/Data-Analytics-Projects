-- 1. Top Products by Total Sales
SELECT 
    Category,
    SUM(CAST(REPLACE(Price, '$', '') AS FLOAT)) AS TotalSales,
    COUNT(*) AS NumberOfPurchases
FROM 
    PurchaseHistory
GROUP BY 
    Category
ORDER BY 
    TotalSales DESC;

-- 2. Top Customers by Purchase Frequency
SELECT 
    Unique_Customer_ID,
    COUNT(*) AS PurchaseCount
FROM 
    PurchaseHistory
GROUP BY 
    Unique_Customer_ID
ORDER BY 
    PurchaseCount DESC;

-- 3. Average Rating of Customers
SELECT 
    pr.Unique_Customer_ID,
    AVG(pr.Rating) AS AverageRating,
    COUNT(*) AS TotalReviews
FROM 
    ProductReviews pr
GROUP BY 
    pr.Unique_Customer_ID
ORDER BY 
    AverageRating DESC;


-- 4. Browsing History Analysis
SELECT 
    Unique_Customer_ID,
    COUNT(*) AS BrowsingCount,
    MAX([BrowsingDateTime]) AS LastBrowsed
FROM 
    BrowsingHistory
GROUP BY 
    Unique_Customer_ID
ORDER BY 
    BrowsingCount DESC;

-- 5. Customer Segmentation by Purchase Behavior
SELECT 
    Unique_Customer_ID,
    COUNT(*) AS PurchaseCount,
    SUM(Price) AS TotalSpent
FROM 
    PurchaseHistory
GROUP BY 
    Unique_Customer_ID
HAVING 
    COUNT(*) > 2 AND 
    SUM(Price) > 100
ORDER BY 
    TotalSpent DESC;

-- 6. Customer Segmentation by Demographics
SELECT 
    cd.Gender,
    AVG(CAST(REPLACE(ph.Price, '$', '') AS FLOAT)) AS AveragePurchase,
    COUNT(ph.Unique_Customer_ID) AS PurchaseCount
FROM 
    CustomerData cd
INNER JOIN 
    PurchaseHistory ph ON cd.Unique_Customer_ID = ph.Unique_Customer_ID
WHERE 
    cd.Gender IN ('Male', 'Female', 'Other')
GROUP BY 
    cd.Gender;

-- 7. Monthly Purchase Trends
SELECT 
    YEAR(TRY_CONVERT(date, Date, 103)) AS Year,
    MONTH(TRY_CONVERT(date, Date, 103)) AS Month,
    COUNT(*) AS Purchases,
    SUM(CAST(REPLACE(Price, '$', '') AS FLOAT)) AS TotalSales
FROM 
    PurchaseHistory
GROUP BY 
    YEAR(TRY_CONVERT(date, Date, 103)), MONTH(TRY_CONVERT(date, Date, 103))
ORDER BY 
    Year, Month;

-- 8. Time Spent Browsing vs. Purchase Value  
SELECT 
    bh.Unique_Customer_ID,
    AVG(DATEDIFF(MINUTE, 0, bh.TimeOnSite_Minutes)) AS AvgBrowsingTime,
    SUM(CAST(REPLACE(ph.Price, '$', '') AS FLOAT)) AS TotalPurchaseValue
FROM 
    BrowsingHistory bh
INNER JOIN 
    PurchaseHistory ph 
    ON bh.Unique_Customer_ID = ph.Unique_Customer_ID
GROUP BY 
    bh.Unique_Customer_ID
ORDER BY 
    AvgBrowsingTime DESC;

-- 9. Customer Retention Analysis
SELECT 
    Unique_Customer_ID,
    COUNT(DISTINCT FORMAT(Date, 'yyyy-MM')) AS ActiveMonths,
    COUNT(*) AS TotalPurchases
FROM 
    PurchaseHistory
GROUP BY 
    Unique_Customer_ID
HAVING 
    COUNT(DISTINCT FORMAT(Date, 'yyyy-MM')) > 1
ORDER BY 
    ActiveMonths DESC;

--10. High-Spending Loyal Customers
SELECT 
    ph.Unique_Customer_ID,
    COUNT(*) AS TotalPurchases,
    SUM(ph.Price) AS TotalSpent
FROM 
    PurchaseHistory ph
GROUP BY 
    ph.Unique_Customer_ID
HAVING 
    COUNT(*) >= 3 AND 
    SUM(ph.Price) > 500
ORDER BY 
    TotalSpent DESC;

--11. Top Categories by Browsing Interest
SELECT 
    Category,
    COUNT(*) AS TimesBrowsed
FROM 
    BrowsingHistory
GROUP BY 
    Category
ORDER BY 
    TimesBrowsed DESC;

--12. Correlation: Browsing Before Purchase
SELECT 
    ph.Unique_Customer_ID,
    COUNT(DISTINCT bh.Category) AS CategoriesBrowsed,
    COUNT(DISTINCT ph.Category) AS CategoriesPurchased
FROM 
    PurchaseHistory ph
LEFT JOIN 
    BrowsingHistory bh ON ph.Unique_Customer_ID = bh.Unique_Customer_ID
GROUP BY 
    ph.Unique_Customer_ID
ORDER BY 
    CategoriesBrowsed DESC;

--13. Customers Without Purchases
SELECT 
    cd.Unique_Customer_ID
FROM 
    CustomerData cd
LEFT JOIN 
    PurchaseHistory ph ON cd.Unique_Customer_ID = ph.Unique_Customer_ID
WHERE 
    ph.Unique_Customer_ID IS NULL;

--14. Gender-Based Review Sentiment
SELECT 
    cd.Gender,
    AVG(pr.Rating) AS AvgRating,
    COUNT(*) AS ReviewCount
FROM 
    CustomerData cd
JOIN 
    ProductReviews pr ON cd.Unique_Customer_ID = pr.Unique_Customer_ID
GROUP BY 
    cd.Gender;

