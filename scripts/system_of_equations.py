import numpy as np
import pandas

years= ['2023','2022', '2021', '2020', '2019', '2018', '2017', '2016', '2015', '2014', '2013', '2012', '2011']

numeric_column_names = ["overall_score", "teaching_score","research_score","citations_score","industry_income_score",
                        "international_outlook_score", "number_students", "student_staff_ratio","intl_students"]

print("teaching","research","citations","industry_income","international_outlook")

for year in years:

    path = "../csv/overall_score_ml/" 

    current_csv_name = "uni_" + year + ".csv"

    final_name = path + current_csv_name

    df = pandas.read_csv(final_name,  sep=',')
    
    row_number = [0, 20, 120, 142, 190]
    numeric_array = []
    score_array = []

    for row in row_number:

        numeric_df = df[["teaching_score","research_score","citations_score","industry_income_score",
                        "international_outlook_score"]]
        
        score_df = df["overall_score"]

        temp_numeric_array = numeric_df.iloc[row].to_numpy()
        temp_score_value = score_df.values[row]

        numeric_array.append(temp_numeric_array)
        score_array.append(temp_score_value)
        
    numeric_array = np.array(numeric_array).astype(float)
    score_array = np.array(score_array).astype(float)

    multipliers_array = np.linalg.solve(numeric_array, score_array)

    print(year, multipliers_array)

    # for names in numeric_column_names:

    #     overall_score = 0
    #     teaching_score	= 41.6
    #     research_score	= 22.5
    #     citations_score	= 62.7
    #     industry_income_score = 99.1
    #     international_outlook_score = 58.7

    #     teaching_score = 0.28964048 * teaching_score
    #     research_score = 0.30793846 * research_score
    #     citations_score  = 0.303409 * citations_score 
    #     industry_income_score = 0.02313499 * industry_income_score
    #     international_outlook_score = 0.07489746 * international_outlook_score

    #     template = overall_score - teaching_score - research_score - citations_score - industry_income_score - international_outlook_score


    #     print(overall_score)

    
        