def imc(weight, height):
    index = weight / (height * height)
    return index

patient_1 = imc(61, 1.83)
print(f"Underweight Patient_1: {patient_1:.2f}", patient_1 < 18.5)

patient_2 = imc(75, 1.50)
print(f"Underweight Patient_2: {patient_2:.2f}", patient_2 < 18.5)
