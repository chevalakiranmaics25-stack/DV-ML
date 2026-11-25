# 5. Geo-Visualization with Maps

**Aim:** Visualize sales geographically by city and state.

**Dataset:** `regional_sales.csv`.

**Steps**
1. Import the CSV.
2. In Data view, set Country to Data Category = Country/Region, State to State or Province, and City to City.
3. Add a Map or Azure Maps visual (depending on what is enabled in your Power BI version).
4. Place City in Location, Sales in Size, and Region in Legend; add State and Country to Tooltips as useful.
5. If locations resolve incorrectly, include State and Country fields or use latitude/longitude if provided by your source.
6. Save as `05_Geo_Visualization.pbix`.

**Expected result:** Map bubbles sized by sales, with location details in tooltips. Map availability can depend on tenant/admin settings.
