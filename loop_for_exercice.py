#Define the array
mascotas = ['gato', 'perro', 'hamster', 'conejo']

#For loop to print the values in the array
def primer_ejemplo():
    for mis_mascotas in mascotas:
        print(mis_mascotas) # values in the array

#Print the array with index
def segundo_ejemplo():
    for index, mis_mascotas in enumerate(mascotas):
        print("El index: ",index, "Tiene el valor: ", mis_mascotas) #index and the value in the array

#Loop through a string
def tercer_ejemplo():
    palabra = 'hola'
    for i in palabra:
        print(i) #letter by letter

#sequence of numbers
def cuarto_ejemplo():
    for i in range(5):
        print(i) #0 to 4

#Range between two numbers
def quinto_ejemplo():
    for i in range(3,10):
        print(i) #3 to 9

def sexto_ejemplo():
    for i in range(4,10,2): #(first_number,last_number, step)
        print (i) #4,6,8 

#main function
if __name__ == "__main__":
    sexto_ejemplo()
