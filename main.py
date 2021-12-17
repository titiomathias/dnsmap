import requests
import time

file = open("atk.txt")

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
print("\nHOW TO USE: write the target address like 'google.com' or 'amazon.com' and don't use 'http://' or 'www'.\n(Now it's just start and attack. I am not responsible for any illegal actions taken.)\n")

print("Starting", end="")
time.sleep(1)
print(".", end="")
time.sleep(1)
print(".", end="")
time.sleep(1)
print(".", end="")
time.sleep(1)
print("\n")

address = input("+ Target: ")

print("\nSearching...\n")

for line in file.readlines():
    line = line.rstrip("\n")
    try:
        link = f"http://{line}{address}"
        add_found = r = requests.get(link)
        print(f"[!] {add_found.status_code} [!] -> {link}")
    except:
        print(end="")
        continue

print("\n[#] Finished [#]")