import random
import itertools
import pandas as pd
from faker import Faker


data = pd.read_csv("accounts.csv")
fake= Faker()
transaction_id = itertools.count(start=300001)


new_data = {"transaction_id": [], "account_id": [], 
        "transaction_type": [], "amount": []}
transaction_types = ["Deposit", "Withdrawal", "Card Purchase"]


for row in data.itertuples():
    random_number_of_transactions = random.randint(2, 5)
    
    for _ in range(random_number_of_transactions):
        new_data["transaction_id"].append(next(transaction_id)),
        new_data["account_id"].append(row.account_id)
        new_data["transaction_type"].append(random.choice(transaction_types)),
        new_data["amount"].append(random.randint(50, 5000))

df = pd.DataFrame(new_data)
print(df)
