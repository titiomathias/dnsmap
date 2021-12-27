import requests
import sys
import datetime

now = datetime.datetime.now().time()
date = f"{now.hour}:{now.minute}:{now.second}"
file = open("atk.txt")

def help_menu():
    print("\nHOW TO USE: write the target address like 'google.com' or 'amazon.com' and don't use 'http://' or 'www'.\n(Now it's just start and attack. I am not responsible for any illegal actions taken.)\n")
    print("dnsmap.py -h to access help")

    print("")

    print("""
    [+]COMAND[+]        |       [+]FUNCTION[+]

    -dns                         Recive a dns address to test [dnsmap.py -dns google.com]
    -wordlist                    Choose a wordlist in your folder to use [dnsmap.py -dns google.com -wordlist "wordlist.txt"].
                                 If you don't have a wordlist the script choose a default list. """)


print("""
▓█████▄  ███▄    █   ██████  ███▄ ▄███▓ ▄▄▄       ██▓███  
▒██▀ ██▌ ██ ▀█   █ ▒██    ▒ ▓██▒▀█▀ ██▒▒████▄    ▓██░  ██▒
░██   █▌▓██  ▀█ ██▒░ ▓██▄   ▓██    ▓██░▒██  ▀█▄  ▓██░ ██▓▒
░▓█▄   ▌▓██▒  ▐▌██▒  ▒   ██▒▒██    ▒██ ░██▄▄▄▄██ ▒██▄█▓▒ ▒
░▒████▓ ▒██░   ▓██░▒██████▒▒▒██▒   ░██▒ ▓█   ▓██▒▒██▒ ░  ░
 ▒▒▓  ▒ ░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░░ ▒░   ░  ░ ▒▒   ▓▒█░▒▓▒░ ░  ░
 ░ ▒  ▒ ░ ░░   ░ ▒░░ ░▒  ░ ░░  ░      ░  ▒   ▒▒ ░░▒ ░     
 ░ ░  ░    ░   ░ ░ ░  ░  ░  ░      ░     ░   ▒   ░░       
   ░             ░       ░         ░         ░  ░         
 ░                                                        
""")
print("[!] Maked by: github.com/titiomathias/ [!]")
print("[+] DNS Finder Tool to Pentest Security [+]")

argumento = sys.argv
index = len(argumento)

if index == 1:
    help_menu()

if index == 2:
    if argumento[1] == "-dns":
        print("\nERROR - Address not typed.")
        print("Type what dns address you wanna search. [dnsmap.py -dns google.com]")
    else:
        help_menu()

if index == 3:
    if argumento[1] == "-dns":
        address = argumento[2]
        print(f"\n[-{date}-] Starting DNS search for the address -> {address}\n")
        for line in file.readlines():
            line = line.rstrip("\n")
            try:
                link = f"http://{line}{address}"
                add_found = r = requests.get(link)
                print(f"[!] {add_found.status_code} [!] -> {link}")
            except:
                print(end="")
                continue
        print(f"\n[#] Finished [#] - [-{date}-]")
    else:
        help_menu()


if index == 4:
    if argumento[3] == "-wordlist":
        print("\nERROR - Wordlist not typed.")
        print("Type where is your wordlist. [dnsmap.py -dns google.com Downloads/wordlists/example.txt]")
    else:
        help_menu()

if index == 5:
    if argumento[3] == "-wordlist":
        address = argumento[2]
        file_user = open(argumento[4])
        print(f"\n[-{date}-] Starting DNS search for the address -> {address}\n")
        for line in file_user.readlines():
            line = line.rstrip("\n")
            try:
                link = f"http://{line}{address}"
                add_found = r = requests.get(link)
                print(f"[!] {add_found.status_code} [!] -> {link}")
            except:
                print(end="")
                continue
        print(f"\n[#] Finished [#] - [-{date}-]")
    else:
        help_menu()
