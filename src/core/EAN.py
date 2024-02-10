def detectar_EAN_13(codigo):
  numeros = []
  digitos = []
  if len(codigo) != 13:
      return codigo + ' no tiene exactamente 13 digitos no es un codigo EAN-13'
  if not codigo[0:12].isdigit():
      return codigo + ' los  13 caracteres no son digitos'
  for c in codigo[:13]:
    numeros.append(c)
  for i in range(1, 12, 2):
    numeros[i] = str(int(numeros[i]) * 3)

  lista_num=lista_int = [int(x) for x in numeros]

  numeros=sum(lista_num)
  if numeros % 10 == 0:
      print(codigo,'Es un código EAN-13 con dígito de control: ' + str(lista_num[12]))
  else:
      print(codigo,'No es un código EAN-13 válido')

def encontrar_d_c_EAN_13(codigo):
  numeros = []
  digitos = []
  if len(codigo) != 12:
      return codigo + ' no tiene exactamente 12 digitos no debe tener digito de control'
  if not codigo[0:11].isdigit():
      return codigo + ' los 12 caracteres no son digitos'
  for c in codigo[:12]:
    numeros.append(c)

  for i in range(1, 12, 2):
    numeros[i] = str(int(numeros[i]) * 3)

  lista_num=lista_int = [int(x) for x in numeros]

  numeros=sum(lista_num)
  n=0
  if numeros % 10 == 0:
    print(codigo+"x",'Es un código EAN-13 con dígito de control: ',0)
  else:
    while numeros %10 != 0:
      n+=1
      numeros=numeros+1
  print(codigo+"x",'Es un código EAN-13 con dígito de control:', n)

def detectar_EAN_8(codigo):
  numeros = []
  digitos = []
  if len(codigo) != 8:
      return codigo + ' no tiene exactamente 8 digitos no es un codigo EAN-8'
  if not codigo[0:7].isdigit():
      return codigo + ' los  7 caracteres no son digitos'
  for c in codigo[:8]:
    numeros.append(c)

  for i in range(1, 7, 2):
    numeros[i] = str(int(numeros[i]) * 3)

  lista_num=lista_int = [int(x) for x in numeros]

  numeros=sum(lista_num)
  if numeros % 10 == 0:
      print(codigo,'Es un código EAN-8 con dígito de control: ' + str(lista_num[7]))
  else:
      print(codigo,'No es un código EAN-8 válido')
     
def encontrar_d_c_EAN_8(codigo):
  numeros = []
  digitos = []
  if len(codigo) != 7:
      return codigo + ' no tiene exactamente 7 digitos no es un codigo EAN-8 o ya tiene digito de control'
  if not codigo[0:6].isdigit():
      return codigo + ' los  6 caracteres no son digitos'
  for c in codigo[:8]:
    numeros.append(c)

  for i in range(1, 6, 2):
    numeros[i] = str(int(numeros[i]) * 3)

  lista_num=lista_int = [int(x) for x in numeros]

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