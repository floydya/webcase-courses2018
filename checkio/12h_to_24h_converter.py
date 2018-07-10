import datetime


def time_converter(time):
    time = time.replace('p.m.', 'PM').replace('a.m.', 'AM')
    time = datetime.datetime.strptime(time, '%I:%M %p')
    return time.strftime('%H:%M')
