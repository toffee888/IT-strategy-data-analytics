import pandas

years = ['2019']

#column_names = ["teaching_score","research_score","citations_score","industry_income_score",
               # "international_outlook_score", "number_students", "student_staff_ratio","intl_students"]

column_names = ["intl_students"]

for year in years:

    current_csv_name = "uni_" + year + ".csv"

    df = pandas.read_csv(current_csv_name,  sep=',')

    average_series = df.mean(axis = 0, skipna = True, numeric_only=True) 

    average_df = average_series.to_frame().reset_index()
    average_df = average_df.rename(columns = {0:'average'})

    print(year)

    for ind in average_df.index:
        
        if "rank" in average_df["index"][ind] or "year" in average_df["index"][ind] or "overall_score" in average_df["index"][ind]:
            pass

        else:
            print(average_df["index"][ind], average_df["average"][ind])
            
            for ind_2 in df.index:
                if pandas.isna(df[average_df["index"][ind]][ind_2]):
                    df[average_df["index"][ind]][ind_2] = round(average_df["average"][ind],2)
 

    df.to_csv(current_csv_name, index=False)