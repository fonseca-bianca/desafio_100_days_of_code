"""
Difinir função com argumento booleano
"""

delivery = True

def deliver(delivery):
    if delivery == True:
        print(input("Enter your address: "), delivery)
        
deliver(delivery)