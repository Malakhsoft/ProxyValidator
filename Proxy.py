import csv
import threading
import socket
from tqdm import tqdm
import os
import platform

def clear_console():
    
    if platform.system() == 'Windows':
        os.system('cls')
    
    else:
        os.system('clear')
        
clear_console()
        
print(" __  __    _    _        _    _  ___   _   ____   ___  _____ _____ ")
print("|  \/  |  / \  | |      / \  | |/ / | | | / ___| / _ \|  ___|_   _|")
print("| |\/| | / _ \ | |     / _ \ | ' /| |_| | \___ \| | | | |_    | |  ")
print("| |  | |/ ___ \| |___ / ___ \| . \|  _  |  ___) | |_| |  _|   | |  ")
print("|_|  |_/_/   \_\_____/_/   \_\_|\_\_| |_| |____/ \___/|_|     |_|  ")

license_text = """
            GNU GENERAL PUBLIC LICENSE
            Version 3, 29 June 2007
            Copyright © 2007 Free Software Foundation, Inc.
            <https://fsf.org/>
            
            This program is free software: you can redistribute it and/or modify
            it under the terms of the GNU General Public License as published by
            the Free Software Foundation, either version 3 of the License, or
            any later version.
            
            This program is distributed in the hope that it will be useful,
            but WITHOUT ANY WARRANTY; without even the implied warranty of
            MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
            GNU General Public License for more details.
            
            You should have received a copy of the GNU General Public License
            along with this program.  If not, see <https://www.gnu.org/licenses/>.
            """
print(license_text)

def validate_proxy(ip_list, progress_bar, valid_proxies):
    while True:
        try:
            ip, port = ip_list.pop()
        except IndexError:
            break
        try:
            sock = socket.create_connection((ip, int(port)), timeout=5)
            valid_proxies.append((ip, port))
            sock.close()
        except Exception:
            pass
        finally:
            progress_bar.update(1)

def save_to_csv(valid_proxies):
    with open('MalakhProxy.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["IP", "Port"])
        writer.writerows(valid_proxies)

def main():

    try:
        with open('Free_Proxy_List.csv', 'r') as file:
            reader = csv.DictReader(file)
            ip_column = None
            port_column = None
            for column in reader.fieldnames:
                if 'ip' in column.lower():
                    ip_column = column
                elif 'port' in column.lower():
                    port_column = column
            if ip_column is None or port_column is None:
                print("IP or Port column not found in CSV.")
                return
            ip_list = [(row[ip_column], row[port_column]) for row in reader]
    except FileNotFoundError:
        print("Free_Proxy_List.csv not found. Please place that in the same folder as your program.")
        return

  
    progress_bar = tqdm(total=len(ip_list), desc="Validating Proxies", dynamic_ncols=True)

    
    valid_proxies = []
    threads = []
    for _ in range(20):
        thread = threading.Thread(target=validate_proxy, args=(ip_list, progress_bar, valid_proxies))
        thread.start()
        threads.append(thread)

    
    for thread in threads:
        thread.join()

    
    progress_bar.close()

    
    print("\nValid Proxies:")
    for ip, port in valid_proxies:
        print(f"\033[92m{ip}:{port}\033[0m")

    
    save = input("\nDo you want to save the valid proxies to MalakhProxy.csv? (yes/no): ").lower().strip()
    if save == 'yes':
        save_to_csv(valid_proxies)
        print("Valid proxies saved to MalakhProxy.csv")

if __name__ == "__main__":
    main()
