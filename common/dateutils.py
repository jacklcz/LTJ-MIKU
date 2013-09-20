'''
author:jack_lcz
date:2013-09-19 15:59
'''



import time,datetime

def get_yesterday():
    return datetime.datetime.now() - datetime.timedelta(1)

def get_tomorrow():
    return datetime.datetime.now() + datetime.timedelta(1)

def get_currentdate():
    return datetime.datetime.now()



"""
get_format_date has two args ,default :date  = current_date and  format_str = '%Y-%m-%d'
"""
def get_format_date(date=get_currentdate().timetuple(),format_str='%Y-%m-%d'):
    return time.strftime(format_str,date)



"""
getbeforeOrAfter date , if you need get before one day, you can set plug = -1'
"""
def get_beforeOrAfter(plus,date=get_format_date()):
    tm = time.strptime(date,'%Y-%m-%d')
    ts = time.localtime(time.mktime(tm)+plus*86400)
    return time.strftime('%Y-%m-%d',ts);


if __name__ == "__main__":
    print(get_beforeOrAfter(-1,'1990-10-23'))
    #pass