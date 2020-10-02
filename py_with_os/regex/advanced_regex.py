import re
result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
print(result)

# returns tuple of two elements - ('Lovelace', 'Ada')
print(result.groups())

# returns whole string - Lovelace, Ada
print(result[0])

# returns first element in string - Lovelace
print(result[1])

# returns second element in string - Ada
print(result[2])

# Ada Lovelace
print(f"{result[2]} {result[1]}")

# Does not account for middle inital
def rearrange_name(name):
  result = re.search(r"^(\w*), (\w*)$", name)
  if result is None:
    return name
  return f"{result[2]} {result[1]}"

# updated for middle initial (my version)
def rearrange_name(name):
  # result = re.search(r"(\w*), (\w*)(..\.)?", name)
  result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
  if result is None:
    return name
  return f"{result[2]} {result[1]}" if result[3] is None else f"{result[2]}{result[3]} {result[1]}"

# correct way - don't need 3 results
def rearrange_name(name):
  # result = re.search(r"(\w*), (\w*)(..\.)?", name)
  result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
  if result is None:
    return name
  return f"{result[2]} {result[1]}"

print(rearrange_name('Tonks, Darren'))
print(rearrange_name('Kennedy, John F'))
