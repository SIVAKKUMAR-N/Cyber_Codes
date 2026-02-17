import os
import platform

# Get current user's home directory
home = os.environ.get('HOME')  # Linux/macOS
print(home)

print(os.name)  # 'posix' means linux/mac, 'nt' means windows nt from windowsw nt, 'java' for java platform 
print(platform.system())  # 'Linux', 'Windows', 'Java'
print(platform.release())  # OS version

os.system('echo "these are the system info"')  # run a system command
