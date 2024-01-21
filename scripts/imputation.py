import pandas
import numpy as np


years= ['2023', '2022', '2021', '2020', '2019', '2018', '2017', '2016', '2015', '2014', '2013', '2012', '2011']
columns = ['teaching_score', 'research_score']

for year in years:

    path = "../csv/overall_score_ml/" 

    current_csv_name = "uni_" + year + ".csv"

    final_name = path + current_csv_name

    df = pandas.read_csv(final_name,  sep=',')

    df = df.astype(str)
    
        
    for column in columns:


        filtered_df = df.loc[(df[column].str.contains('-|—') == False)]

        filtered_df.dropna().empty
        
        y = filtered_df[column].astype(float)

        X = filtered_df['rank'].astype(float)

        xlog_data = np.log(X) 

        # plt.scatter(X, y)
        # plt.show()

        curve = np.polyfit(xlog_data, y, 1)


        for ind in df.index:
            if "-" in df[column][ind] or "—" in df[column][ind] or not df[column][ind].isnumeric():
                current_rank = float(df['rank'][ind])
                predicted_score = curve[0] * np.log(current_rank) + curve[1]
                df[column][ind] = round(float(predicted_score),2)


        saved_path = "../csv/imputation/" 

        saved_name = saved_path + current_csv_name

        df.to_csv(saved_name, index=False)