"""
Os blocos de código em um for loop podem ser tão grandes ou pequenos quanto 
necessário.
Durante o loop, você pode querer executar ações diferentes dependendo do item 
específico na lista.

1.Assim como no passo 2 acima, faça um loop em cada item da lista chamada a.
Como o passo 3 acima, se o número é par, print a variavel. 
"""

a_list_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for number in a_list_numbers:
    if number % 2 == 0: # vai imprimir só os números pares
        print(number)