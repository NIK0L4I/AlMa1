# %%
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

f1 = []
g1 = []

def f(n: int):
    if n % 2 == 0:
        return 0
    return n

def g(n:int):
    return np.sqrt(n)

for i in range(0,11):
    g1.append(g(i))
    f1.append(f(i))

plt.plot(f1,'oy')
plt.plot(g1,'or')
plt.savefig('.\\graphs\\functions.pdf', format='pdf')
# %%
