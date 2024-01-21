import pdfplumber
import pandas as pd


def extract_university_names(pdf_path):
    data = {'University Name': [], 'Strat_Year': []}

    
    with pdfplumber.open(pdf_path) as pdf:
        for page_number in range(len(pdf.pages)):
            page = pdf.pages[page_number]
            tables_in_page = page.extract_tables()
            
            for table in tables_in_page:
                # Assuming the university names are in the first column
    
                for row in table:
                    if row:
                        university_name = row[1].strip()  # Assuming the name is in the first column
                        strategy_year = row[3].strip()

                        data['University Name'].append(university_name)
                        data['Strat_Year'].append(strategy_year)
    
    df = pd.DataFrame(data)
    return df

# Replace 'your_pdf_file.pdf' with the actual path to your PDF file
pdf_path = '../ocr/S.pdf'
university_df = extract_university_names(pdf_path)

university_df.drop([0], inplace=True)

university_df["University Name"] = university_df["University Name"].str.replace(r'\n\[\d+\]|\[\d+\]', '', regex=True)

print(university_df)

university_df.to_csv("S_filtered.csv")