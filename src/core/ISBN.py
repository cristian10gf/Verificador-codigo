def detectar_ISBN_10(codigo):
  numeros = []
  digitos = []

  if len(codigo) != 10:
      return codigo + ' no tiene exactamente 10 caracteres'

  if not codigo[0:9].isdigit():
      return codigo + ' los 10 caracteres no son digitos'
  for c in codigo[:10]:
    numeros.append(c)

  lista_num= [int(x) for x in numeros]

  for j in range(0,10):
    lista_num[j]=(10-j)*lista_num[j]

  numeros=sum(lista_num)


  if numeros % 11 == 0:
      return codigo,'Es un código ISBN-10 con dígito de control: ' + str(lista_num[9])
  else:
      return codigo,'No es un código ISBN-10 válido'
  
def encontrar_ISBN_10(codigo):
  numeros = []
  digitos = []

  if len(codigo) != 9:
      return codigo + ' no tiene exactamente 9 caracteres o ya tiene digito de control'

  if not codigo[0:8].isdigit():
      return codigo + ' los 9 caracteres no son digitos'
  for c in codigo[:9]:
    numeros.append(c)

  lista_num= [int(x) for x in numeros]

  for j in range(0,9):
    lista_num[j]=(10-j)*lista_num[j]

  numeros=sum(lista_num)


  if numeros % 11 == 0:
      return codigo,'Es un código ISBN-10 con dígito de control: ' + str(0)
  else:
      residuo=numeros%11
      return codigo,'Es un código ISBN-10 con dígito de control: ' + str(residuo)
  
def detectar_ISBN_13(codigo):
    numeros = []
    digitos = []
    inicio = "978"

    if len(codigo) != 13:
        return codigo + ' no tiene exactamente 13 caracteres'
    if not codigo[0:12].isdigit():
        return codigo + ' los 13 caracteres no son digitos'
    if codigo[0:2] != inicio:
        return codigo + ' no tiene la identificacion de codigo ISBN-13'

    for c in codigo[3:12]:
        numeros.append(c)

    lista_num= [int(x) for x in numeros]

    for j in range(0,12):
        lista_num[j]=(10-j)*lista_num[j]

    numeros=sum(lista_num)


    if numeros % 13 == 0:
        return codigo,'Es un código ISBN-13 con dígito de control: ' + str(lista_num[12])
    else:
        return codigo,'No es un código ISBN-13 válido'
    
def encontrar_ISBN_13(codigo):
    numeros = []
    digitos = []
    inicio = "978"

    if len(codigo) != 12:
        return codigo + ' no tiene exactamente 12 caracteres o ya tiene digito de control'
    if not codigo[0:11].isdigit():
        return codigo + ' los 12 caracteres no son digitos'
    if codigo[0:2] != inicio:
        return codigo + ' no tiene la identificacion de codigo ISBN-13'

    for c in codigo[3:11]:
        numeros.append(c)

    lista_num= [int(x) for x in numeros]

    for j in range(0,12):
        lista_num[j]=(10-j)*lista_num[j]

    numeros=sum(lista_num)


    if numeros % 13 == 0:
        return codigo,'Es un código ISBN-13 con dígito de control: ' + str(0)
    else:
        residuo=numeros%13
        return codigo,'Es un código ISBN-13 con dígito de control: ' + str(residuo)