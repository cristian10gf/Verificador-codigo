from core.EAN import detectar_EAN_13, detectar_EAN_8
from core.ISBN import detectar_ISBN_10, detectar_ISBN_13
from core.ISIN import ISIN

def revisar_codigo(codigo: str):
  # revisa cual es el tipo de codigo
  if detectar_EAN_13(codigo):
    return 'EAN-13'
  elif detectar_EAN_8(codigo):
    return 'EAN-8'
  elif detectar_ISBN_10(codigo):
    return 'ISBN-10'
  elif detectar_ISBN_13(codigo):
    return 'ISBN-13'
  elif ISIN(codigo, mensaje=False):
    return 'ISIN'
  else:
    return 'No se reconoce el código'