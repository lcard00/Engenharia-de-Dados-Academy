import numpy as np

s_lista = [[10, 6, 4, 8], [5, 6, 8, 7]]
s_lista2 = [[5, 4, 3, 7], [9, 7, 6, 8]]

s_array = np.array(s_lista)


# print(s_lista[0][-1])

# [semestre, prova]
# print(s_array[0, -1])

# print(s_array.ndim)

# print(s_array + 1)
# print(s_array - 1)
# print(s_array * 2)
# print(s_array / 2)
# print(s_array / 2)
# print(s_array ** 2)
# print(s_array % 2)

# resultado = []
# for index in range(len(s_lista)):
#     resultado.append([])
#     for item in s_lista[index]:
#         alterado = item % 2
#         resultado[index].append(alterado)

# print(resultado)
# print(s_array % 2)

e_par = s_array % 2 == 0

# print(s_array[e_par])

# operacoes booleanas
# not -> ~
# and -> &
# or -> |
# xor -> ^

# print(s_array[~e_par])

multi5 = s_array % 5 == 0

filtro = multi5 & e_par

# print(s_array[multi5 | e_par])
# print(s_array[filtro])

a_lista = [
    s_lista,
    s_lista2
]

# print(a_lista)

a_array = np.array(a_lista)

# print(a_array)

# print(a_array[1, 0, -1])

# a_array = a_array[1, : , : ] + 1

# print(a_array)
# print(a_array)
# print(a_array[:, :, [0,-1]])

# ano = [0, 1, 1]
# semestre = [0, 0, 1]
# prova = [0, 1, 2]

# print(a_array[ano, semestre, ano])

# new_array = np.zeros([2, 2, 4])

# print(new_array)

# random_array = np.random.randint(0, 11, (2, 2, 4))

# print(random_array)

# random_array = np.round(np.random.uniform(0, 11, (2, 2, 4)), 2)

# print(random_array)

# random_array = np.random.choice(["A", "R"], (2, 2, 4))

# print(random_array)
