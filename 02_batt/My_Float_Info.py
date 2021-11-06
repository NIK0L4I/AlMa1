import math
import sys


def geteps():
    """
    Diese Funktion brechnet die Maschinengenauigkeit, indem sie den Wert 1 so oft
    halbiert, bis die Differenz |(1+y) - 1| = 0 und gibt diese als String zurück.
    >>> geteps()
    '2.220446049250313e-16'
    """
    y = 1
    while 1+y != 1 :
        y /= 2
    return "{}".format(2*y)

def getmin():
    """
    Diese Funktion berechnet die kleinste darstellbare positive Zahl x_{min}, indem sie den Wert 1
    so oft halbiert, bis y/2 == 0 interpretiert werden würde und gibt diese als String zurück.
    >>> getmin()
    '5e-324'
    """
    y = 1
    while y/2 != 0 :
        y /= 2
    return "{}".format(y)

def getmax():
    """
    Diese Funktion berechnet die größte darstellbare Zahl x_{max}, indem sie den Wert 1
    so oft verdoppelt, bis y*2 == float('+inf') interpretiert werden würde und gibt diese als String zurück.
    >>> getmax()
    '8.98846567431158e+307'
    
    Größter tatsächlicher float:
    >>> sys.float_info.max
    '1.7976931348623157e+308'

    Aber 2*8.98846567431158e+307 würde von python bereits als float(+'inf') interpretiert.
    Das liegt daran, dass |0|11111|1111| als NaN oder 'inf' interpretiert wird,
    aber |0|11110|1111| größer ist als |0|011111|1111|. 
    """
    y = 1.0
    while y*2 != float('+inf'):
        y *= 2.0
    return "{}".format(y)
    

def main():
    print(geteps())
    print(getmin())
    print(getmax())    

if __name__ == "__main__":
    main()