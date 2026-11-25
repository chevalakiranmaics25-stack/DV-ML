# 2. Data Cleaning and Transformation

**Aim:** Clean a deliberately untidy dataset with Power Query.

**Dataset:** `messy_customers.csv` (contains blanks, inconsistent casing, whitespace and mixed date/number formats).

**Steps**
1. Get Data → Text/CSV → select the CSV → Transform Data.
2. Rename columns to CustomerID, CustomerName, City, JoinDate and Sales.
3. Use Transform → Format → Trim and Clean on text columns; standardize City/CustomerName casing.
4. Replace blank Sales with null, then remove or replace nulls according to the rule you document.
5. Set JoinDate to Date and Sales to Decimal Number.
6. Add a custom column such as SalesBand using Conditional Column.
7. Close & Apply; save as `02_Data_Cleaning.pbix`.

**Expected result:** A cleaned table with consistent text, valid data types and a documented missing-value treatment.
