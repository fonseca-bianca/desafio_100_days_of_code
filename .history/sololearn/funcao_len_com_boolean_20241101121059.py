"""
Defina uma função pra retornar True se a contagem de itens do argumento da lista
for MAIOR que 5 e False caso não seja
"""

def check_count(itens):
    if len(itens) > 5:
        return True
    else:
        return False

check_count()
print(check_count)