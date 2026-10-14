import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def make_graphs(words, ana):
    print("Graphic design is my passion")
    fig, ax = plt.subplots()
    ax.bar(words, ana[0], color='forestgreen', width=1, align="center")
    ax.hlines(ana[1], xmin=np.arange(-0.5, len(words)-0.5, 1), xmax=np.arange(0.5, len(words)+0.5, 1), linewidth=3.2, color='coral')

    plt.show()
