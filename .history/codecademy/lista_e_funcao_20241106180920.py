"""
Funções podem levar listas como entradas e executar várias operações nessas 
listas.
1. Escreva uma função que conte quantas vezes a string "fizz"aparece em uma 
lista.
Escreva uma função chamada fizz_count que recebe uma lista "x" como entrada.
Crie uma variável count para manter a contagem em andamento. Inicialize-a 
com zero.
Um for pra cada um item em x, se esse item é igual à string "fizz", então 
incremente count variável.
Após o loop, retorne count variável.
"""

# Write your function below!
def fizz_count(x):
    count = 0
    for item in x:
        if item == "fizz":
            count += 1
            return count

fizz_count()        
print(fizz_count)