"Programa que evalua la secuencia lógica para la admisión de una transferencia bancaria"

Banco_C=(input('ingrese su banco --> ')) # Recordar que el tipo de dato devuelto después de un print es None. 
Cuenta_C=(input('ingrese su número de cuenta--> '))
Saldo=(int(input('¿Cuál es su saldo? --> ')))
Banco_D=(input('ingrese banco destino --> '))
Cuenta_D=(input('ingrese cuenta destino -->'))
Hora=(int(input('ingrese hora actual (entre 0 y 24) -->')))
Cantidad_T=(int(input('ingrese monto a transferir -->'))) 

Bancos=["Mercantil","Bancolombia","Unicasa","Bancaamiga","Bogota"]
H1=list(range(9,13))
H2=list(range(15,21))
Hora_P=H1 + H2
validando=True

# Verificar si el banco está en la lista de bancos y si la longitud de la cuenta es de 10 digitos
if Banco_C in Bancos and len(Cuenta_C)==10:  
 print("Cuenta Valida")
else: 
 print('Banco no Valido')
 validando=False

# Verificar si el banco Cliente es igual al banco Destino
if Banco_C==Banco_D:
  Cantidad_T=Cantidad_T
if Banco_C!=Banco_D:
  Cantidad_T=Cantidad_T+100

# Verificar si el banco D está en la lista de bancos
if Banco_D in Bancos: 
   print('Banco Adeucado')
else: 
  validando=False

# Verificar si la hora está en la lista de horas permitidas
if Hora in Hora_P: 
  print("Horario Valido")
else:
  print('Fuera de Servicio')

# Verificar si el saldo es suficiente
if Saldo >= Cantidad_T:
  print('Saldo Suficiente')
else: 
  print('Saldo Insuficiente')
  validando=False

# Comprobar si todas las validaciones fueron exitosas
if validando:
    print('TRANSFERENCIA COMPLETADA')
else:
    print('Al menos una validación falló. Revise su solicitud.')
