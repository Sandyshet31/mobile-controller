# 📱 Mobile Controller (ADB + Scrcpy)

Control your Android phone from your laptop wirelessly.

---

## 🚀 What this does

* Connects your phone to laptop using WiFi
* Mirrors your phone screen on laptop
* Lets you control your phone from laptop

---

## 🧰 Requirements

### On Laptop:

* Python installed (https://python.org)
* ADB installed
* scrcpy installed

👉 Mac (Homebrew):

```
brew install android-platform-tools
brew install scrcpy
```

---

### On Phone:

1. Go to **Settings → About Phone**
2. Tap **Build Number** 7 times (enable developer mode)
3. Go to **Developer Options**
4. Turn ON:

   * USB Debugging
   * Wireless Debugging (if available)

---

## 🔌 First-Time Setup (IMPORTANT)

1. Connect phone to laptop using USB cable
2. Allow "USB Debugging" popup on phone

Check connection:

```
adb devices
```

You should see:

```
device
```

---

## 📡 Get Phone IP

On phone:

* Go to **Settings → WiFi**
* Tap your connected network
* Note the **IP Address** (example: 192.168.1.5)

---

## ▶️ Run the Project

In terminal:

```
python main.py
```

It will ask:

```
Enter phone IP:
```

Enter your phone IP.

---

## 🎮 What Happens Next

* Phone connects wirelessly
* Screen appears on laptop
* You can control phone using mouse

---

## 🛑 Stop

Just close the scrcpy window or press:

```
CTRL + C
```

---

## ⚠️ Notes

* Phone and laptop must be on SAME WiFi
* First connection requires USB
* Some gestures may feel different (scrcpy limitation)

---

## 💡 Future Improvements

* Add GUI
* Add buttons for back/home
* Auto-detect IP

---

## 👨‍💻 Author

Sandesh Shet
