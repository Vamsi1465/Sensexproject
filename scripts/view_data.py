import sys
import os
# Add project root to sys.path so Python finds `models.py`
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from models import SensexCompany, EndingPrice, SessionLocal
from sqlalchemy.orm import Session
# Create a session
session = SessionLocal()
# Fetch all rows from sensex_company_list
companies = session.query(SensexCompany).all()
print("Sensex Company List:")
for company in companies:
  print(company.stock, company.date_time)  # Use `date_time` instead
# Fetch all rows from ending_price
prices = session.query(EndingPrice).all()
print("\nEnding Prices:")
for price in prices:
    print(price.stock, price.close_price, price.active)
session.close() 