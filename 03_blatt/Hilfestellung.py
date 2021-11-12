# %%
import matplotlib.pyplot as plot
import numpy as math
def N3TR(a, b, c, p0, p1): #a,b,c sind Funktionen, die einem den Wert von ak bzw bk bzw ck geben.
    #Notiz an mich selbst: wenn Zeit übrig, Laufzeitoptimierung und Rückgabe von Dictionary
    def pk(k , l_pk = [p0,p1]):
        if k == 0: #p0 ist schon vorgegeben
            return l_pk[0]
        elif k == 1: #p1 ist ebenfalls schon vorgegeben
            return l_pk[1]
        else:
            if len(l_pk) < k:#wenn Wert von k-1 noch nicht bekannt, rechne ihn aus.
                for i in range(len(l_pk),k):
                    l_pk.append(pk(i, l_pk))
            print(l_pk)        
            return (a(k)*l_pk[k-1])+(b(k)*l_pk[k-2])+c(k) #rechnet rekursiv, über die, in der Vorlesung besprochene Formel, den kten wert von pk aus.
    return pk

def GL(a,b,p0,p1):
    L1 = (a/2) + math.sqrt(((a**2)/4)+b)
    L2 = (a/2) - math.sqrt(((a**2)/4)+b)
    beta = (p1-L1*p0)/(L2-L1)
    alpha = p0 - beta
    def pk(k):
        print(alpha * (L1**k) + beta * (L2**k))
        return alpha * (L1**k) + beta * (L2**k)
    return pk

def Miller(n,a,b):
    p = [0] * (n+1)
    pk = [0] * (n+1)
    p[n-1] = 1

    for k in range(n, 1, -1):#für k = n, n-1,..., 2
        p[k-2] = -1*(a(k)/b(k))* p[k-1] + (1/b(k)) * p[k]
    for k in range(0,n+1):
        pk[k] = p[k]/(math.sqrt((p[0]**2)+(p[1]**2)))
    print(pk)
    return pk

pk = N3TR(lambda a: -2, lambda b: 1, lambda c: 0, 1, math.sqrt(2)-1)
plot.plot([i for i in range(0,46)], [pk(i) for i in range(0,46)])
plot.show()

pk2 = GL(-2, 1, 1, math.sqrt(2)-1)
plot.plot([i for i in range(0,46)], [pk2(i) for i in range(0,46)])
plot.show()

pk3 = Miller(45,lambda a : -2, lambda b: 1)
plot.plot([i for i in range(0,46)], pk3)
plot.show()

# %%
