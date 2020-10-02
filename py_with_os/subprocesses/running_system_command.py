import subprocess

subprocess.run(["date"]) # CompletedProcess(args=['date'], returncode = 0)

subprocess.run(['sleep', '2']) # CompletedProcess(args=['sleep', '2'], returncode=0)

result = subprocess.run(['ls', 'this_file_does_not_exist']) # ls: cannot access 'this_file_does_not_exist': No such file or directory

print(result.returncode) #

