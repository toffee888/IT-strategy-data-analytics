import pandas

years= ['2023', '2022', '2021', '2020', '2019', '2018', '2017', '2016', '2015', '2014', '2013', '2012', '2011']

for year in years:

    current_csv_name = "uni_" + year + ".csv"

    df = pandas.read_csv(current_csv_name,  sep=',')


    for ind in df.index:
        df["student_staff_ratio"][ind] = round(df["student_staff_ratio"][ind]/100,2)

        
    df.to_csv(current_csv_name, index=False)