# Cafe Sales: Data Cleaning & Visualization

## Overview
This project covers data cleaning and visualization of a dirty cafe sales dataset (10,000 rows) using Python and Pandas.

## What I Did
1. **Data Collection:** Downloaded the raw dirty cafe sales dataset from Kaggle
2. **Data Cleaning:** Cleaned the data using Python (Pandas) in VS Code
   - Standardized column names
   - Converted `ERROR` and `UNKNOWN` values to missing values
   - Fixed data types (numbers and dates)
   - Recalculated missing `total_spent` from quantity x price
   - Removed rows with missing critical values and duplicates
3. **Data Visualization:** Created 4 graphs with Matplotlib to show the sales insights

## Key Insights
- **Salad** is the top-selling item (15,780 total sales), followed by Smoothie (12,324) and Sandwich (12,304)
- **Cookie** has the lowest sales (2,937), and Tea is second lowest (4,454)
- Payment methods are almost evenly split: Digital Wallet 33.6%, Credit Card 33.3%, Cash 33.1%
- **In-store** sales (24,625) are slightly higher than **Takeaway** (24,228)

## Visualization
![Cafe Sales Analysis](clean%20data%20cafe%20sale.png)

## Tools
Python, Pandas, Matplotlib, VS Code

## Files
- `data clean.py`: cleaning and visualization code
- `clean data cafe sale.png`: output graphs

## Portfolio
🌐 [faiez-ahmed.netlify.app](https://faiez-ahmed.netlify.app/)
