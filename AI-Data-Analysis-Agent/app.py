
import pandas as pd
from src.data_cleaning import clean_data
from src.ai_insights import generate_insights

file_path = "data/sales_data.csv"

df = clean_data(file_path)

print("\nDataset Preview")
print(df.head())

print("\nAI Insights")
for insight in generate_insights(df):
    print("-", insight)
