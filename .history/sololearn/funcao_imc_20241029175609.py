def imc(weight, height):
    index = weight / (height * height)
    print(f"O IMC é {index:.2f}") 

imc(52, 1.52) # função chamada por fora com os argumentos declarados