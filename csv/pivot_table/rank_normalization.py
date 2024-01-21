import pandas

# years= ['2019', '2016', '2015', '2014', '2013', '2012']

# for year in years:

#     path = "../csv/overall_score_ml/" 

current_csv_name = "07-unified-cleaned.csv"

df = pandas.read_csv(current_csv_name,  sep=',')

df['rank_n'] = df['rank']


for ind in df.index:

    df['rank_n'][ind] = round((df['rank'][ind] - 1)/(2334 - 1),2)

df.to_csv(current_csv_name, index=False)