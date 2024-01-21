import pandas as pd

# Create two sample DataFrames
df1 = pd.read_csv('../csv/I_filtered.csv')
df2 = pd.read_csv('../csv/S_filtered.csv')


# Concatenate the DataFrames and drop duplicates based on the 'ID' column
result_df = pd.concat([df1, df2], ignore_index=True).drop_duplicates(subset='University_Name', keep='last')

# Display the resulting DataFrame

print(result_df)
result_df.to_csv("joined.csv",  index=False)
