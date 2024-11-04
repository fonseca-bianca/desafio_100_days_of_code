"""
Função sorted(): recebe iterável como entrada.
Retorna uma lista com os itens ordenados
"""

ages = [10, 12, 5, 59, 89, 99, 9]

def sort_ages(ages):
    return sorted(ages)    

print(sort_ages(ages))
sort_ages(ages)

prices = [503.9, 199.9, 254.5, 39.9]
srt_prices = sorted(prices)
print(srt_prices[1])
