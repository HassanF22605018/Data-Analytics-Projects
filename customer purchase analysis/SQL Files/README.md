# Customer Purchase Analysis SQL Project

This project is designed to set up a database named **Customer_Purchase_Analysis** for analyzing customer purchase data. It includes SQL scripts for creating the database, defining the necessary tables, and importing data from CSV files.

## Project Structure

```
customer purchase analysis/
├── Customer Purchase  Analysis.xlxs
├── Clean Files/
│ ├── Cleaned_Browsing_History.xlsx
│ ├── Cleaned_Product_Reviews.xlsx
│ └── Cleaned_Purchase_History.xlsx
├── Customer Purchase  Analysis.twb
├── Cleaned_Browsing_History.csv
├── Cleaned_Product_Reviews.csv
├── Cleaned_Purchase_History.csv
├── CustomerData.csv
├── SQL Files/
|  ├── src
│     ├── Analysis Queries
│     |    |── Queries.sql
│     ├── data-import
│     |    └── import-data.sql
│     └── tables
│     |     └──create-tables.sql
├     |── create-database.sql

```

## Setup Instructions

1. **Create the Database**
   - Open the `create-database.sql` file located in the `src` directory.
   - Execute the SQL commands to create the **Customer_Purchase_Analysis** database.

2. **Create Tables**
   - Navigate to the `src/tables/create-tables.sql` file.
   - Run the SQL statements to create the necessary tables for storing customer and purchase data.

3. **Import Data**
   - Open the `src/data-import/import-purchase-history.sql` file.
   - Ensure that the CSV file path in the script is correct.
   - Execute the BULK INSERT command to import data into the **PurchaseHistory** table.

## Notes
- Ensure that you have the necessary permissions to create databases and tables in your SQL environment.
- Modify the file paths in the import script as needed to match your local setup.