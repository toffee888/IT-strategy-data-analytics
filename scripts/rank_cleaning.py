import pandas

years= ['2019', '2016', '2015', '2014', '2013', '2012']

for year in years:

    path = "../csv/overall_score_ml/" 

    current_csv_name = "uni_" + year + ".csv"

    final_name = path + current_csv_name

    df = pandas.read_csv(final_name,  sep=',')


    for ind in df.index:
        temp = int(ind + 1)

        df['rank'][ind] = temp

    df.to_csv(final_name, index=False)