"""
Exceção 'TypeError' só pode ocorrer quando uma função é chamada em um valor 
de tipo INADEQUADO.
A função len() só pode ser chamada em iteráveis (string, listas, etc)
"""

message = "Hello"
lenght = len(message)
print(message)
#output: Hello