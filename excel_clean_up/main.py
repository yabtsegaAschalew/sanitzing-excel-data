import pandas as pd
import time
from validation import *

def validate_all(row_data):
    
    print(validate_family(row_data["local CBHID"]))
    # print(validate_birthdate(row_data["birth date"]))
    # print(validate_gender(row_data["Gender"]))
    # print(validate_phone_number(row_data["Phone number"]))
    # print(validate_profession(row_data["Profession"]))
    # print(validate_relation(row_data["Relationship"]))
    

def read_excel(file):
    xls = pd.ExcelFile(file)
    sheet_list = xls.sheet_names
    
    for sheet in sheet_list:
        
        df = pd.read_excel(xls, sheet_name=sheet)

        if df.empty:
            print("No rows to process.")
            continue
        

        for index, row in df.iterrows():
            #time.sleep(3)
            if row.isna().all() or all(str(val).strip() == "" for val in row):
                print("Error has occured")
                break
            row_data = row.to_dict() 
            validate_all(row_data)
            print(f"{row_data}")
