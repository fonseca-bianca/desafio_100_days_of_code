"""
Exceção 'ValueError' é levantada quando uma função recebe um valor do tipo 
correto, mas o próprio valor é inapropriado ou inaceitável.
A função int() pode ser chamada em string, MAS somente quando TODOS os caracteres
forem valores numéricos.
"""

data = "1903"
num_data = int(data)
print(num_data)