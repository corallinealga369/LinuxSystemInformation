#! python3
import os

print('\n\n Environmental Variable Information: \n')
os.system("cat /etc/profile;")
print("\n")
os.system("cat /etc/bashrc;")
print("\n")
os.system("env;")

#print('\nWhat services are running as root?\n')
#os.system('ps aux|grep root;')
