#  Definir una función que detecte si una palabra es un palíndromo y devuelve True o False.
#  Modificar la función para ignorar espacios, signos de puntuación, y que no haga distinción entre mayúsculas y minúsculas (pueden usar str.lower()). Pueden usar el nombre del desafío como un palindromo de ejemplo.

def pal(str):
  MARKS = set("ºª\!\"@·#$~%€&¬/()='?¡¿`^[+*]´¨{},;.:-_<>")
  ACCENTS = {"á":"a","é":"e","í":"i","ó":"o","ú":"u","â":"a","ê":"e","î":"i","ô":"o","û":"u","ý":"y","à":"a","è":"e","ì":"i","ò":"o","ù":"u"}

  str = str.lower()
  str = str.replace(' ', '')
  for c in str:
    if c in MARKS:
      str = str.replace(c, '')
    if c in ACCENTS:
      str = str.replace(c, ACCENTS[c])

  new_str = ''
  for i in range (len(str)):
    new_str = str[i] + new_str
  if str == new_str: 
    return True
  else:
    return False

if pal(input("Check for palindrome-ness!\n")):
  print("\nIt's a palindrome!")
else:
  print("\nSorry, that's not a palindrome.")
