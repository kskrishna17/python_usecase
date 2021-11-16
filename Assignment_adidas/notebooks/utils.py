import pandas as pd
import numpy as np
import re

years = "\d{4}" #regular expression pattern to detect years. It checks for matching substrings with exactly 4digits
months="(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Nov|Dec)"

def check_alpha_numeric(text):
    if text is np.nan:
        return None
    elif text.isnumeric():
        return False
    else:
        return True
    
def check_get_year(text):
    reg_obj_year=re.search(years,text)
    if reg_obj_year:
        try:
            return text[reg_obj_year.span()[0]:reg_obj_year.span()[1]]
        except Exception as e:
            print(e)
            return None
    else:
        return None
    
def check_get_month(text):
    reg_obj_month=re.search(months,text,re.IGNORECASE)
    if reg_obj_month:
        try:
            return text[reg_obj_month.span()[0]:reg_obj_month.span()[1]].lower()
        except Exception as e:
            print(e)
            return "fir".lower()
    else:
        return "fir".lower()
