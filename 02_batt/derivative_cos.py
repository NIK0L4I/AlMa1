# %%
import math
import matplotlib.pyplot as plt

# Dekalartion und Initialisierung der Listen mit Platz für 30 Werte
list = [None] * 30
abs_err = [None] * 30
rel_err = [None] * 30
x_steps = [None] * 30
x_0 = float(1)



def derivative_cos():
    """
    Diese Funktion approximiert die 1. Ableitung von cos(x), an der Stelle x_0 = 1, über 30 Iterationen über i durch die
    Funktionsvorschrift:
        (cos(x_0 + h) - cos(x_0 - h)) / (2*h) mit Schrittweite h_i = 2 ** (-i)
    """

    for i in range(0,30):
        h = float(2 ** (-i))
        list[i] = (math.cos(x_0 + h) - math.cos(x_0 - h))/ (2*h)
        abs_err[i] = abs(list[i] + math.sin(1))
        rel_err[i] = abs(abs_err[i] / list[i])
        x_steps[i] = h

def plot_errors():
    """
    Dies ist eine Hilfsfunktion zum plotten der Fehlerdaten mit log-log-skalierten Achsen
    """
    # Absoluter Fehler
    plot1 = plt.figure(1)
    plt.xscale('log', base=2)
    plt.yscale('log', base=2)
    plt.xlabel('h_i')
    plt.ylabel('approximation')
    plt.xlim(max(abs_err), min(abs_err))
    plt.plot([x_steps],[abs_err],'or')   
    plt.title('Absoluter Felher')  
    plt.show   
    #plt.savefig('.\\graphs\\abs_error.eps', format='eps')

    # Relativer Fehler
    plot2 = plt.figure(2)
    plt.xscale('log', base=2)
    plt.yscale('log', base=2)
    plt.xlabel('h_i')
    plt.ylabel('approximation')
    plt.title('Relativer Felher')
    plt.xlim(max(rel_err), min(rel_err))
    plt.plot([x_steps],[rel_err],'or')     
    plt.show
    #plt.savefig('.\\graphs\\rel_error.eps', format='eps')

def main():
    derivative_cos()
    plot_errors()

if __name__ == "__main__":
    main()
    
# %%


