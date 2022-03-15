import string
import random
import time
import os
from colorama import init
from colorama import Fore, Back, Style
init()

#Enter your domains
domains = (".ru",".рф")

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
randstr = lower + upper + num

f = open("ipaddresses.txt","a")

timez = time.strftime("%H:%M:%S", time.localtime())


f.write("\n\nNew instance opened at {}".format(timez))

def scan():
    length = random.randint(1,25)

    webstr = random.sample(randstr, length)

    domainstr = random.choice(tuple(domains))

    ip_addr = "".join(webstr) + domainstr

    print("\nChecking " + ip_addr + "\n")

    response = os.system("ping -n 1 {}".format(ip_addr))

    time.sleep(0.2)

    timez = time.strftime("%H:%M:%S", time.localtime())

    if response == 0:
        f.write("\n[{time}] {ip} is valid\n".format(time = timez,ip= ip_addr))
        print(Fore.BLUE + "\n{} exists!\n".format(ip_addr))
        print(Style.RESET_ALL)
    else:
        print("\n{} does not exist.".format(ip_addr))




print("--------------------------------")
print("      IP Scanning Program       ")
print("                                ")
print("        Coded by pipe05         ")
print("      Time:     {}             ".format(timez))
print("--------------------------------")
commence = input("\nCommence IP search?[Y/n]:")
if commence == "Y" or commence == "y":
    while True:
        scan()

elif commence == "n" or "N":
    print("Exiting...")

    for i in range(5):
        exitstr = random.sample(randstr, 10)

        exitstring = "".join(exitstr)

        print(exitstring)

        time.sleep(0.5)

    print("\nBye!")
else:
    print("Please input a valid option: [Y/n]")
    exit()
