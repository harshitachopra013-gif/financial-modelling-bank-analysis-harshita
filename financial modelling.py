#harshita chopra 12513837
import pandas as pd
import numpy as np

f = r"C:\Users\ANURAG PATHAK\Downloads\CBI HARSHITA csv NEW.csv"

df = pd.read_csv(f)

print(df.head())

year = pd.to_datetime(df.iloc[:,0], format="%d-%m-%Y")

equity_capital = pd.to_numeric(df.iloc[:,1], errors="coerce")
reserves = pd.to_numeric(df.iloc[:,2], errors="coerce")
deposits = pd.to_numeric(df.iloc[:,3], errors="coerce")
borrowing = pd.to_numeric(df.iloc[:,4], errors="coerce")
other_liabilities = pd.to_numeric(df.iloc[:,5], errors="coerce")
total_liabilities = pd.to_numeric(df.iloc[:,6], errors="coerce")
fixed_assets = pd.to_numeric(df.iloc[:,7], errors="coerce")
cwip = pd.to_numeric(df.iloc[:,8], errors="coerce")
investments = pd.to_numeric(df.iloc[:,9], errors="coerce")
other_assets = pd.to_numeric(df.iloc[:,10], errors="coerce")
total_assets = pd.to_numeric(df.iloc[:,11], errors="coerce")

growth_rate = total_assets.pct_change() * 100

profit = total_assets - total_liabilities

roi = ((total_assets.iloc[-1] - total_assets.iloc[0]) / total_assets.iloc[0]) * 100

summary = pd.DataFrame({
    "Year": year,
    "Equity Capital": equity_capital,
    "Reserves": reserves,
    "Deposits": deposits,
    "Borrowing": borrowing,
    "Other Liabilities": other_liabilities,
    "Total Liabilities": total_liabilities,
    "Fixed Assets": fixed_assets,
    "CWIP": cwip,
    "Investments": investments,
    "Other Assets": other_assets,
    "Total Assets": total_assets,
    "Profit": profit,
    "Growth Rate %": growth_rate
})

output_path = r"C:\Users\ANURAG PATHAK\Downloads\CBI_FINANCIAL_MODEL.xlsx"

summary.to_excel(output_path, index=False)

print("Financial Modelling Completed")
print("ROI:", roi)
print("Output Saved:", output_path)