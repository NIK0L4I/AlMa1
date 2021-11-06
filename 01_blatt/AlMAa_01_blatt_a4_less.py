def func(m: int, n: int):
    """
    Für m,n \in IN \ {0} berechnet die Funktion die Darstellung von m als vielfaches von n + Rest
    ausschließlich mit Addition und Subtraktion und gibt diese als String des 
    Formats: "m = q*n + Rest" zurück.

    Beispiel I/0:
    >>> func(5,15)
    '5 = 0 * 15 + 5'

    """
    #Prüft, ob m, n positive natürliche Zahlen sind. Falls nicht gib eine Fehlermeldung zurück
    if m < 1 or n < 1:
        return "Error, es dürfen nur positive natürliche Zahlen eingegeben werden!"
    r = m
    q = 0
    # Aus r = m ergibt sich: solange r > n wird r um n reduziert und q um eins erhöht 
    while r > n:
        r -= n
        q += 1
    return "{} = {} * {} + {}".format(m, q, n, r)

def func_2(m:int, n:int):
    """
    Für m,n \in IN \ {0} berechnet die Funktion die Darstellung von m als vielfaches von n + Rest
    und gibt diese als String des Formats "m = q*n + Rest" zurück

    Beispiel I/0:
    >>> func(5,15)
    '5 = 0 * 15 + 5'

    """
    #Prüft, ob m, n positive natürliche Zahlen sind. Falls nicht gib eine Fehlermeldung zurück
    if m < 1 or n < 1:
        return "Error, es dürfen nur positive natürliche Zahlen eingegeben werden!"
    q = m//n
    r = m - (q * n)
    return "{} = {} * {} + {}".format(m, q, n, r)

def main():
    while True:
        try:
            command = int(input("[0]: exit, [1]: nur Addition und Subtraktion, [2]: (Ganzzahl-)Division und Multiplikation "))
            while command != 0:
                if command == 1:
                    m = int(input("Gibt die erste Zahl ein: "))
                    n = int(input("Gibt die erste Zahl ein: "))
                    print(func(m,n))
                elif command == 2:
                    m = int(input("Gibt die erste Zahl ein: "))
                    n = int(input("Gibt die erste Zahl ein: "))
                    print(func_2(m,n))
                elif command == 0:
                    exit()
                else:
                    print("Bitte gib ein gültiges Kommando ein.")
                command = int(input("[0]: exit, [1]: nur Addition und Subtraktion, [2]: (Ganzzahl-)Division und Multiplikation "))

        except ValueError:
            print('Bitte gib ausschließlich Zahlen ein.')
            
if __name__ == "__main__":
    main()

