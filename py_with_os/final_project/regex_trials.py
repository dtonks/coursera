import re
import operator

# find if it's an ERROR or INFO
def error_type(message):
  regex_error_or_info = r"(ERROR|INFO)"
  msg_type = re.search(regex_error_or_info, message)
  return msg_type[1]

# how many info and error messages there are for a given user (dictionary)
def regex_username(message):
  regex_username = r"\((.*?)\)"
  username = re.search(regex_username, message)
  return username[1]

message = ["Jan 31 01:43:10 ubuntu.local ticky: ERROR Tried to add information to closed ticket (jackowens)",
           "Jan 31 02:55:31 ubuntu.local ticky: ERROR Ticket doesn't exist (xlg)",
           "Jan 31 03:05:35 ubuntu.local ticky: ERROR Timeout while retrieving information (ahmed.miller)",
           "Jan 31 08:01:40 ubuntu.local ticky: ERROR Tried to add information to closed ticket (jackowens)",
           "Jan 31 01:00:50 ubuntu.local ticky: INFO Commented on ticket [#4709] (blossom)"
          ]

# Error Message - I want Error and Count
def get_error(message):
  error_message = {}
  regex_error_msg = r": \w+ (.*?) \("
  for line in message:
    error_message[error_type(line)] = error_message.get(error_type(line), 0) + 1
    # error_sort = sorted(error_message.items(), key=operator.itemgetter(1), reverse=True)
  # print(error_sort)
    return error_message


# User Statistic - I want Username and a count of Username[error], username[info]
user_stats = {}
for line in message:
  user_stats[regex_username(line)] = {get_error(line): 1
  }

  # user_stats.get(regex_username(line), 0) + 1


# sort = sorted(user_stats.items(), key=operator.itemgetter(1), reverse=True)
print(user_stats)
