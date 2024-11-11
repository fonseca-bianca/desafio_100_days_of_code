"""
Você pode usar tuplas em qualquer estrutura de controle de fluxo, como 
declarações if-else e loops, assim como faria com listas.
"""

points = (12, 14, 9, 10, 9)
for point in points:
    if point > 10:
        print(point,": aprovado")