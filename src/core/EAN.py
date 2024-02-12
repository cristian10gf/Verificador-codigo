def detectar_EAN_13(codigo: str, mensaje: bool = True):
  numeros = []

  if len(codigo) != 13:
      return codigo + ' no tiene exactamente 13 digitos no es un codigo EAN-13' if mensaje else False
  
  if not codigo[0:12].isdigit():
      return codigo + ' los  13 caracteres no son digitos' if mensaje else False

  for c in codigo[:13]:
    numeros.append(c)

  for i in range(1, 12, 2):
    numeros[i] = str(int(numeros[i]) * 3)

  lista_num= [int(x) for x in numeros]
  numeros=sum(lista_num)

  response = codigo + 'Es un código EAN-13 con dígito de control: ' + str(lista_num[12]) if numeros % 10 == 0 else 'No es un código EAN-13 válido'
  
  return response if mensaje else numeros % 10 == 0

def encontrar_d_c_EAN_13(codigo: str, mensaje: bool = True):
  numeros = []

  if len(codigo) != 12:
      return codigo + ' no tiene exactamente 12 digitos no debe tener digito de control' if mensaje else False

  if not codigo[0:11].isdigit():
      return codigo + ' los 12 caracteres no son digitos' if mensaje else False
  
  for c in codigo[:12]:
    numeros.append(c)

  for i in range(1, 12, 2):
    numeros[i] = str(int(numeros[i]) * 3)

  lista_num= [int(x) for x in numeros]

  numeros=sum(lista_num)
  n=0
  if numeros % 10 == 0:
    print(codigo+"x",'Es un código EAN-13 con dígito de control: ',0)
  else:
    while numeros %10 != 0:
      n+=1
      numeros=numeros+1
  print(codigo+"x",'Es un código EAN-13 con dígito de control:', n)

def encontrar_x_EAN_13(codigo: str, mensaje: bool = True):
  numeros = []
  x = codigo.find('x') # posision de la x en el codigo

  if x == -1:
    return codigo + ' no tiene una x' if mensaje else -1

  if len(codigo) != 13:
      return codigo + ' no tiene exactamente 13 digitos' if mensaje else -1

  if not codigo[0:12].isdigit() and x == -1:
      return codigo + ' los 12 caracteres no son digitos' if mensaje else -1

  if not codigo[:x-1].isdigit() or ((not codigo[x+1:13].isdigit()) and x != len(codigo)-1):
      return codigo + ' los 12 caracteres no son digitos' if mensaje else -1
  
  for c in codigo[:13]:
    numeros.append(c)

  for i in range(1, 12, 2): # multiplica los numeros en pos par
    if i != x:
      numeros[i] = str(int(numeros[i]) * 3)

  lista_num= [int(x) for x in numeros if x != 'x']
  numeros=sum(lista_num)

  response: str = 'ciclo'
  
  if x % 2 != 0: # si la x esta en una posicion par (teoria)
    for i in range(0, 10):
      if (3*i + numeros) % 10 == 0:
        response = codigo + ' Es un código EAN-13 con X: ' + str(i) if mensaje else str(i)
        break
  elif x % 2 == 0: # si la x esta en una posicion impar (teoria)
    for i in range(0, 10):
      if (i + numeros) % 10 == 0:
        response = codigo + f' Es un código EAN-13 con X: {i}' if mensaje else str(i)
        break

  return response if mensaje else int(response)


def detectar_EAN_8(codigo: str, mensaje: bool = True):
  numeros = []

  if len(codigo) != 8:
      return codigo + ' no tiene exactamente 8 digitos no es un codigo EAN-8' if mensaje else False
  
  if not codigo[0:7].isdigit():
      return codigo + ' los  7 caracteres no son digitos' if mensaje else False

  for c in codigo[:8]:
    numeros.append(c)

  for i in range(1, 7, 2):
    numeros[i] = str(int(numeros[i]) * 3)

  lista_num = [int(x) for x in numeros]
  numeros = sum(lista_num)

  response = codigo + ' Es un código EAN-8 con dígito de control: ' + str(lista_num[7]) if numeros % 10 == 0 else ' No es un código EAN-8 válido'

  return response if mensaje else numeros % 10 == 0
     
def encontrar_d_c_EAN_8(codigo: str, mensaje: bool = True):
  numeros = []
  
  if len(codigo) != 7:
      return codigo + ' no tiene exactamente 7 digitos no es un codigo EAN-8 o ya tiene digito de control' if mensaje else False
  if not codigo[0:6].isdigit():
      return codigo + ' los  6 caracteres no son digitos' if mensaje else False
  for c in codigo[:8]:
    numeros.append(c)

  for i in range(1, 6, 2):
    numeros[i] = str(int(numeros[i]) * 3)

  lista_num = [int(x) for x in numeros]

  numeros=sum(lista_num)
  n=0
  codigo=str(codigo)
  if numeros % 10 == 0:
    print(f"{codigo}x Es un código EAN-8 con dígito de control: 0")
  else:
    while numeros %10 != 0:
      n+=1
      numeros=numeros+1
    print(f"{codigo}x Es un código EAN-8 con dígito de control: {n}")

def encontrar_x_EAN_8(codigo: str, mensaje: bool = True):
  numeros = []
  x = codigo.find('x') # posision de la x en el codigo

  if x == -1:
    return codigo + ' no tiene una x' if mensaje else -1

  if len(codigo) != 8:
      return codigo + ' no tiene exactamente 8 digitos' if mensaje else -1

  if not codigo[0:6].isdigit() and x == -1:
      return codigo + ' los 6 caracteres no son digitos' if mensaje else -1

  if not codigo[:x-1].isdigit() or not codigo[x+1:8].isdigit():
      return codigo + ' los 6 caracteres no son digitos' if mensaje else -1
  
  for c in codigo[:7]:
    numeros.append(c)

  for i in range(1, 6, 2):
    if i != x:
      numeros[i] = str(int(numeros[i]) * 3)

  lista_num= [int(x) for x in numeros if x != 'x']
  numeros=sum(lista_num)

  response: str = ''
  if x % 2 != 0: # si la x esta en una posicion par (teoria)
    for i in range(0, 9):
      if (3*i + numeros) % 10 == 0:
        response = codigo + ' Es un código EAN-8 con X: ' + str(i) if mensaje else str(i)
        break
  elif x % 2 == 0: # si la x esta en una posicion impar (teoria)
    for i in range(0, 9):
      if (i + numeros) % 10 == 0:
        response = codigo + f' Es un código EAN-8 con X: {i}' if mensaje else str(i)
        break

  return response if mensaje else int(response)