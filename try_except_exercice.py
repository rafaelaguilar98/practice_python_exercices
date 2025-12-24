# The try except controls the program when an error occurs.

def example_division_zero():
    try:
        resultado = 12/0
        print(resultado)
    except:
        print("Ocurrió un error")

def example_2():
    try:
        numero_1 = int(input("Por favor, ingresa un número: "))
        numero_2 = int(input("Por favor, ingresa otro número: "))
        respuesta = numero_1 / numero_2
        print("El resultado es: ", respuesta)
        archivo = open("missing.txt",'r')
    except ValueError:
        print("Error: no se ingresó un número")
    except ZeroDivisionError:
        print("Error: no se puede dividir entre 0")
    except Exception as e:
        print("Otro error: ",e)
#main function
if __name__ == "__main__":
    example_2()