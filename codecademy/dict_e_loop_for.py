"""
1.Use um for loop para percorrer o webster dicionário e imprimir todas as 
definições.
"""

webster = {
  "Aardvark" : "A star of a popular children's cartoon show.",
  "Baa" : "The sound a goat makes.",
  "Carpet": "Goes on the floor.",
  "Dab": "A small amount."
}

# Add your code below!
for webs in webster: # loop sobre cada chave do dict (webster)
    print(webster[webs]) # pra cada chave webs, webster[webs] acessa o valor associado a essa chave