import os
f = open('archivo_leer.txt', 'r') #Open the file un read mode

#Read the file line by line
def leerLineaPorLinea():
    primera_linea = f.readline()
    segunda_linea = f.readline()
    print(primera_linea)
    print(segunda_linea)
    f.close()

#Read the line with a loop
def leerArchivoConCiclo():
    for line in f:
        print(line, end='')
    f.close()

#Write in a file
def escribirEnArchivo():
    f = open('archivo_leer.txt', 'a') #Open the file in "append" mode
    f.write('\n Se agrega esta linea al archivo')
    f.write('\n Y también se agrega este archivo')
    f.close()

#Specify the buffer size in when you write in a file
def abrirYLeerArchivosBuffer():
    input_file  = open('archivo_entrada.txt', 'r')
    output_file = open('archivo_salida.txt','w')
    msg = input_file.read(10)
    while len(msg):
        output_file.write(msg +'\n')
        msg = input_file.read()
    input_file.close()
    output_file.close()

#Deleting and rename files
def eliminarArchivo():
    os.remove("archivo_entrada.txt")

#Rename file
def renombrarArchivo():
    os.rename('archivo_salida.txt', 'archivo_resultado.txt')

#main function
if __name__ == "__main__":
    renombrarArchivo()