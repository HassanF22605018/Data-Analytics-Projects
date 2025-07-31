# Customer Purchase Analysis SQL Project

This project is designed to set up a database named **Customer_Purchase_Analysis** for analyzing customer purchase data. It includes SQL scripts for creating the database, defining the necessary tables, and importing data from CSV files.

## Project Structure

```
customer-purchase-analysis-sql
├── src
│   ├── create-database.sql
│   ├── tables
│   │   └── create-tables.sql
│   ├── data-import
│   │   └── import-purchase-history.sql
├── README.md
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