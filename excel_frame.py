import pandas as pd

def excel_reader(path): #load data
        df = pd.concat(pd.read_excel(
                path,
                sheet_name=None,
                header=3,
                na_values=""))

        #clean data
        df = df.iloc[:, :5]   
        df = df[df['Lp.'] > 0]
       
        df = df.reset_index(level=[1])
        df = df.drop(['level_1'], axis = 1)
        df.rename(columns = {'Nazwa międzynarodowa preparatu - postać - dawka': 'Opis', 'J.m.': 'Jednostka'}, inplace = True)

        df['INN'] = df['Opis'].str.split(' ').str[0]
        df.index.name = 'Oznaczenie zadania'
        df = df[['Lp.','Opis','INN','Ilość','Jednostka']]

        #file_name = "excel_frame.xls"
        #df.to_excel(file_name)
        return(df)

path = r'C:\file_path.xls'
print(excel_reader(path))
