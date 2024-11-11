"""
Listas são mutáveis, Tuplas não. Isso significa que você pode alterar seus
valores mesmo após terem sido criadas.
"""

colors = ["yellow", "blue", "purple"]
print("List colors: ")
print(colors)

# making change colors
colors[0] = "black"
colors.append("gray")
print("New list colors: ")
print(colors)