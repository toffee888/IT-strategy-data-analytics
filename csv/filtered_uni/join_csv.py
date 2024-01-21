import pandas as pd

csv_name = "07-unified-cleaned.csv"

df = pd.concat( 
    map(pd.read_csv, ['filtered_2023.csv', 'filtered_2022.csv','filtered_2021.csv','filtered_2020.csv','filtered_2019.csv','filtered_2018.csv', 'filtered_2017.csv',
                      'filtered_2016.csv', 'filtered_2015.csv', 'filtered_2014.csv', 'filtered_2013.csv', 'filtered_2012.csv', 'filtered_2011.csv']), ignore_index=True) 

df.to_csv(csv_name, index=False)