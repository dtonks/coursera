import re


print(re.search(r"[a-zA-Z]{5}", "a ghost")) # 'ghost'

print(re.search(r"[a-zA-Z]{5}", "a scary ghost appeared")) # 'scary'

print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared")) # ['scary', 'ghost', 'appea']

print(re.findall(r"\b[a-zA-Z]{5}\b", "a scary ghost appeared")) # ['scary', 'ghost']

print(re.findall(r"\w{5,10}\b", "I really like strawberries")) # ['really', 'rawberries']

print(re.findall(r"\w{5,}\b", "I really like strawberries")) # ['really', 'strawberries']

print(re.search(r"s\w{,20}", "I really like strawberries")) # 'strawberries'


# The long_words function returns all words that are at least 7 characters. Fill in the regular expression to complete this function.
def long_words(text):
  pattern = "[a-zA-Z]{7,}"
  result = re.findall(pattern, text)
  return result

print(long_words("I like to drink coffee in the morning.")) # ['morning']
print(long_words("I also have a taste for hot chocolate in the afternoon.")) # ['chocolate', 'afternoon']
print(long_words("I never drink tea late at night.")) # []
