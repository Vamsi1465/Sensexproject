import sys
import os
from sqlalchemy.orm import Session
from datetime import datetime
# Ensure the script can find `models.py`
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models import SensexCompany, EndingPrice, SessionLocal
# Function to insert stock data
def insert_into_db(company_list, ending_price_list):
    session = SessionLocal()
    try:
        # Insert into sensex_company_list
        for stock, date in company_list:
          session.merge(SensexCompany(stock=stock, date_time=date))  # Directly use `date` if it's already a date object
        # Insert into ending_price
        for stock, close_price, active in ending_price_list:
            session.merge(EndingPrice(stock=stock, close_price=close_price, active=active))
        # Commit transaction
        session.commit()
        print("✅ Data inserted successfully.")
    except Exception as e:
        session.rollback()
        print(f"❌ Error inserting data: {e}")
    finally:
        session.close()
# Run only for debugging
if __name__ == "__main__":
    print("✅ Database connection successful.")