"""
Criar uma lista de 1 a 50 e percorrer todos os valores do início até o final.
"""

numbers = []

for number in range(1,51): # inclui o valor inicial (1) e vai até um número antes do final (50)
    numbers.append(number)
    
print(numbers) # output: serão inseridos os números de 1 a 50 na lista vazia


""" 
LIST COMPREHENSION (atalho):
variável = [expressao for item in iterável]

Código acima reescrito em uma única linha:

numbers = [number for number in range(1,51)]
    
print(numbers)

numbers → <variavel>: armazenará a NOVA lista criada
number (antes de for) → <expressao>: realizada em CADA item. O próprio item é usado
number (depois de for) → <item>: item atual é processado
range(1, 51) → <iteravel>: qlqr objeto iterável (intervalos, listas, strings, tuplas, sets)
"""