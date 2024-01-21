import pandas as pd

import numpy as np


current_csv_name = "raw.csv"

unnormalised = ['rank','overall_score','teaching_score','research_score','citations_score','industry_income_score','international_outlook_score']
normalised = ['rank_n','overall_score_n','teaching_score_n','research_score_n','citations_score_n','industry_income_score_n','international_outlook_score_n']

neg_array = []
pos_array = []


df = pd.read_csv(current_csv_name,  sep=',')


for name in unnormalised:

    pivot_tabledf = pd.pivot_table(df, columns='strategy_year_n', index="name", values=name)

    t_pivot = pivot_tabledf.reset_index()


    t_pivot["m+1"] = t_pivot[1]
    t_pivot["m-1"] = t_pivot[1]

    for col in t_pivot.columns:

        if(type(col) == str):
            continue

        if (int(col) <= 0):
            neg_array.append(col)

        if (int(col) >= 0):
            pos_array.append(col)

    for ind in t_pivot.index:
    
        selected_row = t_pivot.iloc[ind]

        negative_array = selected_row[neg_array].values
        negative_array = negative_array.astype(float)

        clean_negative_array = negative_array[np.logical_not(np.isnan(negative_array))]

        x_array = clean_negative_array.copy()


        for index, value in enumerate(x_array):
            x_array[index] = index

        try:
            slope, intercept = np.polyfit(x_array, clean_negative_array, 1)
            t_pivot["m-1"][ind] = round(slope,2)

        except:
            continue

        positive_array = selected_row[pos_array].values
        positive_array = positive_array.astype(float)

        clean_positive_array = positive_array[np.logical_not(np.isnan(positive_array))]

        x_array = clean_positive_array.copy()

        for index, value in enumerate(x_array):
            x_array[index] = index
        

        try:
            slope, intercept = round(np.polyfit(x_array, clean_positive_array, 1),2)
            t_pivot["m+1"][ind] = round(slope,2)

        except:
            continue
  

    neg_array=[]
    pos_array=[]


    # print(t_pivot)
    t_pivot = t_pivot.drop(["m+1","m-1"], axis=1)

    array_append = t_pivot.mean(numeric_only=True).to_numpy()
    array_append= np.round(array_append, decimals=2)
    array_append = array_append.astype(object)

    np.insert(array_append, 0, "Average")

    print(t_pivot.shape)
    print(array_append)

    new_row_df = pd.DataFrame([array_append], columns=pivot_tabledf.columns)

    t_pivot = pd.concat([t_pivot, new_row_df], ignore_index=True)

    # print(t_pivot.shape)
    


    # new_csv_name = name + "_pivot.csv"

    t_pivot.to_csv("test.csv", index=False)