#! python3
import os

os.system('touch ./linuxUserInfo.txt')

print('What can the current user perform?\n')
os.system("sudo -l > ./linuxUserInfo.txt")

print("\nWho are you? Who is/has been logged in? Who can do what?\n")
print("Printing sudo -l, id, who, w, last output to file /LinuxUserInfo.txt")
os.system("id >> ./linuxUserInfo.txt;")
print("\n")
os.system("who >> ./linuxUserInfo.txt;")
print("\n")
os.system("w >> ./linuxUserInfo.txt;")
print("\n")
os.system("last >> ./linuxUserInfo.txt;")
