"""
Defina uma função pra retornar True se a contagem de itens do argumento da lista
for MAIOR que 5 e False caso não seja
"""

itens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def check_count(itens):
    if len(itens) > 5:
        return True
    else:
        return False

check_count(itens)
# print(check_count(itens))