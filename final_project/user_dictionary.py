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

# how many info and error messages there are for a given user (dictionary)
def regex_username(message):
  regex_username = r"\((.*?)\)"
  username = re.search(regex_username, message)
  return str(username[1])

# find if it's an ERROR or INFO
def error_type(message):
  regex_error_or_info = r"(ERROR|INFO)"
  msg_type = re.search(regex_error_or_info, message)
  return str(msg_type[1])

# type of error message
def error_msg(message):
  regex_error_msg = r": \w+ (.*?) (\[#|\()"
  err_msg = re.search(regex_error_msg, message)
  return str(err_msg[1])

message = ["Jan 31 01:43:10 ubuntu.local ticky: ERROR Tried to add information to closed ticket (jackowens)",
           "Jan 31 02:55:31 ubuntu.local ticky: ERROR Ticket doesn't exist (xlg)",
           "Jan 31 03:05:35 ubuntu.local ticky: ERROR Timeout while retrieving information (ahmed.miller)",
           "Jan 31 08:01:40 ubuntu.local ticky: ERROR Tried to add information to closed ticket (jackowens)",
           "Jan 31 08:01:40 ubuntu.local ticky: INFO Commented on ticket [#4709] (jackowens)",
           "Jan 31 01:00:50 ubuntu.local ticky: INFO Commented on ticket [#4709] (blossom)"
          ]

# Error Message - I want Error message and Count
def get_error(message):
  error_message = {}
  for line in message:
    error_message[error_msg(line)] = error_message.get(error_msg(line), 0) + 1
  error_message = sorted(error_message.items(), key=operator.itemgetter(1), reverse=True)
  return error_message
print(get_error(message))

# User Statistic - I want Username and a count of Username[error], username[info]
# user_stats = {"Darren": {"ERROR": 1, "INFO": 1}}
def user_statistics(message):
  user_stat = {}
  for line in message:
    user_stat[regex_username(line)] = {"ERROR": 0, "INFO": 0}
  for line in message:
    if error_type(line) == "ERROR":
      user_stat[regex_username(line)]["ERROR"] += 1
    else:
      user_stat[regex_username(line)]["INFO"] += 1
  user_stat = sorted(user_stat.items())
  return user_stat
print(user_statistics(message))
