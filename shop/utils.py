from datetime import datetime, timedelta

def incrementor():
    info = {"count": 100}

    def number():
        info["count"] += 1
        return info["count"]
    return number


def is_leap_year(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def get_lapse():
    last_month = datetime.today().month
    current_year = datetime.today().year

    #is last month a month with 30 days?
    if last_month in [9, 4, 6, 11]:
        lapse = 30

    #is last month a month with 31 days?
    elif last_month in [1, 3, 5, 7, 8, 10, 12]:
        lapse = 31

    #is last month February?
    else:
        if is_leap_year(current_year):
            lapse = 29
        else:
            lapse = 30

    return lapse
