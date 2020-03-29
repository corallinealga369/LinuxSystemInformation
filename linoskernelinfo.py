#! python3
import os

print('\n\nWhat is the OS info?\n')
os.system("cat /etc/issue/;")
os.system("cat /etc/*-release;")

print('\n\nKernel Information: \n')
os.system("cat /proc/version;")
os.system("uname -mrs;")
os.system("dmesg | grep Linux;")



