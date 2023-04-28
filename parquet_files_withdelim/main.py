import pandas as pd

# Read the CSV 
df = pd.read_csv('file_with_double_delim_quotes_in_header.csv')

#  to Parquet file
df.to_parquet('file_with_double_delim_quotes_in_header.parquet')