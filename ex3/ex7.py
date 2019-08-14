import eratosthenes
def twinp(n):
    D = {}
    L = eratosthenes.napa(n)
    for i in range(len(L)-2):
        if ((L[i + 1] - L[i]) == 2):
            D[L[i]] = L[i+1]
        if ((L[i + 2] - L[i]) == 2):
            D[L[i]] = L[i+2]
    return D

def mainEx7():
    n = int(input('> '))
    D = twinp(n)
    for i in D.keys():
        print(i,D[i])
        
