import datetime
def convert(date_time):
    format="%b %d %Y %I:%M%p"
    datetime_str=datetime.datetime.strptime(date_time, format)
    return datetime_str
date_time='Dec 4 2018 10:07AM'
print(convert(date_time))
