"""
Mantendo a ordem de itens em uma lista.
.index(): imprime o índice do item selecionado na lista (entre parênteses)
.insert(): insere um item na lista no índice que indicarmos
"""
animals = ["ant", "bat", "cat"]
print(animals.index("bat"))

animals.insert(1, "dog")
print(animals)