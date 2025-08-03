open the project folder

run requirements.txt file:

            pip install -r requirements.txt


Initialize the Database (Only once):

            python scripts/db_operations.py


Fetch Stock Data:

            python scripts/fetch_data.py


if you want to see database tables download duckdbcli and run below commands:

            .open "Give Your Project Path/sensex_project/data/sensex_data.duckdb" 


            SHOW TABLES;

            SELECT * FROM sensex_company_list;

            SELECT * FROM ending_price;

it will show all the details


Then integrate it into Power BI dashboard
Configure Python in Power BI:

            Open Power BI Desktop → File → Options and settings → Options → Python scripting

            Set the path to your Python installation directory (the folder containing python.exe).

Update Python script in Power BI data source:

Use a script like this to load data from DuckDB:

            import duckdb
            conn = duckdb.connect("C:/Users/vamsi/OneDrive/Desktop/New folder/sensex_project/data/sensex_data.duckdb", read_only=True)
            df = conn.execute("SELECT * FROM sensex_company_list").fetchdf()
            conn.close()
            df

Refresh the report to load the latest data from DuckDB.



<img width="2194" height="1129" alt="image" src="https://github.com/user-attachments/assets/bab4eb03-79f2-4b09-a104-2c8ca13e820d" />

