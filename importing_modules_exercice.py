# We can import modules defined in python use the keyword "import" and the name of the module
import random as r #We can use a letter or "identificator" to use our modules through our program more easy

def ejemploDeFuncion():
    print(r.randrange(1,10)) #random number between 1 and 10

#main function
if __name__ == "__main__":
    ejemploDeFuncion()