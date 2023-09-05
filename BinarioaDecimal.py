"Ingreso al programa"
print('Hola, bienvenido al programa para transformar tus números binarios del sistema binario a decimal')

"Función de transformación"

"""La función transform_dec --> Se define como un conjunto de condicionales y bucles donde se hace la transformación 
de el número binario ingresado"""
def transform_dec(bin_str):
    dec = 0

    # Inversión del Binario 
    reversed_bin = bin_str[::-1] # El orden debe ser de izquierda a derecha, y comúnmente se lee de derecha a izquierda

    for i in range(len(reversed_bin)): # Para cada elemento en el iterable rango del tamaño del binario inverso
        digito = int(reversed_bin[i]) # Se van contando los elementos 1 a 1, en la variable digit
        dec += digito * (2 ** i) # Y para cada digit multimplicar por 2 y elevar a la i que es el indice de la matriz o de binario
        #  La variable dec es un contador que durante el ciclo for va sumando cada elemento elevado 
        

    return dec

def run():
    bin_input = input("Ingresa un número binario: ")

    # Evaluando entrada valida 
    if not all(bit in '01' for bit in bin_input):
        print("El número binario ingresado no es correcto")
        return

    dec_result = transform_dec(bin_input)
    print(bin_input + " como decimal es => " + str(dec_result))

if __name__ == '__main__':
    run()
