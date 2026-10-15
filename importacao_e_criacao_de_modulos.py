#Importar módulos

import math

resultado = math.sqrt(25)
print(resultado)

from math import sqrt

resultado = sqrt(50)
print(resultado)

#Funções e classes de módulos padrão

#Math
#Random
#Datetime

import random
import datetime

numero_aleatorio = random.randint(1, 10)
print(numero_aleatorio) #Imprime numero aleatorio entre 1 e 10

data_atual = datetime.datetime.now()
print(data_atual)