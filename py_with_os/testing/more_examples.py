import re

my_txt = "An investment in knowledge pays the best interest."

def LetterCompiler(txt):
    if type(txt) is str:
        result = re.findall(r'([a-c]).', txt)
        return result
    return []

print(LetterCompiler(my_txt))
