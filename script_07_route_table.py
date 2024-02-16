#! /usr/bin/env python3

from netmiko import ConnectHandler
import dev_connection
import re
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

start_time = datetime.now()

#customer = "ITAU"
"""
Call function dev_connection that have all device and user information to connect and collect
"""
net_connect = ConnectHandler(**dev_connection.iosv)
net_connect.enable()  # Needed beacause command below is necessary privilege 15 to be executed
show_route = net_connect.send_command(f"show route")

# Regex pattern to find exatly subnets

route_regex = "S....(\S+).(\S+).*via.(\d..{1,3}.{1,3}.{1,3}.)"
route_match = re.findall(route_regex,show_route)
print(route_match)

def create_routing_table():
    print("\nconfig router static")
    for i in route_match:
        # Create objects address group for current route
        print("edit 0")
        print(f"set dst {i[0]} {i[1]}")
        print(f"set gateway {i[2]}")
        print(f'set device "TRUST-1/38.123"')
        print("next")
    print("end")


create_routing_table()