#! python3
import os

print('What can the current user perform?\n')
os.system("sudo -l;")

print("\n\nWho are you? Who is/has been logged in? Who can do what?\n")
os.system("id;")
print("\n")
os.system("who;")
print("\n")
os.system("w;")
print("\n")
os.system("last;")
