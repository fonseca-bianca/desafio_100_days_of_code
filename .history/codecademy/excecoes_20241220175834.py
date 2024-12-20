"""
Erros em Python podem ser amplamente categorizados em dois tipos: bugs e 
exceções.
Bugs são falhas ou erros no código de um programa, levando a comportamentos 
incorretos ou não intencionados. Isso não necessariamente impede o programa 
de ser executado até o final, mas pode resultar em saídas ou comportamentos 
errados.
"""

name = "Mery"
surname = "Osborn"
print(name + surname)
#output: MeryOsborn

print("----------------------------------------------------------------")

# cód com erro:
# data = ["anna", "bob", "mery"]
# names = [x for x.upper() in data]

# cód corrigido:
data = ["anna", "bob", "mery"]
names = [x.upper() for x in data]
print(names)

"""
O que entendi:
x.upper() vem antes do loop for porque toda vez que há a iteração (x in data)
o programa coloca as letras da palavra em MAIÚSCULO
"""