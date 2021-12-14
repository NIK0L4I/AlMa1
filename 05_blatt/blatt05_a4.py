import numpy as np
import matplotlib.pyplot as plt
import timeit

def quick_sort(arr, l:int, r:int):
    # Innere Funktion für die Partitionierung
    def partition(a,l1:int,r1:int):
        x = a[r1]
        i = l-1
        for j in range (l1,r1):
            if a[j] <= x:
                i +=1
                a[i], a[j] = a[j], a[i] # Vertausche
        a[i+1], a[r1] = a[r1], a[i+1]   # Vertausche
        return i+1

    # Default case: array size = 1
    if len(arr) == 1:
        return arr
    # low < high, bc high < low doesnt make sense
    if l < r:
        q = partition(arr,l,r)
        quick_sort(arr,l,q-1)
        quick_sort(arr,q+1,r)

def plotting(time):
    x = [2**k for k in range(len(time))]
    y = time
    plt.xlabel('Größe des Arrays')
    plt.ylabel('Zeit in s')
    plt.xscale('log',base=2)
    plt.plot(x,time,'b', label='T(quick_sort())')

    model = np.poly1d(np.polyfit(x, y, 2))
    polyline = np.linspace(0, max(x), 50)
    plt.plot(polyline, model(polyline),'r', label='$\mathcal{O}(n^2)$')

    model1 = np.poly1d(np.polyfit(x*np.log10(x), y, 1))
    print(model1)
    plt.plot(polyline,model1(polyline),'orange', label='$\mathcal{O}(n \dot \log(n))$')

    plt.legend()
    plt.show()

def main():
    time = []
    for k in range(16):    # Führt die Funktion Für Arrays der Länge 2**0 bis 2**15 aus
        arr = np.random.randint(100,size=2**k)  # Füllt das Array der Länge 2**k mit random int Werten im Bereich {0,...,99}
        n = len(arr)
        time.append(timeit.timeit(lambda: quick_sort(arr,0,n-1), number=1))   # misst die Zeit für quick_sort auf einem Array der Länge 2**k
        sorted = [arr[i] <= arr[i+1] for i in range(len(arr)-1)]    # Prüft ob für alle Werte im Array die Bedinung a[i] <= a[i+1]
        
        if(all(sorted)==False): # Ist das Array nicht sortiert wird eine Fehlermeldung ausgegeben.
            print("Error, das Array ist nicht sortiert.")
    plotting(time)

if __name__ == '__main__':
    main()