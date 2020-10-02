import re

# anything inside square bracket is taking the literal character and not it's meaning
result = re.split(r"[.?!]", "One sentence. Another one? And the last one!")
print(result) # ['One sentence', ' Another one', ' And the last one', '']

# use parentheses to include the elements we are splitting
result = re.split(r"([.?!])", "One sentence. Another one? And the last one!")
print(result) # ['One sentence', '.', ' Another one', '?', ' And the last one', '!', '']

# redacting certain items
result = re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Recieved an email for go_nuts95@my.example.com")
# print(result) # Recieved an email for [REDACTED]
import re
result = re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada")
print(result) # Ada Lovelace
