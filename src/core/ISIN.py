def detectar_ISIN(codigo: str, mensaje: bool = True):
    letra_en_numeros = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24,
                        'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35}
    numeros = []
    digitos = []

    if len(codigo) != 12:
        return codigo + ' no tiene exactamente 12 caracteres' if mensaje else False

    if not codigo[:2].isalpha():
        return codigo + ' los primeros dos caracteres no son letras' if mensaje else False

    if not codigo[2:11].isdigit():
        return codigo + ' los siguientes 9 caracteres no son digitos' if mensaje else False

    for c in codigo[:12]:
        if c.isalpha():
          numero_letra = letra_en_numeros[c.upper()]

          digitos = []

          while numero_letra > 0:
              digit = numero_letra % 10
              digitos.append(digit)
              numero_letra //= 10
          numeros.extend(reversed(digitos))
        else:
         numeros.append(c)
    for i in range(0, 14, 2):
        numeros[i] = str(int(numeros[i]) * 2)

        if len(numeros[i]) == 2:
            numeros[i] = str(sum(int(digito) for digito in numeros[i]))

    lista_num = [int(x) for x in numeros]

    numeros=sum(lista_num)

    response = codigo + ' Es un código ISIN con dígito de control: ' + str(lista_num[13]) if numeros % 10 == 0 else 'No es un código ISIN válido'

    return response if mensaje else numeros % 10 == 0
    

def ISIN_search_control(codigo):
    letra_en_numeros = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24,
                        'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35}
    numeros = []
    digitos = []


    if not codigo[:2].isalpha():
        return codigo + ' los primeros dos caracteres no son letras'
    if  len(codigo) !=11 :
        return codigo + ' Ya tiene un digito de control'


    for c in codigo[:11]:
        if c.isalpha():
          numero_letra = letra_en_numeros[c]

          digitos = []

          while numero_letra > 0:
              digit = numero_letra % 10
              digitos.append(digit)
              numero_letra //= 10
          numeros.extend(reversed(digitos))
        else:
         numeros.append(c)
    for i in range(0, 14, 2):
          numeros[i] = str(int(numeros[i]) * 2)

          if len(numeros[i]) == 2:
              numeros[i] = str(sum(int(digito) for digito in numeros[i]))

    lista_num = [int(x) for x in numeros]

    numeros=sum(lista_num)

    n=0
    if numeros % 10 == 0:
      print(codigo+"x",'Es un código ISIN con dígito de control: ',0)
      return 0
    else:
      while numeros %10 != 0:
        n+=1
        numeros=numeros+1

      print(codigo+"x",'Es un código ISIN con dígito de control:', n)
      return n
    

def ISIN_search_x(codigo: str, mensaje: bool = True):
    letra_en_numeros = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24,
                        'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35}
    numeros = []
    digitos = []
    x = codigo.find('x') # posision de la x en el codigo

    if x == -1:
      return codigo + ' no tiene una x' if mensaje else -1
    if len(codigo) != 12:
        return codigo + ' no tiene exactamente 12 digitos' if mensaje else -1
    if not codigo[:2].isalpha():
        return codigo + ' los primeros dos caracteres no son letras' if mensaje else -1
    if not codigo[2:11].isdigit() and x == -1:
        return codigo + ' los 12 caracteres no son digitos' if mensaje else -1
    if not codigo[2:x-1].isdigit() or (not codigo[x+1:12].isdigit() and x != len(codigo)-1):
        return codigo + ' los 12 caracteres no son digitos' if mensaje else -1

    for c in codigo[:12]:
        if c.isalpha() and c != 'x':
          numero_letra = letra_en_numeros[c.upper()]

          digitos = []

          while numero_letra > 0:
              digit = numero_letra % 10
              digitos.append(digit)
              numero_letra //= 10
          numeros.extend(reversed(digitos))
        else:
            numeros.append(c)

    x = numeros.index('x')
    for i in range(0, 14, 2): # multiplica los numeros en pos impares
        if i != x:
            numeros[i] = str(int(numeros[i]) * 2)

            if len(numeros[i]) == 2:
                numeros[i] = str(sum(int(digito) for digito in numeros[i]))

    lista_num = [int(x) for x in numeros if x != 'x']
    numeros=sum(lista_num)

    response: str = 'ciclo'
    if x % 2 != 0: # si la x esta en una posicion par (teoria)
        for i in range(0, 10):
            if (i + numeros) % 10 == 0:
                response = codigo + ' Es un código ISIN con X: ' + str(i) if mensaje else str(i)
                break
    elif x % 2 == 0: # si la x esta en una posicion impar (teoria)
        for i in range(0, 10):
            numero = f"{2*i}"
            if len(numero) == 2:
                numero = str(sum(int(digito) for digito in numero))
            
            if (int(numero) + numeros) % 10 == 0:
                response = codigo + f' Es un código ISIN con X: {i}' if mensaje else str(i)
                break

    return response if mensaje else int(response)