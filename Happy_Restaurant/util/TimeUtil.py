
from datetime import datetime

"""
    This function will take the current 
"""
def get_time_as_int():
    return int(datetime.now().strftime("%Y%m%d%H%M%S"))

#This function will return the format of mm/dd/yy hh:mm:ss
def get_current_date():
    return datetime.now().strftime("%x %X")

#This function will return format of dd_mm_yyyy
def get_today_date():
    return datetime.now().strftime("%d_%m_%Y")
