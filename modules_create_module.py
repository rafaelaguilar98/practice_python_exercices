# We can create a module with functions and can use it in different programs with the keyword "import"

def verificarSiEsPrimo(numero_a_revisar):
    for x in range(2, numero_a_revisar):
        if (numero_a_revisar%x == 0):
            return False
    return True
