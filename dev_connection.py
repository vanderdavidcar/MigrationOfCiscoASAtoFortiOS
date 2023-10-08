"""
Function Netmiko Connection
"""
from dotenv import load_dotenv
load_dotenv()
import os

username = os.getenv("USERNAME")
passwd = os.getenv("PASSWD")
secret = os.getenv("SECRET")

# Device connection
nb_api = ["172.20.201.31"]

def netmiko_asa(ip):
    return {
            'device_type': 'cisco_ios',
            'ip': ip,
            'username': username,
            'password': passwd,
            'secret': passwd
             }
# Netmiko connection
for ipadd in nb_api:
    iosv = netmiko_asa(str(ipadd))
    print(f"Hostname: {str(ipadd)}\n")