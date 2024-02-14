def detectar_ISBN_10(codigo: str, mensaje: bool = True):
  numeros = []

  if len(codigo) != 10:
      return codigo + ' no tiene exactamente 10 caracteres' if mensaje else False
  if not codigo[0:9].isdigit():
      return codigo + ' los 10 caracteres no son digitos' if mensaje else False
  
  for c in codigo[:10]:
    numeros.append(c)

  lista_num= [int(x) for x in numeros]

  for j in range(0,10):
    lista_num[j]=(10-j)*lista_num[j]

  numeros=sum(lista_num)

  response = codigo + 'Es un código ISBN-10 con dígito de control: ' + str(lista_num[9]) if numeros % 11 == 0 else 'No es un código ISBN-10 válido'
  return response if mensaje else numeros % 11 == 0
  
def encontrar_ISBN_10(codigo: str, mensaje: bool = True):
  numeros = []
  x = codigo.find('x') # posision de la x en el codigo

  if x == -1:
      return codigo + ' no tiene x a buscar' if mensaje else -1
  
  validacion = codigo.split('x')
  if len(codigo) != 10:
      return codigo + ' no tiene exactamente 9 caracteres o ya tiene digito de control' if mensaje else -1
  if (not validacion[0].isdigit() and validacion[0] != "") or (not validacion[1].isdigit() and validacion[1] != ''):
      return codigo + ' los 9 caracteres no son digitos' if mensaje else -1

  for c in codigo[:9]:
    numeros.append(c)

  lista_num= [int(x) for x in numeros if x != 'x']

  for j in range(0,x):
    lista_num[j]=(10-j)*lista_num[j]
  for j in range(x,8):
    lista_num[j]=(10-j)*lista_num[j]

  numeros=sum(lista_num)

  for i in range(0,10):
    if (numeros+(10-x)*i) % 11 == 0:
        return codigo + ' Es un código ISBN-10 con X: ' + str(i) if mensaje else i
  



def detectar_ISBN_13(codigo: str, mensaje: bool = True):
    numeros = []
    inicio = "978"

    if len(codigo) != 13:
        return codigo + ' no tiene exactamente 13 caracteres' if mensaje else False
    if not codigo[0:12].isdigit():
        return codigo + ' los 13 caracteres no son digitos' if mensaje else False
    if codigo[0:3] != inicio:
        return codigo + ' no tiene la identificacion de codigo ISBN-13' if mensaje else False

    for c in codigo[:12]:
        numeros.append(c)

    lista_num= [int(x) for x in numeros]

    for j in range(0,9):
        lista_num[j]=(10-j)*lista_num[j]

    numeros=sum(lista_num)

    response = codigo + 'Es un código ISBN-13 con dígito de control: ' + str(lista_num[-1]) if numeros % 11 == 0 else 'No es un código ISBN-13 válido'
    return response if mensaje else numeros % 11 == 0
    
def encontrar_ISBN_13(codigo: str, mensaje: bool = True):
    numeros = []
    inicio = "978"
    x = codigo.find('x') # posision de la x en el codigo

    if x == -1:
        return codigo + ' no tiene x a buscar' if mensaje else -1
    
    validacion = codigo.split('x')

    if len(codigo) != 13:
        return codigo + ' no tiene exactamente 12 caracteres o ya tiene digito de control' if mensaje else -1
    if codigo[0:3] != inicio:
        return codigo + ' no tiene la identificacion de codigo ISBN-13' if mensaje else -1
    if (not validacion[0].isdigit() and validacion[0] != "") or (not validacion[1].isdigit() and validacion[1] != ''):
        return codigo + ' los 12 caracteres no son digitos' if mensaje else -1

    for c in codigo[:12]:
        numeros.append(c)

    lista_num= [int(x) for x in numeros if x != 'x']

    x -= 3
    for j in range(0,x):
        lista_num[j]=(10-j)*lista_num[j]
    for j in range(x,8):
        lista_num[j]=(10-j)*lista_num[j]

    numeros=sum(lista_num)

    for i in range(0,10):
        if (numeros+(10-x)*i) % 11 == 0:
            return codigo + ' Es un código ISBN-13 con X: ' + str(i) if mensaje else i
