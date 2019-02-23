def keres_index(lista, elem):
  i = 0
  while i < len(lista):
    if lista[i] == elem:
      return i
    i = i + 1
  return -1


def benne_van_e(lista, elem):
  if keres_index(lista, elem) != -1:
    return True
  else:
    return False
