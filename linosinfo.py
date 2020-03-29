#! python3
import os
os.system('touch ./linuxOsInfo.txt')

print('\nWhat is the OS info?')
os.system("cat /etc/issue/ > ./linuxOsInfo.txt;")
os.system("cat /etc/*-release >>./linuxOsInfo.txt;")

print('\nKernel Information? ')
os.system("cat /proc/version >>./linuxOsInfo.txt;")
os.system("uname -mrs >>./linuxOsInfo.txt;")
os.system("dmesg | grep Linux >>./linuxOsInfo.txt;")

print('\nEnvironmental Variable Information? ')
os.system("cat /etc/profile >>./linuxOsInfo.txt;")
print("\n")
os.system("cat /etc/bashrc >>./linuxOsInfo.txt;")
print("\n")
os.system("env >>./linuxOsInfo.txt;")

print('\nIs there a printer?\n')
os.system("lpstat -a >>./linuxOsInfo.txt;")

print("Writing OS version, kernel, evironmental variable, and printer information to ./linuxOsInfo.txt")

