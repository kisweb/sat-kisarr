import pandas as pd
from glob import glob

# data = pd.read_excel("./excels\Releve_notes_Mathématiques_6émeB.xlsx", skiprows=6)

# pd.DataFrame(data)

path = "./excels/*.xlsx"
files = glob(path)

for f in files:
    print(f)
    d = pd.read_excel(f, skiprows=6)
    print(d)
    data = pd.concat(pd.read_excel(f, skiprows=6) for f in files)
    pd.DataFrame(data, columns=["Nom", "Prénom", "Note"])

# # get the absolute paths of all Excel files 
# all_excel_files = glob("./excels/*.xlsx")

# # read all Excel files at once
# data = pd.concat(pd.read_excel(excel_file, skiprows=6) for excel_file in all_excel_files)
# print(data)