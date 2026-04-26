import os

def connect(ip):
    os.system(f"adb connect {ip}:5555")

def mirror():
    os.system("scrcpy")

def install(apk_path):
    os.system(f"adb install {apk_path}")

def shell():
    os.system("adb shell")

def menu():
    print("\n=== Mobile Controller ===")
    print("1. Connect to device")
    print("2. Mirror screen")
    print("3. Install APK")
    print("4. Open shell")
    print("5. Exit")

while True:
    menu()
    choice = input("Choose option: ")

    if choice == "1":
        ip = input("Enter device IP: ")
        connect(ip)

    elif choice == "2":
        mirror()

    elif choice == "3":
        path = input("Enter APK path: ")
        install(path)

    elif choice == "4":
        shell()

    elif choice == "5":
        break

    else:
        print("Invalid choice")