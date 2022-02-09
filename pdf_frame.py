
import re
import tabula
import pandas as pd
import numpy as np



path = pd.concat(tabula.read_pdf(r'C:\file_path.pdf',
    pages='all'))


def find_capital_word(str1):
        result = re.findall(r'\b[A-Z]\w+', str1)
        return result


def pdf_reader(path): ## load data
    df = pd.DataFrame(path)
    
    ## cleaning data
    df = df.iloc[3:,:3]
    df.columns = 'Nazwa towaru','j.m','Ilość'
    df = df.rename(columns = {'Nazwa towaru':'Opis'})
    df = df[df['Opis'].str.contains("Nazwa towaru")==False]

    df['Nazwa programu'] = df['Opis'].apply(lambda cw : find_capital_word(cw))
    df = df.explode('Nazwa programu')
    
    df['lp'] = 0
    df.loc[df['Nazwa programu'] == 'Program','lp'] = 1
    df['lp'] = df['lp'].replace(0,np.NaN)
    df = df[['Nazwa programu','lp','Opis','j.m','Ilość']]

    df = df.reset_index()
    df = df.drop(columns=['index'])
    
    #df.to_excel('pdf.frame.xls', header=True, index=True)
    return(df)

print(pdf_reader(path))