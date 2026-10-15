from DateCounting import split_date, count_months
MONTH_IN_YEAR = 12

def get_interval(start_date, end_date):
    """
    Given a start date and an end date in format yyyy-mm, creates an array containing the months spanning the interval in an array in format yyyy-mm

    :param start_date: the date in format yyyy-mm to start the interval from
    :param end_date: the date in format yyyy-mm to end the interval at

    :return: an array of strings whose elements are, in order, the months in the interval
    """
    nbr_month = count_months(start_date, end_date)
    splitted = split_date(start_date)
    sy = int(splitted[0]); sm = int(splitted[1])

    date_list = [None] * nbr_month

    for i in range(nbr_month):
        date = str(sy + (sm+i-1) // MONTH_IN_YEAR) + '-' + str(1 + (sm + i - 1) % MONTH_IN_YEAR).zfill(2)
        date_list[i] = date

    return date_list
