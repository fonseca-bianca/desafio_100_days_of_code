def imc(weight, height):
    index = weight / (height * height)
    print(f"O IMC é {index:.2f}") 

imc(52, 1.52) # função chamada fora do escopo dela com os argumentos declarados