import pandas as pd
#from .validation import validate_birthdate, validate_gender, validate_phone_number, validate_profession, validate_relation


xls = pd.ExcelFile('excel_file/Lideta SC 2nd round export_active_members_07-05-17.xlsx')


print(xls.sheet_names)


print("Number of sheets:", len(xls.sheet_names))


headers = pd.read_excel(xls, sheet_name=xls.sheet_names[0], nrows=0).columns.tolist()
print("Headers:", headers)

df = pd.read_excel(xls, sheet_name=xls.sheet_names[0])  
current_row = df.loc[0].tolist() 
print("First row:", current_row)
