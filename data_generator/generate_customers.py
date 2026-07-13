import datetime
import os
from faker import Faker
from src.config import VALID_PROVINCES


fake = Faker()
start_date = datetime.date(2020, 1, 1)
end_date = datetime.date(2026, 6, 30)
os.makedirs("data/raw", exist_ok=True)

with open("data/raw/customers.csv", "w") as f:
    f.write("customer_id,full_name,province,join_date\n")
    for i in range(100001, 101001):
        f.write(
            f"{i},{fake.name()},{fake.random_element(elements=VALID_PROVINCES)},{str(fake.date_between(start_date, end_date))}\n"
        )
