"""
Mantendo a ordem de itens em uma lista.
.index(): imprime o índice do item selecionado na lista (entre parênteses)
.insert(): insere um item na lista no índice que indicarmos
"""
animals = ["ant", "bat", "cat"]
print(animals.index("bat"))

animals.insert(1, "dog")
print(animals)


"""
1 .
Use o .index()método para encontrar o índice de "duck". Atribua esse resultado a 
uma variável chamada duck_index.
Em seguida, use o .insert()método com duck_indexcomo primeiro argumento e a 
string "cobra"como segundo argumento.
"""

animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")

animals.insert(duck_index, "cobra")

print(animals) # Observe what prints after the insert operation