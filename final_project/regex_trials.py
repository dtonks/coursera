import re
import operator
# line1 = "May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)"
# print(re.search(r"ticky: INFO: ([\w ]*) ", line1))

# line2 = "May 27 11:45:40 ubuntu.local ticky: ERROR: Error creating ticket [#1234] (username)"
# print(re.search(r"ticky: ERROR: ([\w ]*) ", line2))

# error1 = "Jan 31 01:43:10 ubuntu.local ticky: ERROR Tried to add information to closed ticket (jackowens)"
# error2 = "Jan 31 02:55:31 ubuntu.local ticky: ERROR Ticket doesn't exist (xlg)"
# error3 = "Jan 31 03:05:35 ubuntu.local ticky: ERROR Timeout while retrieving information (ahmed.miller)"
# error4 = "Jan 31 08:01:40 ubuntu.local ticky: ERROR Tried to add information to closed ticket (jackowens)"

## find if it's an ERROR or INFO
# def error_or_info(message):
#   regex_error_or_info = r"(ERROR|INFO)"
#   msg_type = re.search(regex_error_or_info, message)
#   return msg_type[1]

## count how many errors are of the same type
# regex_error_msg = r": (.*?) \("
# error_msg = re.search(regex_error_msg, error1)
# print(error_msg[1])

# how many info and error messages there are for a given user (dictionary)
def regex_username(message):
  regex_username = r"\((.*?)\)"
  username = re.search(regex_username, message)
  return username[1]

# def user_messages(file):
#   user_message_type = {}
#   with open(file, 'r') as f:
#     for line in f.readlines():
#       user_message_type[regex_username(line)] = user_message_type.get(char, 0) + 1
#   sort = user_message_type.sorted()
#   print(sort)

h = ["Jan 31 01:43:10 ubuntu.local ticky: ERROR Tried to add information to closed ticket (jackowens)", "Jan 31 02:55:31 ubuntu.local ticky: ERROR Ticket doesn't exist (xlg)", "Jan 31 03:05:35 ubuntu.local ticky: ERROR Timeout while retrieving information (ahmed.miller)", "Jan 31 08:01:40 ubuntu.local ticky: ERROR Tried to add information to closed ticket (jackowens)"]
user_message_type = {}
for line in h:
  user_message_type[regex_username(line)] = user_message_type.get(regex_username(line), 0) + 1
sort = sorted(user_message_type.items(), key=operator.itemgetter(1), reverse=True)
print(sort)

# message = "Jan 31 01:43:10 ubuntu.local ticky: ERROR Tried to add information to closed ticket (jackowens)\nJan 31 02:55:31 ubuntu.local ticky: ERROR Ticket doesn't exist (xlg)\n Jan 31 03:05:35 ubuntu.local ticky: ERROR Timeout while retrieving information (ahmed.miller)\n Jan 31 08:01:40 ubuntu.local ticky: ERROR Tried to add information to closed ticket (jackowens)"

# print(user_messages(message))
