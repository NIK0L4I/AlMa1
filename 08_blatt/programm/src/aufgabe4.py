import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from queue import PriorityQueue 
# (a)
res_path = os.getcwd() + '/08_blatt/programm/ressources'

edges = {}
x_coords = {}
y_coords = {}


# Einlesen der .csv Daten
with open (res_path + '/xcoords.csv') as xcoord_file:
    x_coords = pd.read_csv(xcoord_file, header=None)

with open (res_path + '/ycoords.csv') as ycoord_file:
    y_coords = pd.read_csv(ycoord_file, header=None)

with open(res_path + '/edges.csv') as edges_file:
    edges = pd.read_csv(edges_file, header=None)

# Erstellung und Initialisierung der Adjazenzmatrix 
n = len(edges)
adjazenzMatrix = np.zeros((n,n))

# Plotten des Kartennetzes
def plotData():
    for i in range(len(edges)):
        x1 = x_coords.loc[edges[0][i]][0]
        y1 = y_coords.loc[edges[0][i]][0]
        # Edge
        x2 = x_coords.loc[edges[1][i]][0]
        y2 = y_coords.loc[edges[1][i]][0]
        
        plt.plot([x1, x2], [y1, y2], 'k')

    plt.plot(x_coords.loc[1758], y_coords.loc[1758], 'rx') # Knoten mit Index 1758 (Eingang zum Hörsaalzentrum Poppelsdorf)
    plt.plot(x_coords.loc[584], y_coords.loc[584], 'rx') # Knoten mit Index 584 (Mensa Nassestraße)
    plt.show()

# (b) Fügt die Kantengewichte in die Adjazenzmatrix ein, um eine Wegematrix mit der
# euklidischen Betragsnorm für Vektoren zu bestimmen.
def initAdjazenz():
    for i in range(len(edges)):
        x1 = x_coords.loc[edges[0][i]][0]
        y1 = y_coords.loc[edges[0][i]][0]
        x2 = x_coords.loc[edges[1][i]][0]
        y2 = y_coords.loc[edges[1][i]][0]
        # adjazenz[a][b] = sqrt( [x(a)-x(b)]^2 + [y(a) - y(b)]^2 )
        adjazenzMatrix[edges[0][i]][edges[1][i]] = np.sqrt((x1-x2)**2 + (y1-y2)**2)
    print(adjazenzMatrix[12][1364])

def dijkstra(src):
    visited = []
    costs = {v: float('inf') for v in range(n)}
    costs[src] = 0
    
    pq = PriorityQueue()
    pq.put((0, src))

    while not pq.empty():
        (dist, current) = pq.get()
        visited.append(current)

        for neigbor in range(n):
            if adjazenzMatrix[current][neigbor] != 0:
                distance = adjazenzMatrix[current][neigbor]

                if neigbor not in visited:
                    old_cost = costs[neigbor]
                    new_cost = costs[current] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neigbor))
                        costs[neigbor] = new_cost
    return costs

if __name__ == '__main__':
    #plotData()
    initAdjazenz()
    print(dijkstra(1758)[585])
