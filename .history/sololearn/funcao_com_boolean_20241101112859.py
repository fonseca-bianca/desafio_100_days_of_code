"""
Difinir função com argumento booleano
"""

delivery = True
address = input()

def deliver(delivery):
    if delivery == True:
        print(f"Enter your address: {address}")
        
deliver(delivery)
