import pandas as pd
stocks = pd.read_csv('EQUITY.csv').rename(columns={"NAME OF COMPANY" :"NAME" }).head(100)

def stock():
    return stocks