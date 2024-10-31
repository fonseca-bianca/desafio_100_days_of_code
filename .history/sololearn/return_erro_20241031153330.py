"""
Todo o cód POSTERIOR dentro do mesmo bloco do 'return' será ignorado.
"""

def rect(d1, d2):
    area = 0
    return area
    area = d1 * d2
    
x = rect(50, 50)
print(x)



movies=["Avatar","Titanic","Alien"]
movies.append("Avengers")
movies.insert(2, "Terminator")
print(movies[3])