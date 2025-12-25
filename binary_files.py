#We can copy binary files (not text files) in this example we'll copy an image into a new image file
def binaryFiles():
    try:
        input_file  = open('myimage.jpg', 'rb') #rb for binary files
        output_file = open('myoutputimage.jpg','wb')
        msg = input_file.read()
        while len(msg):
            output_file.write(msg)
            msg = input_file.read()
        input_file.close()
        output_file.close()
    except Exception as e:
        print("Error al crear el archivo: ",e)

#main function
if __name__ == "__main__":
    binaryFiles()