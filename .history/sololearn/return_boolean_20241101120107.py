score = 65

def is_pass(score):
    if score >= 70:
        return True

print(is_pass())

# esse função retorna None porque o score é MENOR do que 70 e para valores abaixo
# de 70, NÃO há instrução de retorno.
# Nesse caso, como Python NÃO encontra instrução de retorno, ele retorna None por padrão