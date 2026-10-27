import calendar
import json
import xml.etree.ElementTree as ET
from collections import defaultdict
from time import sleep
from month_range import Month, MonthRange

import CST
from Search import search
from DateCounting import split_date, count_months
from interval import get_interval


is_usable = lambda license: not license in CST.unusable_licenses
namespace = {'ns': 'http://www.openarchives.org/OAI/2.0/'}




def get_from_servers(servers, current_date, start_date, end_date):
    """ 
    collect data according to the arguments from the given servers one after the other.
    
    :param servers: list of the servers to search on
    :param current_date: date at the start of the program
    :param s_date: date to use as the starting date in the search, if specified
    :param e_date: date to use as the ending date in the search, if specified
    :return: a list of dicts containing the abstracts of each server, organised by year and month
    """

    print("Start of data collection...")
    serverIndex_to_function = {0: get_from_biorxiv, 1: get_from_medrxiv, 2: get_from_arxiv} # TODO maybe clarify in a "how to change code" file that this is here

    interval = MonthRange.parse([start_date, end_date]).split()
    results = [defaultdict(list) for _ in servers]
    nbr_months = len(interval)

    for i in range(nbr_months):
        print(f"{100 * i / nbr_months:.2f}%")

        m = interval[i]
        s_date = m.first_day.isoformat()
        e_date = m.last_day.isoformat()
        print(s_date, 'to', e_date)
        for j in range(len(servers)):
            results[j][str(m)] = serverIndex_to_function[j](server=servers[j], s_date=s_date, e_date=e_date, current_time=current_date)
        
        # not required for functionality, but this is to ensure to not overload the servers, per request of most mass data collection APIs
        sleep(1.5)
        
    print(f'100% - End of data collection.')
    return results



def get_from_biorxiv(*, server, s_date, e_date, current_time, subject=None, cursor=0):
    """
    Formats the arguments into a url according to the biorxiv api, makes the request and formats
    the result into a dict of the abstratcs organised by year and month yyyy-mm.

    :param server: the url to use for the request
    :param s_date: the first date of the interval of publication in which papers are considered
    :param e_date: the last date of the interval of publication in which papers are considered
    :param current_time: the date at the beginning of the execution of the program as a whole
    :param subject: defines the category of interest for this request
    :param cursor: number of papers to ignore, counted from the first element of the list

    :return: a defaultdict(list) with the abstracts accessible by year and month
    """

    s_date = f"/{s_date}"
    e_date = f"/{e_date}"
    interval = s_date + e_date
    subject = f"?category={subject}" if subject != "" else ""
    cursor = f"/{cursor}"
    url = f"{server}{interval}{subject}{cursor}/JSON"

    r = search("BioRxiv", url)

    if r == None or r == "":
        return None
    

    abstracts = []
    year_months = []
    results = defaultdict(list)

    try:
        dic = json.loads(r)['collection']

        for paper in dic:
            if is_usable(paper['license']):
                abstracts.append(paper['abstract'])
                year_months.append(paper['date'][:7])

        for y in year_months:
                results[y] = [abstracts[i] for i, x in enumerate(year_months) if x == y]
    except:
        print("Failed to extract data from BioRxiv.")
        return None

    return results



def get_from_medrxiv(*, server, s_date, e_date, current_time, subject=None, cursor=0):
    """
    Formats the arguments into a url according to the medrxiv api, makes the request and formats
    the result into a dict of the abstratcs organised by year and month yyyy-mm.

    :param server: the url to use for the request
    :param s_date: the first date of the interval of publication in which papers are considered
    :param e_date: the last date of the interval of publication in which papers are considered
    :param current_time: the date at the beginning of the execution of the program as a whole
    :param subject: defines the category of interest for this request
    :param cursor: number of papers to ignore, counted from the first element of the list

    :return: a defaultdict(list) with the abstracts accessible by year and month
    """

    s_date = f"/{s_date}"
    e_date = f"/{e_date}"
    interval = s_date + e_date
    subject = f"?category={subject}" if subject != None else ""
    cursor = f"/{cursor}"
    url = f"{server}{interval}{subject}{cursor}/JSON"

    r = search("MedRxiv", url)

    if r == None or r == "":
        return None
    
    abstracts = []
    year_months = []
    results = defaultdict(list)
    try:
        dic = json.loads(r)['collection']

        for paper in dic:
            if is_usable(paper['license']):
                abstracts.append(paper['abstract'])
                year_months.append(paper['date'][:7])

        for y in year_months:
                results[y] = [abstracts[i] for i, x in enumerate(year_months) if x == y]
    except:
        print("Failed to extract data from MedRxiv.")
        return None

    return results




def get_from_arxiv(*, server, s_date=None, e_date=None, subject=None, cursor=0, current_time):
    """
    Formats the arguments into a url according to the arxiv api, makes the request and formats
    the result into a dict of the abstratcs organised by year and month yyyy-mm.

    :param server: the url to use for the request
    :param s_date: the first date of the interval of publication in which papers are considered
    :param e_date: the last date of the interval of publication in which papers are considered
    :param subject: defines the category of interest for this request
    :param cursor: number of papers to ignore, counted from the first element of the list

    :return: a defaultdict(list) with the abstracts accessible by year and month
    """

    if not (s_date == None or e_date == None):
        s_date = f"&from={s_date if s_date is not None else CST.STANDARD_START_DATE[:9]}"
        e_date = f"&until={e_date if e_date is not None else current_time[:9]}"


    # set = f"&set={subject}" if subject is not None else ""
    url = f"{CST.ARXIV_OAI_URL}verb=ListRecords{s_date}{e_date}&metadataPrefix=arXiv"

    r = search(server, url)

    if r is None or r == "":
        return None

    abstracts = []
    year_months = []
    results = defaultdict(list)
    # max_ids_sim = 500
    # pdfs = []

    try:
        root = ET.fromstring(r)
        papers = root.find('ns:ListRecords', CST.arxiv_namespace).findall('ns:record', CST.arxiv_namespace)

        for paper in papers:
            for elem in paper:
                for e in elem.iter():
                    match e.tag.split('}', 1)[1]:
                        case 'datestamp':
                            year_months.append(e.text[:7])
                        case 'license':
                            if not is_usable(e.text):
                                break
                        case 'abstract':
                            abstracts.append(e.text)

        # TODO if time available remove paper whilst sorting instead of going through all of them every time
        for y in year_months:
            results[y] = [abstracts[i] for i, x in enumerate(year_months) if x == y]

        # client = Client(page_size=max_ids_sim)
        # r = client.results(search=Search(id_list=ids))


        # for p in r:
        #     if not p.pdf_url is None:
        #         try:
        #             response = requests.get(p.pdf_url)
        #             if response.status_code == '200':
        #                 pdfs.append(response.text)
        #         except ConnectionError:
        #             print(f'failed to get file {p.title} at {p.pdf_url}')
        #     else:
        #         pdfs.append(p.summary)
    except AttributeError:
        print("Failed to extract data from ArXiv.")
        return None

    return results
