"""
Tuplas são IMUTÁVEIS (assim como strings). Isso significa que você NÃO pode 
alterar seus valores mesmo após terem sido criadas.
"""

colors = ["yellow", "blue", "purple"]
print("List colors: ")
print(colors)

# making change colors
colors[0] = "black"
colors.append("gray")
print("New list colors: ")
print(colors)


# birth = (1981, "may", 12)
# birth[0] = 1982
# print(birth)