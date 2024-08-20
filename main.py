# Subdomain scanner by @tarpiov in all socials mediaa

#!/usr/bin/python3
import threading
import time
import requests
import urllib3
from utils import screen
from utils.colors import Colors


subdomains = []
threads = []


def create_thread(domain):

    screen.clearScreen()
    print(screen.searchingSubdomains())

    for subdomain in subdomains:
        
        url = f"https://{subdomain}.{domain}"
        thread = threading.Thread(target=scan, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:

        thread.join()
        

def scan(url):

    try: 
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:

            print(f"    {Colors.green}[+] Subdominio encontrado: {Colors.white}{url}")

    except requests.ConnectionError:
        pass

    except requests.Timeout:      
        pass

    except requests.exceptions.InvalidURL:
        pass

    except urllib3.exceptions.LocationParseError:   
        pass

    except KeyboardInterrupt:

        print(f"{Colors.red} Ctrl + C detectado, saliendo...{reset}")
        time.sleep(0.3)
        pass

def main():
    

    try:
        screen.clearScreen()

        print(screen.getBanner())

        print(f"\n    ➤ 1. Normal (estándar)\n    ➤ 2. Spanish (subdominios españoles)\n")

        opt = int(input(f"\n     {Colors.red}root@tarpiov> "))

        if opt == 1:
            
            screen.clearScreen()
            with open('subdomains-lite.txt', 'r') as low:
                for subdomain in low:
                    subdomains.append(subdomain.strip())

                print(screen.menuSubdomains())

                domain = input(f"\n   {Colors.red}root@tarpiov>{Colors.white} ")
                create_thread(domain)

        elif opt == 2:
            
            screen.clearScreen()
            with open('subdomains-spanish.txt', 'r') as mid:
                for subdomain in mid:
                    subdomains.append(subdomain.strip())

                print(screen.menuSubdomains())

                domain = input(f"\n   {Colors.red}root@tarpiov> {Colors.white}")
                create_thread(domain)

        else:

            print(f"{Colors.red}[!] Opción inválida! {Colors.reset}")
            pass

    except KeyboardInterrupt:

        print(f"{Colors.red} [!] Ctrl + C detectado{Colors.reset}")
        print(screen.getExceptions())
        time.sleep(0.3)
        pass


if __name__ == "__main__":
    main()

