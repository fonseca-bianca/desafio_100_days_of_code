"""
Função retornando múltiplos valores:
Função rect() recebe duas dimensões como argumento
ex.:
A função rect() ajuda uma agência imobiliária a calcular a área e o perímetro 
de um terreno retangular. Ela recebe as duas dimensões do terreno como argumentos.
"""

def rect(length, width):
    area = length * width
    perimeter = 2 * length + 2 * width
    return area, perimeter

x, y = rect(50, 100)
print(f'The value of area is {x} and the value of perimeter is {y}')