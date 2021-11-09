# %%
import numpy as np
import matplotlib.pyplot as plt

def dreitermrekursion(n, a, b, c, p0, p1):  #a, b, c sind (Lambda-)Funktionen hier jedoch konstant
    p = []
    p.append(p0)    # Startwert 1: p_0 = p0 an k = 0
    p.append(p1)    # Startwert 2: p_1 = p1 an k = 1
    for k in range(2,n): # brechnet die Werte von p_k bis p_n, nach der Funktionsvorschrift und speichert sie in p:
        p.append(a(k)*p[k-1]+b(k)*p[k-2]+c(k))   
    return p    # gibt die Liste p zurück

def geschl_lsg(n, a, b, p0, p1):
    p = []
    p.append(p0)    # Startwert 1: p_0 = p0 an k = 0
    p.append(p1)    # Startwert 2: p_1 = p1 an k = 1
    lambda1 = a/2 + np.sqrt((a**2/4)+b)
    lambda2 = a/2 - np.sqrt((a**2/4)+b)
    beta = (p1 - lambda1*p0)/(lambda2 - lambda1)
    alpha = p0 - beta
    l1 = lambda1
    l2 = lambda2
    for k in range(2,n):
        l1 *= lambda1   # l1**(k)
        l2 *= lambda2   # l2**(k)
        p.append(alpha*l1+beta*l2)
    return p    # gibt die Liste p zurück

def miller(n, a, b):    #a und b sind (Lambda-)Funktionen hier jedoch konstant
    p = []
    pk = []
    p.append(0)     # Startwert 1: p^_n = 0 an k = n 
    p.append(1)     # Startwert 2: p^_{n-1} = 1 an k = n-1
    for k in range(2,n+1):  # Berechnet die Werte die Werte von p^k schreibt sie jedoch in falsche Reihenfolge ins Array
        p.append(-(a(k)/b(k))*p[k-1] + (1/b(k)) * p[k-2])
    p.reverse()     # Dreht die Reihenfolge der Liste um
    for k in range(0,n-2):  # Normierung
        pk.append(p[k] / np.sqrt(p[0]**2+p[1]**2))
    return pk

def plot_graphs(arr): 
    plt.plot(arr)
    plt.show()

def main():
    p1 = dreitermrekursion(46,lambda a:-2, lambda b:1, lambda c:0,1, np.sqrt(2)-1)
    p2 = geschl_lsg(46, -2, 1, 1, np.sqrt(2)-1)
    p3 = miller(46,lambda a:-2, lambda b:1)
    plot_graphs(p1)
    plot_graphs(p2)
    plot_graphs(p3)
    

if __name__ == "__main__":
    main()
# %%
