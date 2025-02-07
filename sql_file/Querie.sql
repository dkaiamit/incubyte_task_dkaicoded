##Total Transactions vs Total Revenue
SELECT 
    COUNT(DISTINCT TransactionID) AS Total_Transactions, 
    SUM(TransactionAmount) AS Total_Revenue 
FROM `test-74ac1.sales_data.sales_table`;

##Average Order Value
SELECT 
    SUM(TransactionAmount) / COUNT(DISTINCT TransactionID) AS Average_Order_Value 
FROM  `test-74ac1.sales_data.sales_table`;
