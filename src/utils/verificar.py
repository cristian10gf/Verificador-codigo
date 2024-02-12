from core.EAN import *
from core.ISBN import *
from core.ISIN import *

def revisar_codigo(codigo):
  if (not codigo.isdigit()):
    return 'No es un código valido'
  if detectar_EAN_13(codigo, False):
    return 'EAN-13'
  elif detectar_EAN_8(codigo, False):
    return 'EAN-8'
  elif detectar_ISBN_10(codigo, False):
    return 'ISBN-10'
  elif detectar_ISBN_13(codigo, False):
    return 'ISBN-13'
  elif detectar_ISIN(codigo,False):
    return 'ISIN'
  else:
    return 'No se reconoce el código'
  
def consultar_codigo(codigo, tipo):
  # revisa cual es el tipo de codigo
  if tipo == 'EAN-13':
    return detectar_EAN_13(codigo)
  elif tipo == 'EAN-8':
    return detectar_EAN_8(codigo)
  elif tipo == 'ISBN-10':
    return detectar_ISBN_10(codigo)
  elif tipo == 'ISBN-13':
    return detectar_ISBN_13(codigo)
  elif tipo == 'ISIN':
    return detectar_ISIN(codigo)
  else:
    return 'No se reconoce el código'
  
def encontrar_codigo(codigo, tipo):
  # revisa cual es el tipo de codigo
  if tipo == 'ISBN-10':
    return detectar_ISBN_10(codigo)
  elif tipo == 'ISBN-13':
    return detectar_ISBN_13(codigo)
  else:
    return 'No se reconoce el código'
  

def encontrar_x(codigo):
  if encontrar_ISBN_10(codigo, False) != -1:
    return encontrar_ISBN_10(codigo)
  elif encontrar_ISBN_13(codigo, False) != -1:
    return encontrar_ISBN_13(codigo)
  elif encontrar_x_EAN_13(codigo, False) != -1:
    return encontrar_x_EAN_13(codigo)
  elif encontrar_x_EAN_8(codigo, False) != -1:
    return encontrar_x_EAN_8(codigo)
  elif ISIN_search_x(codigo, False) != -1:
    return ISIN_search_x(codigo)
  else:
    return 'No se reconoce el código'