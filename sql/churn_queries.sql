use churn_analysis;
show tables;
select * from telco_churn_clean;
SELECT COUNT(*) AS total_customers
FROM telco_churn_clean;
SELECT Churn,
       COUNT(*) AS total
FROM telco_churn_clean
GROUP BY Churn;

SELECT Contract,
       COUNT(*) AS total_customers,
       SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS churned_customers
FROM telco_churn_clean
GROUP BY Contract;

SELECT PaymentMethod,
       COUNT(*) AS total_customers,
       SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS churned_customers
FROM telco_churn_clean
GROUP BY PaymentMethod;

SELECT Churn,
       AVG(MonthlyCharges) AS avg_monthly_charges
FROM telco_churn_clean
GROUP BY Churn;

SELECT Churn,
       AVG(tenure) AS avg_tenure
FROM telco_churn_clean
GROUP BY Churn;
