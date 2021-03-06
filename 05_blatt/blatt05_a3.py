import numpy as np
import matplotlib.pyplot as plt
#import timeit

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

    if l < r:
        q = partition(arr,l,r)
        quick_sort(arr,l,q-1)
        quick_sort(arr,q+1,r)


time = []
for k in range(0,7):
    arr = np.randint(100,size=2**k)
    print(arr)
    quick_sort(arr)
    print(arr)
    #time = timeit.timeit(quick_sort(arr))

plt.plot(time)