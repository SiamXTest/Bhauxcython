#!/data/data/com.termux/files/usr/bin/python3.12
# -*- coding: utf-8 -*-
import os
import subprocess

bit = os.uname().machine
changes = subprocess.getoutput("git status --porcelain")

# ✅ Git পরিবর্তন থাকলে ক্লিন + pull
if changes:
    os.system("git reset --hard")
    os.system("git clean -fd")
    os.system("git pull")

os.system("chmod 777 *")

# ✅ .so ফাইল ইমপোর্ট করা (শুধু 64-bit এ)
if '64' in bit:
    import BhauTheUltimateTools  # ← .so ফাইলের নাম (cpython-312 বাদ দিয়ে)
else:
    os.system("clear")
    print("❌ TOOL NOT AVAILABLE FOR 32-BIT DEVICE")
