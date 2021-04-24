# Coded by Raven aka HeadlessMan
# XploitSec-ID - 2021
import socket, platform, os
from datetime import date
from datetime import datetime
import random as anjayy
import time
from colorama import Fore,Style
import smtplib

now = datetime.now()
hostname = socket.gethostname()
ipaddres = socket.gethostbyname(hostname)
biru = f"{Fore.BLUE}"
tutup = f"{Style.RESET_ALL}"
os.system("clear")
banner = f"""
{biru}System Information{tutup}
-------------------
{biru}OS{tutup}: {platform.system()}
{biru}OS Release{tutup}: {platform.release()}
{biru}Host{tutup}: {hostname}
{biru}IP Addres{tutup}: {ipaddres}
{biru}Date{tutup}: {date.today()}
{biru}Time{tutup}: {now.strftime("%H:%M:%S")}
{biru}Processor{tutup}: {platform.processor()}
{biru}Machine{tutup}: {platform.machine()}
{biru}Language{tutup}: Python3
{biru}Coded by{tutup}: HeeadlessMan
{biru}Github{tutup}: https://github.com/africode7
{biru}Telegram{tutup}: https://t.me/headlessman7
{biru}Team{tutup}: XploitSec-ID
"""
print(banner)

def getotp():
    emailuser = input("Enter your email: ")
    global otp
    otp = ""
    for raven in range(6):
        otp += str(anjayy.randint(1,9))
    mes = f"""
    I have send the OTP code to the email {emailuser}
    Please check the OTP code first then enter it to login..!
    """
    sender = "headlessmanlog@gmail.com"
    messageemail = f"""From: Dari Email {sender}
To: Untuk Email {emailuser}
Subject: CODE OTP!

Your OTP is {otp}
Thanks from HeadlessMan.
    """
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("headlessmanlog@gmail.com","secretkey7") #login email
    server.sendmail(sender, emailuser, messageemail)
    time.sleep(2)
    print(mes)

def isitools():
    print("Hello world!")

getotp()
pwuser = input("Enter your OTP: ")
if pwuser == otp:
   print("Your OTP is right, wait a moment..")
   time.sleep(2)
   isitools()
else:
   print("OTP wrong, try again!")
