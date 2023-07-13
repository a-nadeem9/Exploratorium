# SQL Data Cleaning
This repository contains SQL queries for cleaning and standardizing data in the NashvilleHousing table of the Portfolio database. The main steps involved in the data cleaning process are as follows:

1. Standardize Date Format: Convert the SaleDate column to the Date data type and create a new column for the converted dates.
2. Populate Property Address: Update missing PropertyAddress values by joining the table with itself and selecting non-null values.
3. Split Address into Individual Columns: Split the PropertyAddress column into separate columns for Address and City.
4. Split Owner Address into Individual Columns: Split the OwnerAddress column into separate columns for Address, City, and State.
5. Change 'Y' and 'N' to 'Yes' and 'No' in the "Sold as Vacant" field.
6. Remove duplicate rows based on specific columns.
7. Delete unused columns from the table.
These SQL queries aim to clean and standardize the data, ensuring consistency and improving data quality in the NashvilleHousing table.
