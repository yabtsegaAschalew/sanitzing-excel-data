from datetime import datetime
from ethiopian_date import EthiopianDateConverter
import re

converter = EthiopianDateConverter()

def validate_phone_number(string_val=None):
    if not isinstance(string_val, str) or string_val is None:
        return ""

    if string_val.startswith("+251"):
        return string_val
    elif string_val.startswith("0"):
        if len(string_val) == 10:
            formatted = "+251" + string_val[1:]  
            return formatted
        else:
            return ""
    else:
        return ""

def validate_birthdate(birthdate=None):
    
    if birthdate:
        if "-" in birthdate:
            # splitting birth date and reversing the list

            birthdate = birthdate.split("-")[::-1]
            gc_date = converter.to_gregorian(int(birthdate[0]), int(birthdate[1]), int(birthdate[2]))
            return str(gc_date)
        if "/" in birthdate:
            # splitting birth date and reversing the list
            birthdate = birthdate.split("/")[::-1]
            gc_date = converter.to_gregorian(int(birthdate[0]), int(birthdate[1]), int(birthdate[2]))
            return str(gc_date)
    else:
        current_date = datetime.now()
        past_date = current_date.replace(year=current_date.year - 18)
        return f"{past_date.year}-{past_date.month}-{past_date.day}"


def validate_profession(profession=None):
    profession_dict = {
        "house wife": 1,
        "employee": 2,
        "self employed": 3,
        "other": 4
    }
    
    if not isinstance(profession, str) or profession is None:
        return profession_dict["other"]
    
    profession = " ".join(profession.split()).lower()
    
    for key in profession_dict:
        if key in profession:
            return profession_dict[key]
    
    return profession_dict["other"]

def validate_relation(relation=None):
    relation_dict = {
        "self": "head",
        "brother": 1,
        "sister": 1,
        "parent": 2,
        "relative": 3,
        "child": 4,
        "grand parents": 5,
        "employee": 6,
        "other": 7,
        "spouse": 8
    }
    if not isinstance(relation, str):
        return relation_dict["other"]
    relation = " ".join(relation.split()).lower()
    
    
    return relation_dict.get(relation, relation_dict["other"])

def validate_gender(gender=None):
    gender_dict = {
        "Male":"M",
        "Female": "F"
    }
    gender = " ".join(gender.split()).lower()

    for key in gender_dict:
        if key in gender_dict:
            return gender_dict[key]
        
    if gender == "m":
        return gender_dict["Male"]
    elif gender == "f":
        return gender_dict["Female"]
    else:
        return gender_dict["Male"]

def validate_family(new_id, families={}):  
    parts = new_id.split("/")
    for part in parts:
        if re.match(r"^[A-Za-z]+\d+$", part): 
            family_id = part
            families.setdefault(family_id, []).append(new_id)
            break 
    return families
