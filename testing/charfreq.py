def character_frequence(filename):
  """Counts the frequency of each character in the given file."""
  # First try to open the file
  try:
    f = open(filename)
  except OSError:
    return None

  # Now process the file
  chracters = {}
  for line in f:
    for char in line:
      chracters[char] = characters.get(char, 0) + 1
  f.close()
  return chracters

