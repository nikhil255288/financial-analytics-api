-- insert_data.sql

INSERT INTO financial_data (
    date, department, region, revenue, cost, expense, profit_center,
    profit, gross_margin_percent, net_profit_margin_percent
)
VALUES
('2023-07-01', 'Sales', 'South', 100000, 70000, 5000, 'South Zone', 25000, 25.00, 20.00),
('2023-07-02', 'Marketing', 'North', 120000, 80000, 10000, 'North Zone', 30000, 27.50, 22.50);
