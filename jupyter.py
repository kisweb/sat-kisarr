import pandas as pd
import openpyxl

df = pd.read_excel(
    'https://github.com/kisweb/stat-kisarr/blob/main/appel_salle.xlsx?raw=True',
    skiprows=8
    
)

print(df)