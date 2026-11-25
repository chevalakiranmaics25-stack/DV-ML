# 1. Getting Started with Power BI

**Aim:** Import a CSV dataset and explore table, bar chart and line chart visuals in Power BI Desktop.

**Dataset:** `retail_sample.csv` (sample retail orders).

**Steps**
1. Open Power BI Desktop → Home → Get data → Text/CSV.
2. Select `retail_sample.csv` and choose Load.
3. Add a Table visual; include OrderDate, Region, Category and Sales.
4. Add a Clustered column chart; Axis = Category, Values = Sum of Sales.
5. Add a Line chart; X-axis = OrderDate, Y-axis = Sum of Sales.
6. Save as `01_Getting_Started.pbix`.

**Expected result:** A table, category-wise sales bar/column chart and sales trend line chart.
