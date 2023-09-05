"Ingreso al programa"
print('Hola, bienvenido al programa para transformar tus números enteros del sistema decimal a binarios')

"Función de transformación"

"""La función transform_bin --> Se define como un conjunto de condicionales donde se hace la transformación 
de el número entero ingresado"""
def transform_bin(number): # Llamado de la función
    if number > 0: # Ingreso al proceso, solo ingresará si el número es entero mayor a 0
        binario = []  # Iniciando Lista Binario, en esta lista se organizarán los restos obtenidos
        while number >= 1:  # Ciclo de calculo, en este caso se empleará la misma variable number 
            # Mientras number sea mayor o igual 1 entonces proseguir con la secuencia de comandos
            if number % 2 == 0: # Este condicional define que para el modulo o resto de la división que se define con %, es igual a 0 
                # entonces agregar un 0, a la lista binario
                binario.append(0)
                number //= 2 # Y seguirá haciendo la división entera mientras ese sea el resultado de la operación 
            elif number % 2 != 0: # En otro caso donde el modulo sea distinto de 0, entonces se sigue haciendo la división
                number //= 2
                binario.append(1) # Y se agrega un 1 a lista de binario
        return binario[::-1] # Respuesta binario, acá se da la respuesta de la función. El -1 es para hacer el recorrido o slicing de la lista al revés 
    else:
        print('Tu número no es válido')
        return None  # Respuesta de número  no valido, en caso de que el valor que se ingrese sea menor a 0 
    
"Corrida del Código"
def run():
    number = int(input('Ingrese un número entero positivo: '))
    binario = transform_bin(number)

    if binario is not None:
        print(f'{binario} es el número binario de {number}')

if __name__ == '__main__':
    run()