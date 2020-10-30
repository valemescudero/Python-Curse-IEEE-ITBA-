#  For this challenge you have to program a linter to verify the correct usage of brackets in a text.
#  The text will be an input that may include parentheses, square brackets and/or braces and the algorithm must print True or False
#  according to whether all brackets are properly paired or not.

def perfectly_closed(text):
    brackets = {'(':0,')':0, '[':0,']':0, '{':0,'}':0}
    for c in text:
        if c in brackets:
            brackets[c]= brackets[c] + 1 
    if brackets['('] == brackets[')'] and brackets['['] == brackets[']'] and brackets['{'] == brackets['}']:
        return True
    else:
        return False

print(perfectly_closed(input()))
