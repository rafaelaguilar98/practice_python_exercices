#Example about how to use the break in a condition or wherever we need it
def ejemplo_1():
    j = 0
    for i in range(5):
        j = j+2
        print('i = ', i, ', j = ', j)
        if j == 6: # if j = 6 the program stops
            break
#main function
if __name__ == "__main__":
    ejemplo_1()