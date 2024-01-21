import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

unnormalised = ['rank','overall_score','teaching_score','research_score','citations_score','industry_income_score','international_outlook_score']
normalised = ['rank_n','overall_score_n','teaching_score_n','research_score_n','citations_score_n','industry_income_score_n','international_outlook_score_n']

for name in normalised:
    current_csv_name = "csv/" + name + "_pivot.csv"
    current_df = pd.read_csv(current_csv_name,  sep=',')
    current_df = current_df.drop(["m+1", "m-1", "-12", "-11","-10","-9","-8","-7","7","8"] ,axis=1)

    print(current_df)

    mean = current_df.mean(numeric_only=True)
    print(mean)

    mean.index = mean.index.astype(int)

    fig, graph = plt.subplots()

    graph.plot(mean, label="mean")

    neg_index = []
    neg_values = []

    pos_index = []
    pos_values = []

    for ind in mean.index:

        if (int(ind) <=0):
            neg_index.append(int(ind))
            neg_values.append(float(mean[ind]))

        if (int(ind) >=0):
            pos_index.append(int(ind))
            pos_values.append(float(mean[ind]))

    
    
    coefficient_neg = np.polyfit(neg_index, neg_values, 1)

    trendline_neg = np.poly1d(coefficient_neg)
    m_trendline_neg = round(trendline_neg[1],2)

    trendline_neg_y = trendline_neg(neg_index)

    graph.plot(neg_index, trendline_neg_y, color="orange", linestyle="--", label="m before IT strat, {}".format(m_trendline_neg))


    coefficient_pos = np.polyfit(pos_index, pos_values, 1)
    trendline_pos = np.poly1d(coefficient_pos)
    m_trendline_pos = round(trendline_pos[1],2)


    graph.plot(pos_index, trendline_pos(pos_index), color="green", linestyle="--", label="m after IT strat, {}".format(m_trendline_pos))

    graph.spines['left'].set_position(('data', 0))


    graph.set_xlabel('Year Difference')
    graph.set_ylabel('Values')
    graph.set_title(name)
    graph.grid()
    graph.legend() 

    

    saved_as = 'graphs/' + name + ".png"

    plt.savefig(saved_as)
    plt.show()

    

    
    