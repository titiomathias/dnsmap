import requests
import sys
import datetime

def get_current_time():
    now = datetime.datetime.now().time()
    return f"{now.hour}:{now.minute}:{now.second}"

def help_menu():
    print("\nHOW TO USE: write the target address like 'google.com' or 'amazon.com' and don't use 'http://' or 'www'.\n(Now it's just start and attack. I am not responsible for any illegal actions taken.)\n")
    print("dnsmap.py -h to access help")
    print("")
    print("""
    [+] COMMAND [+]        |       [+] FUNCTION [+]

    -dns                   Recieve a DNS address to test [dnsmap.py -dns google.com]
    -wordlist              Choose a wordlist in your folder to use [dnsmap.py -dns google.com -wordlist "wordlist.txt"].
                           If you don't have a wordlist the script uses a default list. """)

def print_banner():
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
    print("[!] Made by: github.com/titiomathias/ [!]")
    print("[+] DNS Finder Tool for Pentest Security [+]")

def read_wordlist(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"\nERROR - File not found: {file_path}\n")
        sys.exit(1)

def perform_dns_search(address, wordlist):
    date = get_current_time()
    print(f"\n[-{date}-] Starting DNS search for the address -> {address}\n")
    for line in wordlist:
        subdomain = line.strip()
        link = f"http://{subdomain}{address}"
        try:
            response = requests.get(link, timeout=5)
            print(f"[!] {response.status_code} [!] -> {link}")
        except requests.RequestException:
            continue
    print(f"\n[#] Finished [#] - [-{date}-]")

def main():
    print_banner()
    argumento = sys.argv
    index = len(argumento)

    if index == 1 or (index > 1 and argumento[1] == "-h"):
        help_menu()
        return

    if index == 2:
        if argumento[1] == "-dns":
            print("\nERROR - Address not typed.")
            print("Type the DNS address you want to search. [dnsmap.py -dns google.com]")
        else:
            help_menu()
        return

    if index >= 3:
        if argumento[1] == "-dns":
            address = argumento[2]

            if index == 3:
                default_wordlist = "atk.txt"
                wordlist = read_wordlist(default_wordlist)
                perform_dns_search(address, wordlist)

            elif index == 5 and argumento[3] == "-wordlist":
                user_wordlist = argumento[4]
                wordlist = read_wordlist(user_wordlist)
                perform_dns_search(address, wordlist)
            else:
                help_menu()
        else:
            help_menu()
    else:
        help_menu()

if __name__ == "__main__":
    main()
