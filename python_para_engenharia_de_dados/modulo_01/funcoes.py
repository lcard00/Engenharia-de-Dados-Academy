from matplotlib.image import resample
from matplotlib.widgets import EllipseSelector


def soma(a, b):
    return a +b
    
# rersultado = soma(1,2)

# print(rersultado)

# print(abs(-1))
lista = list(range(10))


def filtra_par(x):
    if x%2 == 0:
        return True
    else:
        return False
    
lista2 = list(filter(filtra_par, lista))

# print(lista2)    
    

def dobro(x):
    return x * 2

lista3 = list(map(dobro, lista2)) 

print(lista3)