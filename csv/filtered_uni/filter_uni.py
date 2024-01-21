import pandas as pd

csv_file_path = 'joined_2.csv'  # Replace with the actual path to your CSV file
conditions = pd.read_csv(csv_file_path)


years= ['2023', '2022', '2021', '2020', '2019', '2018', '2017', '2016', '2015', '2014', '2013', '2012', '2011']

for year in years:

    path = "../normalized/" 
    current_csv_name = "normalized_" + year + ".csv"

    final_name = path + current_csv_name

    df = pd.read_csv(final_name,  sep=',')

    filtered_df = df[df['name'].isin(conditions['name'])]

    new_conditions = conditions[conditions['name'].isin(filtered_df['name'])]
    new_conditions = new_conditions.drop(columns=['rank'])

    final_df = pd.merge(filtered_df, new_conditions, on="name", how='right')

    final_df['strategy_year_n'] = final_df['year'] - final_df['strategy_year']

    

    new_name = 'filtered_' + year + '.csv'
    final_df.to_csv(new_name, index=False)

