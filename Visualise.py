import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def visualise(words, stats):
    """
    make graphs and save them from the statistics given and the list of banned words

    :param words: list of banned words
    :param stats: the statistics to make graphs of in a list
    """
    [nbr_paper, word_count_per_month, paper_count_per_month] = stats

    fig, ax = plt.subplots()
    ax.bar(word_count_per_month.keys(), word_count_per_month.values(), color='limegreen', alpha=0.68, width=1, align="center")
    ax.hlines(paper_count_per_month.values(), xmin=np.arange(-0.5, len(word_count_per_month.keys())-0.5, 1), xmax=np.arange(0.5, len(word_count_per_month.keys())+0.5, 1), linewidth=3.2, color='coral')

    plt.show()

    return