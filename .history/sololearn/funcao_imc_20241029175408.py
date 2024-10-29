def imc(weight, height):
    index = weight / (height * height)
    print("O IMC é", round(index, 2))

imc(52, 1.52)