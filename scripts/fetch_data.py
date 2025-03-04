import yfinance as yf
from datetime import datetime
from db_operations import insert_into_db
# List of top 30 Sensex stocks
top_30_sensex_stocks = [
    "RELIANCE.NS", "TCS.NS", "HDFCBANK.NS", "INFY.NS", "HINDUNILVR.NS", "ICICIBANK.NS",
    "BHARTIARTL.NS", "KOTAKBANK.NS", "ITC.NS", "LT.NS", "MARUTI.NS", "M&M.NS",
    "AXISBANK.NS", "ASIANPAINT.NS", "BAJAJ-AUTO.NS", "SUNPHARMA.NS", "HCLTECH.NS",
    "TITAN.NS", "WIPRO.NS", "NTPC.NS", "ULTRACEMCO.NS", "JSWSTEEL.NS", "POWERGRID.NS",
    "BAJFINANCE.NS", "BAJAJFINSV.NS", "GRASIM.NS", "DIVISLAB.NS", "SBIN.NS",
    "TECHM.NS", "INDUSINDBK.NS"
]
# Get current date
current_date = datetime.today().replace(hour=15, minute=30,second=0,microsecond=0)
 # This ensures it's a proper date object
# Lists to store data
company_list = []
ending_price_list = []
# Fetch stock data for each stock
for stock in top_30_sensex_stocks:
    stock_info = yf.Ticker(stock)
    data = stock_info.history(period="1d")  # Get daily data
    if not data.empty:
        close_price = data["Close"].iloc[0]  # Closing price of the day
        is_active = True
    else:
        print(f"⚠️ No data found for {stock}. Skipping...")
        continue  # Skip to the next stock
    # Append to respective lists
    company_list.append((stock, current_date))
    ending_price_list.append((stock, close_price, is_active))
# Insert data into DuckDB
if company_list and ending_price_list:
    insert_into_db(company_list, ending_price_list)
else:
    print("❌ No valid stock data available to insert.")  #".open C:/Users/vamsi/OneDrive/Desktop/sensex_project/data/sensex_data.duckdb"

#import duckdb
''' Open the DuckDB database in read-only mode
conn = duckdb.connect("C:/Users/vamsi/OneDrive/Desktop/sensex_project/data/sensex_data.duckdb", read_only=True)
# Fetch data from both tables
df_sensex = conn.execute("SELECT * FROM sensex_company_list").fetchdf()
df_ending_price = conn.execute("SELECT * FROM ending_price").fetchdf()
# Close the connection
conn.close()
# Print DataFrames (Optional, for debugging)
# print(df_sensex.head())  
print(df_ending_price.head()) '''