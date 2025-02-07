##Total Transactions vs Total Revenue
SELECT 
    COUNT(DISTINCT TransactionID) AS Total_Transactions, 
    SUM(TransactionAmount) AS Total_Revenue 
FROM `test-74ac1.sales_data.sales_table`;

##Average Order Value
SELECT 
    SUM(TransactionAmount) / COUNT(DISTINCT TransactionID) AS Average_Order_Value 
FROM  `test-74ac1.sales_data.sales_table`;

##Top 5 Products by Revenue
SELECT 
    ProductName, 
    SUM(TransactionAmount) AS Total_Sales 
FROM `test-74ac1.sales_data.sales_table`
GROUP BY ProductName 
ORDER BY Total_Sales DESC 
LIMIT 6;

##Sale Distribution by Store Type
SELECT 
    StoreType, 
    SUM(TransactionAmount) AS Total_Sales, 
    COUNT(TransactionID) AS Total_Transactions 
FROM `test-74ac1.sales_data.sales_table` 
GROUP BY StoreType;

DRILL DOWN METRICS
##Region wise revenue breakdown
SELECT 
    Region, 
    SUM(TransactionAmount) AS Total_Sales, 
    COUNT(TransactionID) AS Transactions 
FROM `test-74ac1.sales_data.sales_table`
GROUP BY Region 
ORDER BY Total_Sales DESC;


###Impact of Discounts
SELECT 
    CASE 
        WHEN DiscountPercent > 0 THEN 'Discounted Sales'
        ELSE 'Full Price Sales'
    END AS Sale_Type,
    COUNT(TransactionID) AS Transactions,
    SUM(TransactionAmount) AS Total_Sales 
FROM `test-74ac1.sales_data.sales_table` 
GROUP BY Sale_Type;

###Preferred Payment Mode

SELECT 
    PaymentMethod, 
    COUNT(TransactionID) AS Transactions, 
    SUM(TransactionAmount) AS Total_Sales 
FROM `test-74ac1.sales_data.sales_table` 
GROUP BY PaymentMethod 
ORDER BY Total_Sales DESC;

###Returnby Product
SELECT 
    ProductName, 
    COUNT(TransactionID) AS Total_Returns 
FROM `test-74ac1.sales_data.sales_table` 
WHERE Returned = 'Yes'
GROUP BY ProductName 
ORDER BY Total_Returns DESC 
LIMIT 5;