import sys
sys.path.append('./data/raw/')
sys.path.append('./data/processed/')
import pandas as pd

df = pd.read_csv('./data/processed/varejo_processed.csv')

print(df.head())
