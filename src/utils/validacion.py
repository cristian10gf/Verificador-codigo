def validar(codigo: str,cantidad:int, mensaje: bool = False):
  if len(codigo) != cantidad and mensaje:
      return codigo + f' no tiene exactamente {cantidad} digitos'
  if not codigo[0:cantidad-1].isdigit() and mensaje:
      return codigo + f' los  {cantidad} caracteres no son digitos'

  if len(codigo) != cantidad and not mensaje:
      return False
  if not codigo[0:cantidad-1].isdigit() and not mensaje:
      return False
  
  return True