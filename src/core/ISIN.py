def ISIN(codigo: str, mensaje: bool = True):
    letra_en_numeros = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24,
                        'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35}
    numeros = []
    digitos = []

    if len(codigo) != 12:
        return codigo + ' no tiene exactamente 12 caracteres'

    if not codigo[:2].isalpha():
        return codigo + ' los primeros dos caracteres no son letras'

    if not codigo[2:11].isdigit():
        return codigo + ' los siguientes 9 caracteres no son digitos'

    for c in codigo[:12]:
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

    lista_num=lista_int = [int(x) for x in numeros]

    numeros=sum(lista_num)

    response = ''
    if numeros % 10 == 0:
        response =  'Es un código ISIN con dígito de control: ' + str(lista_num[13])
    else:
        response = 'No es un código ISIN válido'

    if mensaje:
        return response
    else:
        return numeros % 10 == 0
    
    
    
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

    lista_num=lista_int = [int(x) for x in numeros]

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