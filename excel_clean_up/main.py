import pandas as pd

file = pd.read_excel('excel_file/Lideta SC 2nd round export_active_members_07-05-17.xlsx', sheet_name="W1")
current_row = file.loc[100]
print(current_row)