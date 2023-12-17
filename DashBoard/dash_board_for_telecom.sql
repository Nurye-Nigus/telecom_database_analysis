-- telecom.sql

-- Customers Overview
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    address VARCHAR(100)
    -- Add other customer-related fields
);

-- User Engagement
CREATE TABLE user_engagement (
    engagement_id SERIAL PRIMARY KEY,
    customer_id INT,
    engagement_date DATE,
    duration_minutes INT,
    data_usage_mb DECIMAL(10, 2),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
    -- Add other user engagement-related fields
);

-- Experience and Satisfaction Analysis
CREATE TABLE satisfaction_analysis (
    analysis_id SERIAL PRIMARY KEY,
    customer_id INT,
    satisfaction_score INT,
    feedback TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
    -- Add other satisfaction analysis-related fields
);
INSERT INTO customers (name, age, address)
VALUES
    ('Nurye Nigus', 26, '123 Main St'),
    ('Jane Smith', 25, '456 Oak St');
INSERT INTO user_engagement (customer_id, engagement_date, duration_minutes, data_usage_mb)
VALUES
    (1, '2023-01-01', 60, 200),
    (2, '2023-01-02', 45, 150);
INSERT INTO satisfaction_analysis (customer_id, satisfaction_score, feedback)
VALUES
    (1, 5, 'Excellent service!'),
    (2, 4, 'Good experience overall');


