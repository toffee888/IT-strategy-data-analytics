import pandas

years = ['2020']

column_names = ["overall_score", "teaching_score","research_score","citations_score","industry_income_score",
                "international_outlook_score", "number_students", "student_staff_ratio","intl_students"]

for year in years:

    current_csv_name = "uni_" + year + ".csv"
    df = pandas.read_csv(current_csv_name,  sep=',')

    numeric_df_storage = [df["rank"], df["overall_score"], df["teaching_score"], df["research_score"], df["citations_score"], df["industry_income_score"],
                          df["international_outlook_score"], df["number_students"], df["student_staff_ratio"], df["intl_students"]]

    numeric_df = pandas.concat(numeric_df_storage, axis=1, join='outer')
    
    numeric_df.astype(float)

    for names in column_names:
        
        normalized = numeric_df[names] / numeric_df[names].abs().max()

        new_column_name = names + "_n"

        temp_df = pandas.concat([df["rank"], normalized.round(2)], axis=1, join='outer')

        temp_df = temp_df.rename(columns = {names: new_column_name})

        df = df.merge(temp_df, how = 'left')
        


    new_csv_name = "normalized_" + year + ".csv"
    df.to_csv(new_csv_name, index=False)