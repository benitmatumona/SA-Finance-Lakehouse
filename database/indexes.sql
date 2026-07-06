CREATE INDEX province_index
ON customers(province);

CREATE INDEX customer_id_index 
ON accounts(customer_id);

CREATE INDEX account_id_index
ON transactions(account_id);

CREATE INDEX transaction_date_index
ON transactions(transaction_date);

CREATE INDEX is_fraud_index
ON transactions(is_fraud);