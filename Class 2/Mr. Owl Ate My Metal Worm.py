def pal(str):
  MARKS = set("ºª\!\"@·#$~%€&¬/()='?¡¿`^[+*]´¨{},;.:-_<>áéíóúâêîôûýàèìòù")

  str = str.lower()
  str = str.replace(' ', '')
  for c in str:
    if c in MARKS:
      str = str.replace(c, '')

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
