from netmiko import ConnectHandler
import dev_connection
import re, os
from dotenv import load_dotenv
from datetime import datetime
from ipaddress import IPv4Network
import time
load_dotenv()
import json
start_time = datetime.now()

"""
Call function dev_connection that have all device and user information to connect and collect
"""
net_connect = ConnectHandler(**dev_connection.iosv)
net_connect.enable() # Needed beacause command below is necessary privilege 15 to be executed
term_pager0 = net_connect.send_command('terminal pager 0')

cmd = net_connect.send_command(f'show running-config object-group')
show_objgrp = cmd.splitlines()

# this regex is to match for all object-group on firewall Cisco ASA
grpname_pattern = "object-group network (\S+)"
grpname_regex = re.compile(grpname_pattern)

netobj_pattern = "network-object host (\d+)"
regex_prx32 = re.compile(netobj_pattern)

netobj_pattern2 = "network-object object (\d.+)"
regex_obj = re.compile(netobj_pattern2)

netobj_pattern3 = "network-object (\d.+)"
regex_subnets = re.compile(netobj_pattern3)


def create_external_file():
    
    """
    Find all object groups to use 
    """
    
    # Convert address objects in Cisco ASA to Fortigate object group
    print('Conversão de IP Address objetos no Cisco Asa para Fortigate')                        
    for hosts in show_objgrp:
        # Create objects address group name
        if grpname_regex.search(hosts):
            grpname = hosts.split()[2]
            print(f'\n{grpname}')
        
        # Create many subnet prefix lenghts
        if regex_subnets.search(hosts):
            netobject2 = hosts.split()[1:]
            newgrp = []
            newgrp.append(netobject2)
            
            # Loop with new list
            for i in newgrp:
                subpfx = f'{i[0]}/{i[1]}' # subnet with prefix length
                net = IPv4Network(subpfx)
                print(f'{net.network_address}/{net.prefixlen}')
                subnet = f'{net.network_address}/{net.prefixlen}'
                ip = "".join(str(subnet))
                new_sub = []
                new_sub.append(ip)
        
                with open(f"output_{grpname}.txt", "a") as f:
                    f.write(f'{new_sub}')
                    f.close()
        
        # Create only prefix lenght /32
        if regex_prx32.search(hosts):
            netobject1 = hosts.split()[2]
            newgrp = []
            newgrp.append(netobject1)
 
            # Loop with new list
            for i in newgrp:
                # Find only hosts with prefix lenght 32
                net = IPv4Network(i)
                prefix32 = f'{net.network_address}/{net.prefixlen}'
                ip = "".join(str(prefix32))
                new_ips = []
                new_ips.append(ip)
        
                with open(f"output_{grpname}.txt", "a") as f:
                    f.write(f'{new_ips}')
                    f.close()
                
                # Remove special characteres to use data on address group
                delcharctere = f"sed -i 's/\[/ /g' output_{grpname}.txt && sed -i 's/\]//g' output_{grpname}.txt"
                cmdFile = os.system(delcharctere)
                time.sleep(1)
                       
create_external_file()