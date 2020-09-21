import os
import subprocess

my_env = os.environ.copy()
my_env["PATH"] = os.pathsep.join(["/opt/adv_subprocess_mgmt/", my_env["PATH"]])


result = subprocess.run(['adv_subprocess_mgmt'], env=my_env)
