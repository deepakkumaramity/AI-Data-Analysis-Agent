
import pandas as pd

def clean_data(file_path):
    df = pd.read_csv(file_path)
    
    # basic info
    print("Dataset Info")
    print(df.info())
    
    # missing values
    print("\nMissing Values")
    print(df.isnull().sum())
    
    # duplicates
    df = df.drop_duplicates()
    
    return df
