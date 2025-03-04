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

