# %%
import numpy as np
import matplotlib.pyplot as plt

a = []
b = []
c = []
p = []
p.append(1)
p.append(np.sqrt(2)-1)

def dreitermrekursion(n:int):
    for k in range(2,n):
        p.append(-2*(p[k-1])+p[k-2])



def main():
    n = int(input("n"))
    dreitermrekursion(n)
    print(p)

if __name__ == "__main__":
    main()
    plt.plot(p)

# %%

# %%
