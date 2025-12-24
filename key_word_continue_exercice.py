#The keyword "continue" like it says continue with the iteration in the loop
def ejemplo_1():
    j = 0
    for i in range(5):
        j+=2
        print('\ni = ', i, ', j =', j)
        if j == 6:
            continue 
        print("No se imprime si j = 6")
#main function
if __name__ == "__main__":
    ejemplo_1()