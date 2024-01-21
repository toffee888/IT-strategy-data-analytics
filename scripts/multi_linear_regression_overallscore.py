import pandas

from sklearn import linear_model

year= ["2013", "2014", "2015"]

for x in year:

    current_csv_name = "uni_" + x + ".csv"

    df = pandas.read_csv(current_csv_name,  sep=',')

    filtered_df = df.loc[(df['industry_income_score'] != "-") & (df['overall_score'] != "-")]

    X = filtered_df[['teaching_score','research_score','citations_score','industry_income_score','international_outlook_score']]
    y = filtered_df[['overall_score']]


    X = X.astype({"industry_income_score":float})

    regr = linear_model.LinearRegression()
    regr.fit(X, y)

    for ind in df.index:

        if (df['overall_score'][ind] == "-"):

            industry_income_score = df['industry_income_score'][ind]

            if(industry_income_score != "-"):

                industry_income_score = float(df['industry_income_score'][ind])
                teaching_score = df['teaching_score'][ind]
                research_score = df['research_score'][ind]
                citations_score = df['citations_score'][ind]
                international_outlook_score = df['international_outlook_score'][ind]

                df['overall_score'][ind] = str(regr.predict([[teaching_score, research_score, citations_score, industry_income_score, international_outlook_score]]))[2:-2]
                print(df.iloc[[ind]])

    df.to_csv("multiregression_result_2013.csv", index=False)
