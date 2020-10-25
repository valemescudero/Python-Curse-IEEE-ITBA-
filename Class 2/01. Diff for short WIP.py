def derivada(lista):
  new_lista = []
  
  for i in range(1,len(lista)):
    r = lista[i] - lista[i-1]
    new_lista.append(r)
  return new_lista


lista = [3, 2, 3]
print(derivada(lista))
