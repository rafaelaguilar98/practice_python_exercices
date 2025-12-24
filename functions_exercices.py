#Functions in python starts by the keyword def and this functions can require some parameters (or not) to work

'''
    We can define global or local variables to use in our program. The local variables are declared inside of the function
    and the global variables outside of all the functions
'''

#Global variable (This variables can used in all of our functions)

global_variable = "Valor global"

#Defindig the function
def funcionSinParametros():
    print(global_variable) #print the global value.

def funcionConVariableLocal():
    global_variable = "Cambio el valor dentro de la funcion"
    print(global_variable) #The value of the global variable has been changed

def funcionConParametros(mensaje):
    print(mensaje) #Print the message from the varible "mensaje"

#Call the function in the "main" function
if __name__ == "__main__":
    mensaje_del_usuario = input("Ingrese el mensaje a imprimir: ")
    funcionConParametros(mensaje_del_usuario)