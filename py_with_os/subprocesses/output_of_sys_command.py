import subprocess

result = subprocess.run(['host', '8.8.8.8'], capture_output=True)
print(result.returncode) # 0

print(result.stdout) # b'8.8.8.8.in-addr.arpa domain name pointer dns.google.\n'
# The b at the front of the output represents an array of bytes to represent up to 256 characters

print(result.stdout.decode().split()) # ['8.8.8.8.in-addr.arpa', 'domain', 'name', 'pointer', 'dns.google.']
# using decode method we can convert to UTF-8 which is the standard of all represented characters

result = subprocess.run(['rm', 'does_not_exist'], capture_output=True) # errors out
print(result.stdout) # b''

print(result.stderr) # b"rm: cannot remove 'does_not_exist': No such file or directory\n"
