import re

line1 = "May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)"
print(re.search(r"ticky: INFO: ([\w ]*) ", line1))

line2 = "May 27 11:45:40 ubuntu.local ticky: ERROR: Error creating ticket [#1234] (username)"
print(re.search(r"ticky: ERROR: ([\w ]*) ", line2))


error1 = "Jan 31 01:43:10 ubuntu.local ticky: ERROR Tried to add information to closed ticket (jackowens)"
error2 = "Jan 31 02:55:31 ubuntu.local ticky: ERROR Ticket doesn't exist (xlg)"
error3 = "Jan 31 03:05:35 ubuntu.local ticky: ERROR Timeout while retrieving information (ahmed.miller)"
error4 = "Jan 31 08:01:40 ubuntu.local ticky: ERROR Tried to add information to closed ticket (jackowens)"

# count how many errors are of the same type
regex_error_msg = r": (.*?) \("
error_msg = re.search(regex_error_msg, error1)
print(error_msg[1])
# how many info and error messages there are for a given user (dictionary)
regex_username = r"\((.*?)\)"
username = re.search(regex_username, error1)
print(username[1])
