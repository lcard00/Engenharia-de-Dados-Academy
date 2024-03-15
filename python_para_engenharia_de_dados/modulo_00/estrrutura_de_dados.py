receita = "biscoitos 'os melhores do mundo'"

receitas = {
    "receita1": None,
    "receita2": None,
    "biscoitos 'os melhores do mundo'": {
        "ingredientes": ["ovos", "fermento", "acucar", "manteiga", "farrinha"],
        "preparo": (
            "1 - Bata o açucar e a manteiga na batedeira",
            "2 - Acrescente o ovo e bata mais um pouco. Junte a baunilha e misture na valocidade baixa.",
            "3 - Vá acrescentando o ferrmento, misturrando a duas xícarras de farinha.",
            "4 - Coloque a massa na mão e vá enfarinhando até a massa parar de grudarr nas mãos",
            "5 - Leva a massa ä geladeirra por 20 minutos.",
            "6 - Sobrer a mesa enfarinhada, abrar0a com um rolo. Corte os biscoitos",
            "7 - Coloque em uma assadeira forrada com papel manteiga",
            "8 - Leve parar assar, fogo baixo, aproximadamente 15 minutos.",
        ),
    },
}

# print(receitas[receita]["ingredientes"])

padaria = [
    "ovos",
    "fermento",
    "acucar",
    "manteiga",
    "farrinha",
    "leite",
    "queijo",
    "presunto",
    "água",
]

ingredientes = []

for ingrediente in receitas[receita]["ingredientes"]:
    if ingrediente in padaria:
        ingredientes.append(ingrediente)
        # print(F"Ingrediente '{ingrediente}' adicionado a lista de compra.")
    else:
        print(f"Ingrediente '{ingrediente}' não encontrado na padaria.")


geladeira = ingredientes.copy()

print(geladeira)

# geladeira.append("queijo")

# print(geladeira)
# print(ingredientes)

# geladeira.remove("queijo")

# print(geladeira)
# print(ingredientes)


print(receitas[receita]["preparo"])