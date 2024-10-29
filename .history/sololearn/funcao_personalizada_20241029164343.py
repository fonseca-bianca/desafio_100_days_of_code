"""
Função personalizada:
1º definir a função pra chamá-la no cód sempre que precisar (cód reutilizável)
"""

def greet():
    print("Hello from a function.")
    print("Have a nice day!")

greet()
# ao chamar a função sem parâmetros, é ela que faz os comandos print acima serem executados
# por estar SEM Argumentos (NÃO irá receber nenhuma entrada), ela irá executar o bloco de cód q está dentro dela


def say_hello():
    print("Hello, world!")  # Apenas imprime uma mensagem

# Variável fora da função
message = "This is a message outside the function."

# Chamando a função
say_hello()

# Imprimindo a variável fora da função
print(message)