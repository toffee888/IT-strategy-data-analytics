import pandas as pd

import numpy as np

from pylatex import Document, Section, Subsection, Tabular, Math, TikZ, Axis, \
    Plot, Figure, Matrix, Alignat
from pylatex.utils import italic
import os


if __name__ == '__main__':

    normalised = ['rank_n','overall_score_n','teaching_score_n','research_score_n','citations_score_n','industry_income_score_n','international_outlook_score_n']

    for name in normalised:
        # current_csv_name = name + "_pivot.csv"

        # df = pd.read_csv(current_csv_name,  sep=',')

        doc = Document()

        with doc.create(Subsection('Table of something')):
            with doc.create(Tabular('rc|cl')) as table:
                table.add_hline()
                table.add_row((1, 2, 5, 6))

        doc.generate_tex("test")