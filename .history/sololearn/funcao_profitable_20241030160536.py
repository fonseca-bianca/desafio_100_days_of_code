"""
Função profitable(): determina se algo é bom ou ruim, retornando True ou False
Ex.:
A função profitable() abaixo determina se a compra de um lote de terra é um bom
investimento para uma agência imobiliária em um local específico.
"""

def profitable(d1, d2):
    area = d1 * d2
    invest = area > 700
    return invest

buy = profitable(90, 120)
print(buy) # vai retornar True
