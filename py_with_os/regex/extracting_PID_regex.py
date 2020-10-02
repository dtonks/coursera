import re

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1]) # 12345

result = re.search(regex, "A completely different string that also has numbers [34567]")
print(result[1]) # 34567

# result = re.search(regex, "99 elephants in a [cage]")
# print(result[1]) # ERROR - Not Scriptable

def extract_pid(log_line):
  regex = r"\[(\d+)\]"
  result = re.search(regex, log_line)
  return "Not a valid log" if result is None else result[1]

print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345
print(extract_pid("99 elephants in a [cage]")) # Not a valid log


# Add to the regular expression used in the extract_pid function, to return the uppercase message in parenthesis, after the process id.
def extract_pid(log_line):
    regex = r"(\[(\d+)\]): (\b[A-Z]*\b)"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result[2], result[3])

print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)


