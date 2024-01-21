import pandas

years = ['2021']

for year in years:

    path = "../csv/overall_score_ml/" 

    current_csv_name = "uni_" + year + ".csv"

    final_name = path + current_csv_name

    df = pandas.read_csv(final_name,  sep=',')

    df = df.astype(str)

    for ind in df.index:
        df["number_students"][ind] = int(df["number_students"][ind].replace(",", ""))

                

    df.to_csv(final_name, index=False)
                