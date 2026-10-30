import pandas as pd

df = pd.read_csv("/Users/apple/Downloads/clean_cafe_sales.csv", parse_dates=["transaction_date"])

# Summary tables
item_sales = df[df["item"] != "Unknown"].groupby("item")["total_spent"].sum().sort_values(ascending=False).reset_index()
pay = df[df["payment_method"] != "Unknown"]["payment_method"].value_counts().reset_index()
pay.columns = ["payment_method", "count"]
monthly = df.groupby(df["transaction_date"].dt.to_period("M").astype(str))["total_spent"].sum().reset_index()
loc = df[df["location"] != "Unknown"].groupby("location")["total_spent"].sum().reset_index()

# Excel file, alag alag sheets mein
with pd.ExcelWriter("/Users/apple/Downloads/cafe_sales.xlsx", engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="Clean Data", index=False)
    item_sales.to_excel(writer, sheet_name="Item Sales", index=False)
    pay.to_excel(writer, sheet_name="Payment Method", index=False)
    monthly.to_excel(writer, sheet_name="Monthly Sales", index=False)
    loc.to_excel(writer, sheet_name="Location Sales", index=False)

print("Excel file ban gayi: Downloads/cafe_sales.xlsx")
