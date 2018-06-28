from datetime import date, timedelta
def days_diff(date1, date2):
    f = date(*date1)
    s = date(*date2)
    return abs((s - f).days)
