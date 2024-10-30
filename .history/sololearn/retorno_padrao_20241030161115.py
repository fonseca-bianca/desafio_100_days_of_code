"""
Python permite que os argumentos da função tenham valores padrão. 
Se a função é chamada sem o argumento, o argumento recebe seu valor padrão.
"""


def greet(name = "Michael"):
    print("Welcome", name)
    
greet()
greet("John Oliver")

# Welcome Michael
# Welcome John Oliver