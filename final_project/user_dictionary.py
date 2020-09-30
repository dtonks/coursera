import re
import operator
import csv

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

# {"Ticket doesn't exist": 2, "Commented on ticket": 1}
def get_error(message):
  error_message = {}
  for line in message:
    error_message[error_msg(line)] = error_message.get(error_msg(line), 0) + 1
  error_message = sorted(error_message.items(), key=operator.itemgetter(1), reverse=True)
  return error_message
# print(get_error(message))

 # {"Darren": {"ERROR": 2, "INFO": 1}}
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
# print(user_statistics(message))

# output error_message.csv
with open("error_message.csv", "w") as csv_file:
  with open("syslog.log", "r") as f:
    fieldnames = ["Error", "Count"]
    error_message = get_error(f.readlines())

    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for row in error_message:
      writer.writerow({"Error": row[0], "Count": row[1]})

# output user_statistics.csv
with open("user_statistics.csv", "w") as csv_file:
  with open("syslog.log", "r") as f:
    fieldnames = ["Username", "INFO", "ERROR"]
    user_stats = user_statistics(f.readlines())

    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for row in user_stats:
      writer.writerow({"Username": row[0],
                       "INFO": row[1]["INFO"],
                       "ERROR": row[1]["ERROR"]})
