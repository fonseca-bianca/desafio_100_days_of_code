"""
Incorporar uma condição em uma compreensão de lista, colocada após o iterável.
Por exemplo, o seguinte código filtra nomes que começam com B:
"""

users = ["Brandon","Emma", "Brian","Sophia", "Chloe", "Bella", "Benjamin"]
group_users = [user for user in users if user[0] == "B"] # strings que começam com "B"
print(group_users) # output: ['Brandon', 'Brian', 'Bella', 'Benjamin']

