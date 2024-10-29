def imc(weight, height):
    index = weight / (height * height)
    return index

patient_5 = imc(61, 1.83)
print(f"Underweight: ", patient_5 < 18.5)