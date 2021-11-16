# %%
import timeit
import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.polynomial import poly1d
import pandas as pd

def bubbleSort(arr):
    for _ in range(0,len(arr)):
        swapped = False
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:   
                arr[i], arr[i+1] = arr[i+1], arr[i]     # Tauscht arr[i] und arr[i+1]
                swapped = True
        if swapped == False:    # in einem kompletten Durchlauf wurde nicht getauscht
            break               # -> arr[] ist sortiert
    return arr

def main():
    time = []
    for k in range(1,9):
        arr1 = np.random.randint(100, size=10**k)   # Lege zufälliges Array der größe 10^k an mit Werten aus {0,...,99}
        t1 = timeit.timeit(lambda: bubbleSort(arr1), number=1)  # Misst die Zeit, die BubbleSort für das sortieren eines Arrays der größe 10^k benötigt
        time.append(t1)
    plt.plot(time) 
    plt.show()

def plot_time(xscale_value):
    '''
    Plottet den Graphen der Laufzeit des BubbleSort-Algorithmus aus einer csv-Datei für {xscale_value}**K viele Elemente
    Führt anschließend eine Regressionsanalyse durch, um die Werte mit einer polynomiellen Funktion vom Grad 2
    zu approximieren.
    '''
    time = []
    df = pd.read_csv("laufzeiten.csv")
    x = df['n']
    y = df['Laufzeit']
    model = np.poly1d(np.polyfit(x, y, 2))
    polyline = np.linspace(0, xscale_value**5, 50)
    print(model)
    plt.xlabel('Anzahl der Elemente')
    plt.ylabel('Laufzeit in s')
    plt.xscale("log", base=xscale_value)
    plt.plot(x,y,'ob',label='Laufzeit BubbleSort')
    plt.plot(polyline, model(polyline),\
        'r',label='${}x^2 + {}x + {}$'.format(\
            round(model[2],8), round(model[1],5), round(model[0],3)))
    #plt.plot(x,x**2,'y',label='$x^2$')
    plt.legend(loc='upper left')
    plt.savefig('./graphs/laufzeit.eps', format='eps')
    plt.show()

if __name__ == '__main__':
    #main()
    plot_time(10)
# %%
