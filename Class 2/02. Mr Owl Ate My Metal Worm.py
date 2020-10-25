#  Write a function to find out whether a given word or sentence is a palindrome and return True or False accordingly
#  The function should ignore spaces and punctuation marks and make no distinction between lower and uppercase.

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
