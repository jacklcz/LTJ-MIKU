'''
author:jack_lcz
date:2013-09-19 15:59
'''



import time,datetime
import gflags


FLAGS = gflags.FLAGS

gflags.DEFINE_string('start_date','2013-09-20','this is start_time ,is use to the loop date')
gflags.DEFINE_string('end_date','2013-09-28','this is end_time ,is use to the loo date')
gflags.DEFINE_string('default_date_format','%Y-%m-%d','format date_str')


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


def each_date(start_date=FLAGS.get('start_date','2013-09-20'),end_date=FLAGS.get('end_date','2013-09-21')):
    date_format = FLAGS.get('default_date_format','%Y-%m-%d')
    tm_start = time.strptime(start_date,date_format);
    start = time.mktime(tm_start)
    end = time.mktime(time.strptime(end_date,date_format))
    interval_days = int((end-start)/86400) +1
    for d in range(interval_days):
        yield time.strftime(date_format,time.localtime(start+d*86400))


if __name__ == "__main__":
    for day in each_date('2013-09-01','2013-09-20'):
        print day
    pass
