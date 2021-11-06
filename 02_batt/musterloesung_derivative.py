
# %%

import numpy
import matplotlib.pyplot as plt
h = []
cd = []
deriv = []
abs_err = []
rel_err = []

for i in range (0,31):
    h.append(2**(-i))
    cd.append((numpy.cos(1+h[i])) - numpy.cos(1-h[i])/(2*h[i]))
    deriv.append(-numpy.sin(1))
    abs_err.append(abs(cd[i] - deriv[i]))
    rel_err.append(abs_err[i] / deriv[i])

plt.loglog(h,abs_err)
plt.loglog(h,rel_err)
# %%
