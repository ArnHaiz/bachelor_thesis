from collections import defaultdict
from month_range import Month, MonthRange


MONTH_IN_YEAR = 12


def make_stats(words : list[str], data : list[defaultdict], s_date, e_date):
    """
    Utilize the input data to infere statistics and usefull informations.

    :param words: list of string, the words which might change bwhavior in abstracts
    :param data: the abstracts to use for analysis
    :param s_date: the first year and month from which the data has been collected
    :param e_date: the last year and month from which the data has been collected

    :return: #TODO 
    """

    agg_data = defaultdict(list)
    word_count_per_month = defaultdict(int)
    paper_count_per_month = defaultdict(list)

    months = MonthRange.parse([s_date, e_date]).split()
    nbr_month = len(months)

    for i in range(nbr_month):
        date = str(months[i])

        date_data = []
        for d in data:
            if d.__contains__(date):
                date_data.append(d[date])

        agg_data[date] = list(set(date_data))

        word_count_per_month[date] = sum([s.count(words[j]) for j in range(len(words))] for s in agg_data[date])
        paper_count_per_month[date] = sum(sum(words[j] in d for d in agg_data[date]) for j in range(len(words)))

    nbr_paper = sum(len(a) for a in agg_data.values())


    return [nbr_paper, dict(word_count_per_month), dict(paper_count_per_month)]
