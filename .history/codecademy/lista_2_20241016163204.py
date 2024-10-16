letters = ['a', 'b', 'c']
letters.append('d')
print(len(letters))
print(letters)

print()
"""
1 .
Nas linhas 18, 19 e 20, acrescente mais três itens à 'suitcaselista', assim como a 
segunda linha do exemplo acima. Em seguida, defina em 'list_length' o valor igual
ao comprimento da suitcaselista.
"""

suitcase = [] 
suitcase.append("sunglasses")

# Your code here!
suitcase.append("biquini")
suitcase.append("maio")
suitcase.append("canga")

list_length = len(suitcase) # Set this to the length of suitcase

print("There are %d items in the suitcase." % (list_length))
print(suitcase)