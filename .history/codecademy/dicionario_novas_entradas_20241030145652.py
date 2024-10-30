"""
Dicionários, assim como Listas, são mutáveis.
Após terem sido criados, podem ter adc NOVOS pares de chave:valor
ex.: dicionario_ja_criado[nova_chave] = novo_valor
Par de {} vazio é DICIONÁRIO vazio
Par de [] vazio é uma LISTA vazia

1. Adicione pelo menos mais três pares de chave-valor à menuvariável, com o 
nome do prato (como um "string") para a chave e o preço (um float ou inteiro) 
como o valor. Aqui está um exemplo:
"""

menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print(menu['Chicken Alfredo'])

# Your code here: Add some dish-price pairs to menu!
menu['Hamburger'] = 8.50
menu['Pizza Slice'] = 3.50
menu['Salad'] = 10.00

print("There are " + str(len(menu)) + " items on the menu.")
print(menu) # imprimirá o dicionário