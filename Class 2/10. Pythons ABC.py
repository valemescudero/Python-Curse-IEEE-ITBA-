#  An ancient stone has been found in Buenos Aires. Its inscriptions may help us to decipher an entirely new alphabet.
#  Thanks to these carvings it has been discovered that archaic Latin alphabet has a correspondence with Latin alphabet.
#  You must create a program to translate from one alphabet into the other:

#  Write a function to receive a string, translate every known archaic Latin character into its modern equivalent WITHOUT altering any other character
#  (punctuation marks, spaces, etc.) and return the resulting string.

#  For instance,
#  translate( "𐌀𐌋𐌐𐌇𐌀𐌁𐌄𐌕" ) => "ALPHABET"
#  translate( "𐌇𐌄𐌋𐌋𐌏!" ) => "HELLO!"
#  translate("Y𐌄𐌔 𐌏𐌓 𐌍𐌏? 𐌌𐌌𐌌... 𐌏𐌊.") => "YES OR NO? MMM... OK."

#  Correspondence between alphabets:
#  Archaic : Modern
#  '𐌀' : 'A', '𐌁' : 'B', '𐌂' : 'C', '𐌃' : 'D', '𐌄' : 'E', '𐌅' : 'F', '𐌆' : 'Z',
#  '𐌇' : 'H', '𐌉' : 'I', '𐌊' : 'K', '𐌋' : 'L', '𐌌' : 'M', '𐌍' : 'N', '𐌏' : 'O',
#  '𐌐' : 'P', '𐌒' : 'Q', '𐌓' : 'R', '𐌔' : 'S', '𐌕' : 'T', '𐌖' : 'V', '𐌗' : 'X'

alpha_translit = { 
    '𐌀' : 'A', '𐌁' : 'B', '𐌂' : 'C', '𐌃' : 'D', '𐌄' : 'E', '𐌅' : 'F', '𐌆' : 'Z',
    '𐌇' : 'H', '𐌉' : 'I', '𐌊' : 'K', '𐌋' : 'L', '𐌌' : 'M', '𐌍' : 'N', '𐌏' : 'O',
    '𐌐' : 'P', '𐌒' : 'Q', '𐌓' : 'R', '𐌔' : 'S', '𐌕' : 'T', '𐌖' : 'V', '𐌗' : 'X'
}

def transliterate(text):
    transliteration = ''
    for character in text:
        if character in alpha_translit:
            transliteration += alpha_translit[character]
        else:
            transliteration += character
    return transliteration

text = input("Please, enter your archaic Latin text below to begin transliteration:\n")
transliteration = transliterate(text)
print("")
print("Transliteration:", transliteration)

