def imc(weight, height):
    index = weight / (height * height)
    return index

patient_5 = imc(61, 1.83)
print(f"Underweight: {patient_5:.2f}", patient_5 < 18.5)

patient_6 = imc(75, 1.50)
print(f"Underweight: {patient_6:.2f}", patient_5 < 18.5)
