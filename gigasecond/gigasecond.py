from datetime import datetime,timedelta

def add_gigasecond(year, month, day, hour=0,minute=0,seconds=0):
    dbd = datetime(year,month,day,hour,minute,seconds)
    tdelta = timedelta(seconds=1000000000)
    sum = dbd + tdelta
    return sum.year, sum.month, sum.day, sum.hour, sum.minute, sum.second


