"""
Difinir função com argumento booleano
"""

delivery = True
address = input('Enter your address: ')

def deliver(delivery):
    if delivery == True:
        print(f"Your address is: {address}")
        
deliver(delivery)
