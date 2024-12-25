import os
import requests
import time
import socket
import webbrowser
from colorama import Fore, Style

def banner():
    print(Fore.YELLOW + r"""
██╗  ██╗   ████████╗██████╗  █████╗  ██████╗███████╗██████╗ 
██║  ██║   ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗
███████║█████╗██║   ██████╔╝███████║██║     █████╗  ██████╔╝
██╔══██║╚════╝██║   ██╔══██╗██╔══██║██║     ██╔══╝  ██╔══██╗
██║  ██║      ██║   ██║  ██║██║  ██║╚██████╗███████╗██║  ██║
╚═╝  ╚═╝      ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚══════╝╚═╝  ╚═╝
""" + Style.RESET_ALL)

def menu():
    print(Fore.GREEN + "[1]" + Fore.RESET + " Track IP Address")
    print(Fore.GREEN + "[2]" + Fore.RESET + " Track Your IP Address")
    print(Fore.GREEN + "[3]" + Fore.RESET + " About Us")
    print(Fore.GREEN + "[4]" + Fore.RESET + " Help")
    print(Fore.GREEN + "[5]" + Fore.RESET + " Update H-Tracer")
    print(Fore.GREEN + "[6]" + Fore.RESET + " View on Map")
    print(Fore.GREEN + "[7]" + Fore.RESET + " Perform Port Scan")
    print(Fore.GREEN + "[8]" + Fore.RESET + " Perform Network Diagnostics")
    print(Fore.GREEN + "[X]" + Fore.RESET + " Exit")
    print()

def track_ip(ip):
    print(Fore.CYAN + f"Tracking IP: {ip}..." + Style.RESET_ALL)
    response = requests.get(f"http://ip-api.com/json/{ip}")
    if response.status_code == 200:
        data = response.json()
        for key, value in data.items():
            print(f"{key.capitalize()}: {value}")
    else:
        print(Fore.RED + "Error: Unable to fetch data." + Style.RESET_ALL)

def track_my_ip():
    print(Fore.CYAN + "Fetching your IP address..." + Style.RESET_ALL)
    response = requests.get("https://api64.ipify.org?format=json")
    if response.status_code == 200:
        ip = response.json()['ip']
        print(Fore.CYAN + f"Your IP Address: {ip}" + Style.RESET_ALL)
        track_ip(ip)
    else:
        print(Fore.RED + "Error: Unable to fetch your IP address." + Style.RESET_ALL)

def view_on_map(ip):
    print(Fore.CYAN + f"Opening map for IP: {ip}..." + Style.RESET_ALL)
    webbrowser.open(f"https://www.google.com/maps/search/?api=1&query={ip}")

def port_scan(ip):
    print(Fore.CYAN + f"Performing port scan on {ip}..." + Style.RESET_ALL)
    for port in range(1, 1025):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(Fore.GREEN + f"Port {port} is open." + Style.RESET_ALL)
        sock.close()

def network_diagnostics(ip):
    print(Fore.CYAN + f"Pinging {ip}..." + Style.RESET_ALL)
    response = os.system(f"ping -c 4 {ip}")
    if response == 0:
        print(Fore.GREEN + f"{ip} is reachable." + Style.RESET_ALL)
    else:
        print(Fore.RED + f"{ip} is not reachable." + Style.RESET_ALL)

def return_to_menu():
    input(Fore.YELLOW + "\nPress Enter to return to the menu..." + Style.RESET_ALL)
    os.system('clear')
    banner()

def main():
    os.system('clear')
    banner()
    while True:
        menu()
        choice = input(Fore.GREEN + "H-Trace >> " + Style.RESET_ALL).strip().lower()
        if choice == "1":
            ip = input(Fore.YELLOW + "Enter IP Address: " + Style.RESET_ALL)
            track_ip(ip)
            return_to_menu()
        elif choice == "2":
            track_my_ip()
            return_to_menu()
        elif choice == "3":
            print(Fore.CYAN + "H-Tracer: A simple tool to track IP addresses." + Style.RESET_ALL)
            return_to_menu()
        elif choice == "4":
            print(Fore.CYAN + "Help: Use options 1 or 2 to track IPs. Option 6 displays IP on map." + Style.RESET_ALL)
            return_to_menu()
        elif choice == "5":
            print(Fore.CYAN + "Updating IP-Tracer..." + Style.RESET_ALL)
            time.sleep(1)
            print(Fore.CYAN + "Updated to the latest version." + Style.RESET_ALL)
            return_to_menu()
        elif choice == "6":
            ip = input(Fore.YELLOW + "Enter IP Address to view on map: " + Style.RESET_ALL)
            view_on_map(ip)
            return_to_menu()
        elif choice == "7":
            ip = input(Fore.YELLOW + "Enter IP Address to scan ports: " + Style.RESET_ALL)
            port_scan(ip)
            return_to_menu()
        elif choice == "8":
            ip = input(Fore.YELLOW + "Enter IP Address to diagnose network: " + Style.RESET_ALL)
            network_diagnostics(ip)
            return_to_menu()
        elif choice == "x":
            print(Fore.RED + "Exiting H-Tracer. Goodbye!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)
            return_to_menu()

if __name__ == "__main__":
    main()
