import os

print("Mobile Controller Started")

def connect(ip):
    os.system(f"adb connect {ip}:5555")

def mirror():
    os.system("scrcpy")

ip = input("Enter phone IP: ")
connect(ip)
mirror()