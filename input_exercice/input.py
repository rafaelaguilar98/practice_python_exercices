#First exaple about how to use the input function. The next function ask name and age
def input_example():
    name = input("Dime tu nombre: ")
    edad = input("Dame tu edad: ")
    print('''Bienvenido:  {}  
    ya se que tienes: {} años :)'''.format(name, edad))
if __name__ == "__main__":
    input_example()
