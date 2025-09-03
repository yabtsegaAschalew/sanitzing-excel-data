
def validate_phone_number(string_val):
    string_val = string_val.strip(" ")

    if string_val.startswith("+251"):
        print(string_val)  
    elif string_val.startswith("0"):
        if len(string_val) == 10:
            formatted = "+251" + string_val[1:]  
            print(formatted)
        else:
            print("Enter a valid number")
    else:
        print("Invalid number")

print("አ/ሰላም አ/ወሰዕ ሰኢድ")
