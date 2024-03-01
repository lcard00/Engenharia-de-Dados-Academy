dicionario = {
    "diligencia" : "Zelo, cuiodade e  aplicaćão na realizaćão de algo.",
    "corroborar" : "Confirmar a existência ou a verdade de dar provas de comprovar.",
    "verbete" : "Conjunto que contém essas palavras, com suas acepcoes, significados e explicacoes."
}


print(dicionario["corroborar"])


# print(dicionario.keys())
# print(dicionario.values())
# print(dicionario.items())

palavra = input("Informe a palavra para buscar no dicionário: ")


print(dicionario.get(palavra, "Palavra não encontrada!"))

# if palavra in dicionario:
#     print(f"{palavra} = {dicionario[palavra]}")
# else:
#     print("Palavra não encontrada!")
    
    
r = range(0, 11, 1)

dic = dict.fromkeys(r)

# print(dic)