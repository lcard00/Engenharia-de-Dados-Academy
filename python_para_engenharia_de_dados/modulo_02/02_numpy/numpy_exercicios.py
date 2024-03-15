import calendar
from importlib.machinery import all_suffixes
import numpy as np

def f_print(var, text = ""):
    print(text)
    print(var)
    print()

# Utilizando a biblioteca numpy siga as intruções:
#   1. Crie um array 6x6 preenchido com zero
#   2. Preencha o centro deste array com um array 4x4 preenchido com uns
#   3. Preencha o centro deste array com um array 2x2 preenchido com dois
#   4. Gere um segundo array 6x6 com números inteiros aleatórios entre 0 e 2 (seed 0)
#   5. Subtraia o primeiro array pelo segundo

# # 1 
# array = np.zeros((6,6),int)

# # array = np.random.randint(0, 80, (6, 6))

# # 2
# f_line = 1
# f_col = 5

# array[f_line:f_col, f_line:f_col] = 1

# # 3 
# f_line = 2
# f_col= 4

# array[f_line:f_col, f_line:f_col] = 2

# print(array)

# print()

# # 4 
# np.random.seed(0)
# array_random = np.random.randint(0, 3, (6, 6))

# print(array_random)

# print()

# # 5 
# print(array - array_random)


# array = np.zeros((6,6), int)
# f_print(array)

# array2 = array.copy()
# array2[1:5, 1:5] = np.ones((4, 4))

# f_print(array2)

# array3 = array2.copy()
# array3[2:4, 2:4] = np.full((2,2),2)

# f_print(array3)

# np.random.seed(0)
# array4 = np.random.randint(0, 3, (6,6))

# f_print(array4)

# array5 = array3 - array4

# f_print(array5)

# Crie um array de duas dimensões, no formato 9x9, com números de 0 a 80 ordenados de modo crescente e selecione:
#   1. Os números ímpares
#   2. Os números pares
#   3. Os múltiplos de 7
#   4. Os múltiplos de 10
#   5. Os números 32, 33, 42, 43


# dim = (9, 9)

# array = np.arange(81).reshape(dim)

# f_print(array)

# # 1
# is_odd = array % 2 == 1

# a_odd = array[is_odd]
# f_print(a_odd, "1. Os números ímpares: ")

# # 2
# is_even = array %  2 == 0 

# a_even =  array[is_even]
# f_print(a_even, "2. Os números pares: ")

# # 3
# is_mult7 = array %  7 == 0

# a_mult7 = array[is_mult7]
# f_print(a_mult7, "3. Os múltiplos de 7: ")

# # 4
# is_mult10 = array %  10 == 0

# a_mult10 = array[is_mult10]
# f_print(a_mult10, "4. Os múltiplos de 10: ")

# # 5 

# f_num = (32, 33, 42, 43)
# a_filter = np.isin(array, f_num)

# f_print(array[a_filter], "5. Os números 32, 33, 42, 43: ")

# dim = (9, 9)
# array = np.arange(81, dtype=int, ).reshape(dim)

# f_print(array)

# mask_odd = array % 2 == 1

# f_print(array[mask_odd])

# mask_even  = array % 2 == 0

# f_print(array[mask_even])

# mask_mod7 = array % 7 == 0

# f_print(array[mask_mod7])

# # mask_mod10 = array % 10 == 0

# # f_print(array[mask_mod10])
# f_print(array.diagonal())

# mask_num = [32, 33, 42, 43]
# a_num = np.isin(array, mask_num)

# f_print(array[a_num])

# # lines = [3, 3, 4, 4]
# # col = [5, 6, 6, 7 ]

# # f_print(array[lines, col])

# Crie um array com três dimensões, onde a primeira dimensão são os dias da semana (seg a dom), a segunda dimensão
# são as semanas do mês (considere apenas 4 para todos os meses), e a terceira são os meses do ano (jan a dez).add()
#   1. Marque os finais de semana com a letra W
#   2. Marque o começo do mês com a letra S
#   3. Marque o final do mês com a letra E
#   4. Marque os demais dias com a letra D
#   5. Marque os feriados nacionais com a letra F
#       - 01/01 - Ano novo
#       - 15/04 - Paixão de Cristo
#       - 21/04 - Tiradentes
#       - 01/05 - Dia do Trabalho
#       - 07/09 - Independência do Brasil
#       - 12/10 - Nossa Senhora Aparecida
#       - 02/11 - Finados
#       - 15/11 - Proclamação da República
#       - 25/12 - Natal

f_month = 12
f_week = 4
f_week_days = 7

calendary=  np.full(([f_month, f_week, f_week_days]), "D", dtype=str)

calendary[:, :, -2:] = "W"
calendary[:, 0, 0] = "S"
calendary[:, -1, -1] = "E"

# mask_days = calendary == ""  
# calendary[mask_days] = "D"

# mask_WSE = ~np.isin(calendary, ["W", "S", "E"])
# calendary[mask_WSE] = "D"

months = [0, 3, 3, 4, 8, 9, 10, 10, 11]
weeks = [0, 2, 2, 0, 0, 1, 0, 2, 3]
days = [0, 0, 6, 0, 6, 4, 1, 0, 3]

calendary[months, weeks, days] = "F"

f_print(calendary)

# weekends = np.full_like(calendary, False, dtype=bool)
# weekends[:, :, -2:] = True

# calendary[weekends] = "W"

# first_day = np.full_like(calendary, False, dtype=bool)
# first_day[:, 0, 0] = True

# calendary[first_day] = "S"

# end_day = np.full_like(calendary, False, dtype=bool)
# end_day[:, 3, -1] = True

# calendary[end_day] = "E"

# calendary[~weekends & ~first_day & ~end_day] = "D"

# holidays = np.full_like(calendary, False, dtype=bool)

# #       - 01/01 - Ano novo
# holidays[0, 0, 0] = True

# #       - 15/04 - Paixão de Cristo
# #       - 21/04 - Tiradentes
# holidays[3, 2, (0, -1)] = True

# #       - 01/05 - Dia do Trabalho
# holidays[4, 0, 0] = True

# #       - 07/09 - Independência do Brasil
# holidays[8, 0, -1] = True

# #       - 12/10 - Nossa Senhora Aparecida
# holidays[9, 1, 4] = True

# #       - 02/11 - Finados
# #       - 15/11 - Proclamação da República
# holidays[10, (0, 2), (1, 0)] = True

# #       - 25/12 - Natal
# holidays[11, 3, 3] = True

# calendary[holidays] = "F"




