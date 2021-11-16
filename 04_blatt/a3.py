# %%
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from os import write
import csv
import pandas as pd

f1 = []
g1 = []
h1 = []

f1.append(6.74999999998871*np.exp(-5))
f1.append(0.004346300000000136)
f1.append(0.4447595999999998)
f1.append(45.7846787)
f1.append(4539.3007692)

plt.plot(f1,'oy')
plt.plot(g1,'or')
plt.savefig('.\\graphs\\functions.pdf', format='pdf')
# %%
