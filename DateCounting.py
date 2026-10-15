def split_date(date: str):
    """
    Given a date in format yyyy-mm or yyyy-mm-dd, splits in 2 respectively 3 strings containing the year, month and potentially day

    :param date: the date to split, given as a string

    :return: 2, respectively 3, strings containing the year, month and potentially day in that order 
    """
    if len(date) == 7:
        return date[:4], date[5:]
    elif len(date) == 10:
        return date[:4], date[5:7], date[8:]

def count_months(sd, ed):
    (sy, sm := split_date(sd)) if len(sd) == 7 else (sy, sm, _ := split_date(sd))
    (ey, em := split_date(ed)) if len(ed) == 7 else (ey, em, _ := split_date(ed))

    return (int(ey) - int(sy)) * 12 + int(em) - int(sm)
    #e_year - s_year + e_month - s_month