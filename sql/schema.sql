DROP TABLE IF EXISTS financial_data;

CREATE TABLE financial_data (
    Date DATE,
    Department VARCHAR(50),
    Region VARCHAR(50),
    Revenue INTEGER,
    Cost INTEGER,
    Expense INTEGER,
    Profit_Center VARCHAR(100),
    Profit INTEGER,
    Gross_Margin_Percent NUMERIC,
    Net_Profit_Margin_Percent NUMERIC
);
