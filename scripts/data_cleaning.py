import pandas
import math

#machine learning doesnt accept hyphen

years= ['2023', '2022', '2021', '2020', '2019', '2018', '2017', '2016', '2015', '2014', '2013', '2012', '2011']

for year in years:

    path = "../csv/raw_csv/" 
    current_csv_name = "uni_" + year + ".csv"

    final_name = path + current_csv_name

    df = pandas.read_csv(final_name,  sep=',')


    for ind in df.index:
        df['rank'][ind] = ind + 1

        try:
            current_value = float(df['overall_score'][ind])
            if math.isnan(current_value):
                df['overall_score'][ind] = "-"
        
        except:
            df['overall_score'][ind] = "-"

        
    new_name = "../csv/overall_score_ml/" + current_csv_name

    df.to_csv(new_name, index=False)