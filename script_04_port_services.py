#! /usr/bin/env python3
from netmiko import ConnectHandler
import dev_connection
import re
from dotenv import load_dotenv
from datetime import datetime
import time, os
load_dotenv()


# To have a logging only for Netmiko connection
import logging

logging.basicConfig(filename="netmiko_global.log", level=logging.DEBUG)
logger = logging.getLogger("netmiko")

start_time = datetime.now()


"""
Call function dev_connection that have all device and user information to connect and collect
"""
net_connect = ConnectHandler(**dev_connection.iosv)
net_connect.enable()
term_pager0 = net_connect.send_command('terminal pager 0')
showrun = net_connect.send_command(f"show object-group service")
show_objgrp = showrun.splitlines()

# this regex is to match for all object-group on firewall Cisco ASA
grpname_pattern = "object-group service (?P<grpname>\S+)"
grpname_regex = re.compile(grpname_pattern)





for line in show_objgrp:
    # prot-object
    port_object_pattern = "port-object.eq (\S+)"
    port_object_regex = re.compile(port_object_pattern)

    # Create objects address group         
    if grpname_regex.search(line):
        grpname = line.split()[2]
        #print(f"\n{grpname}")
    if port_object_regex.search(line):
        port_object = line.split()[2]
        portgrp = []
        portgrp.append(port_object)
        #print(portgrp)
        """
        Put all founded TCP/PORT in FortiOS script
        """
        for i in portgrp:
            port = f'TCP_{i}'
            print(f"edit {port.upper()}")

            # Regex to find only decimal ports instead of texts
            num_pattern = "(\d+)"
            num_regex = re.compile(num_pattern)
    
            if num_regex.search(i):
                print(f"set tcp-portrange {i}")
                print(f"set udp-portrange {i}")
        
            # Conditional to find ports configured by name like SSH, FTP, DOMAIN...and convert all of them in port numbers on FortiOS script
            if "ssh" in i:
                print(f"set tcp-portrange 22")
                print(f"set udp-portrange 22")
            if i == "www":
                print(f"set tcp-portrange 80")
                print(f"set udp-portrange 80")
            if i == "nfs":
                print(f"set tcp-portrange 2049")
                print(f"set udp-portrange 2049")
            if i == "https":
                print(f"set tcp-portrange 443")
                print(f"set udp-portrange 443")
            if i == "ftp":
                print(f"set tcp-portrange 21")
                print(f"set udp-portrange 21")
            if i == "ftp-data":
                print(f"set tcp-portrange 20")
                print(f"set udp-portrange 20")
            if i == "sqlnet":
                print(f"set tcp-portrange 1521")
                print(f"set udp-portrange 1521")
            if i == "ntp":
                print(f"set tcp-portrange 123")
                print(f"set udp-portrange 123")
            if i == "telnet":
                print(f"set tcp-portrange 23")
                print(f"set udp-portrange 23")
            if i == "snmp":
                print(f"set tcp-portrange 161")
                print(f"set udp-portrange 161")
            if i == "snmptrap":
                print(f"set tcp-portrange 162")
                print(f"set udp-portrange 162")
            if i == "domain":
                print(f"set tcp-portrange 53")
                print(f"set udp-portrange 53")
            print("next")


        #my_dictionary = {}
        #my_dictionary['name'] = grpname,
        #my_dictionary['service'] = portgrp
        #print(my_dictionary)
