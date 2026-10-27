import json
import sys
import datetime

from CST import PRE_PRINT_SERVERS
from CST import BANNED_LIST
from CST import STANDARD_START_DATE
from DataAcquisition import get_from_servers
from Analytics import make_stats
from Visualise import visualise


def start():
    """ 
    Main method of the program. Handles the flow of the program.
    First, getting system arguments for user input, then getting abstracts from pre-print servers,
    then analysing and making statistics out of the data and finally visualising data.
    """

    s_date, e_date = sys.argv[1:3]
    current_date = str(datetime.datetime.today()).split()[0]
    print(f"current day is {current_date}")

    if not (s_date == "None" or e_date == "None"):
        s_date = s_date[:7]
        e_date = e_date[:7]
    else:
        s_date = STANDARD_START_DATE[:7]
        e_date = current_date[:7]

    data = get_from_servers(PRE_PRINT_SERVERS, current_date, s_date, e_date)
    no_none_data = [d for d in data if d is not None]

    file = open(r'./datas/data.json', 'w')
    json.dump(no_none_data, file)

    if no_none_data is []:
        print("No data available. Program ended.")
        return

    stats = make_stats(BANNED_LIST, no_none_data, s_date, e_date)
    visualise(BANNED_LIST, stats)

    print('End of execution.')


if __name__ == '__main__':
    start()
