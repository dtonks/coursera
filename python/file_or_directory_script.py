#script will tell you if files within a directory are a file or directory
import os
dir = 'code'
for name in os.listdir(dir):
    fullname = os.path.join(dir, name)
    if os.path.isdir(fullname):
            print(f"{fullname} is a directory")
    else:
            print(f"{fullname} is a file")


# output
# os.listdir('code')
# ['Untitled.ipynb', 'python', '.ipynb_checkpoints', 'dtonks', 'lewagon', 'coursera']

# code/python is a directory
# code/.ipynb_checkpoints is a directory
# code/dtonks is a directory
# code/lewagon is a directory
# code/coursera is a directory
