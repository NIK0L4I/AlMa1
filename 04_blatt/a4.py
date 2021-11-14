
from os import write
import csv
import timeit
import numpy as np
import matplotlib.pyplot as plt

def bubbleSort(arr):
    for _ in range(0,len(arr)):
        swapped = False
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
        if swapped == False:
            break
    return arr

def main():
    time = []
    with open("laufzeiten3.csv", "a") as file:
        for k in range(1,9):
            arr1 = np.random.randint(100, size=4**k)
            t1 = timeit.timeit(lambda: bubbleSort(arr1), number=1)
            time.append(t1)
            writer = csv.writer(file)
            writer.writerow("{},{}".format(str(t1),4**k))
    plt.plot(time) 
    plt.show()

if __name__ == '__main__':
    main()