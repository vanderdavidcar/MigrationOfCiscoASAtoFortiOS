#! /usr/bin/env python3
from netmiko import ConnectHandler
import dev_connection
import re
from dotenv import load_dotenv
from datetime import datetime
import time, os
load_dotenv()
from collections import OrderedDict


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

# service-object ICMP|6
serv_object_icmp_pattern = "service-object icmp6* (\S+)"
serv_object_icmp_regex = re.compile(serv_object_icmp_pattern)

# service-object TCP
serv_object_tcp_pattern = "service-object.tcp-udp.destination.eq.(\S+)|service-object.tcp.destination.eq.(\S+)"
serv_object_tcp_regex = re.compile(serv_object_tcp_pattern)

# service-object UDP
serv_object_udp_pattern = "service-object.udp (\S+)|service-object.udp.destination.eq.(\S+)"
serv_object_udp_regex = re.compile(serv_object_udp_pattern)

# service-object OBJECT
serv_object_obj_pattern = "service-object object (\S+)"
serv_object_obj_regex = re.compile(serv_object_obj_pattern)


for row in show_objgrp:
    # Create objects address group         
    if grpname_regex.search(row):
        grpname = row.split()[2]
        #print(f"\n{grpname}")
    if serv_object_tcp_regex.search(row):
        service_object = row.split()[4]
        service_tcp_grp = []
        service_tcp_grp.append(service_object)
        #print(service_tcp_grp)
        for i in service_tcp_grp:
            """
            Put all founded TCP/PORT in FortiOS script
            """
            for i in service_tcp_grp:
                port = f'TCP_{i}'
                print(f"edit {port.upper()}")

                # Regex to find only decimal ports instead of texts
                num_pattern = "(\d+)"
                num_regex = re.compile(num_pattern)

                if num_regex.search(i):
                    print(f"set tcp-portrange {i}")
                    print(f"set udp-portrange {i}")

                # Conditional to find ports configured by name like SSH, FTP, DOMAIN...and convert all of them in port numbers on FortiOS script
                if "echo" in i:
                    print(f"set tcp-portrange icmp")
                    print(f"set udp-portrange icmp")
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


    if serv_object_icmp_regex.search(row):
        service_object = row.split()[2]
        service_icmp_grp = []
        service_icmp_grp.append(service_object)
        #print(service_icmp_grp)
        for i in service_icmp_grp:
            """
            Put all founded TCP/PORT in FortiOS script
            """
            for i in service_icmp_grp:
                port = f'TCP_{i}'
                print(f"edit {port.upper()}")

                # Regex to find only decimal ports instead of texts
                num_pattern = "(\d+)"
                num_regex = re.compile(num_pattern)

                if num_regex.search(i):
                    print(f"set tcp-portrange {i}")
                    print(f"set udp-portrange {i}")

                # Conditional to find ports configured by name like SSH, FTP, DOMAIN...and convert all of them in port numbers on FortiOS script
                if "echo" in i:
                    print(f"set tcp-portrange icmp")
                    print(f"set udp-portrange icmp")
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


    if serv_object_obj_regex.search(row):
        serv_object = row.split()[2]
        service_obj_grp = []
        service_obj_grp.append(serv_object)
        #print(service_obj_grp)
        for i in service_obj_grp:
            """
            Put all founded TCP/PORT in FortiOS script
            """
            for i in service_obj_grp:
                port = f'TCP_{i}'
                print(f"edit {port.upper()}")

                # Regex to find only decimal ports instead of texts
                num_pattern = "(\d+)"
                num_regex = re.compile(num_pattern)

                if num_regex.search(i):
                    print(f"set tcp-portrange {i}")
                    print(f"set udp-portrange {i}")

                # Conditional to find ports configured by name like SSH, FTP, DOMAIN...and convert all of them in port numbers on FortiOS script
                if "echo" in i:
                    print(f"set tcp-portrange icmp")
                    print(f"set udp-portrange icmp")
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


    if serv_object_udp_regex.search(row):
        service_object = row.split()[4]
        service_udp_grp = []
        service_udp_grp.append(service_object)
        #print(service_udp_grp)
        for i in service_udp_grp:
            """
            Put all founded TCP/PORT in FortiOS script
            """
            for i in service_udp_grp:

                # Regex to find only decimal ports instead of texts
                num_pattern = "(\d+)"
                num_regex = re.compile(num_pattern)

                if num_regex.search(i):
                    print(f"set tcp-portrange {i}")
                    print(f"set udp-portrange {i}")

                # Conditional to find ports configured by name like SSH, FTP, DOMAIN...and convert all of them in port numbers on FortiOS script
                if "echo" in i:
                    print(f"set tcp-portrange icmp")
                    print(f"set udp-portrange icmp")
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
                
                ## Remove special characteres to use data on address group
                #delcharactere = f"sort -u fortios_tcp_ports.cfg"
                #cmdFile = os.system(delcharactere)
                #time.sleep(0.5)