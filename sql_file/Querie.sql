##Total Transactions vs Total Revenue
SELECT 
    COUNT(DISTINCT TransactionID) AS Total_Transactions, 
    SUM(TransactionAmount) AS Total_Revenue 
FROM `test-74ac1.sales_data.sales_table`;