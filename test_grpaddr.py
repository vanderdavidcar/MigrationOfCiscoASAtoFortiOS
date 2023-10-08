from netmiko import ConnectHandler
import dev_connection
import re
from dotenv import load_dotenv
from datetime import datetime
from ipaddress import IPv4Network
import ipaddress
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


def create_pfx_lenght_32():
    
    """
    Find all object groups to use 
    """
    
    # Convert address objects in Cisco ASA to Fortigate object group
    print('Conversão de IP Address objetos no Cisco Asa para Fortigate')                        
    for hosts in show_objgrp:
        # Create objects address group name
        if grpname_regex.search(hosts):
            grpname = hosts.split()[2]
            print(f'\n!{grpname}')
        
        # Create many subnet prefix lenghts
        if regex_subnets.search(hosts):
            netobject2 = hosts.split()[1:]
            newgrp = []
            newgrp.append(netobject2)
                #    # Loop with new list
            for i in newgrp:
                subpfx = f'{i[0]}/{i[1]}' # subnet with prefix length
                net = IPv4Network(subpfx)
                subnet = " ".join(i)
                print(f'edit {net.network_address}/{net.prefixlen}')
                print(f'set subnet {subnet}')
                print("next")
        
        # Create only prefix lenght /32
        if regex_prx32.search(hosts):
            netobject1 = hosts.split()[2]
            newgrp = []
            newgrp.append(netobject1)
 
            # Loop with new list
            for i in newgrp:
                # Find only hosts with prefix lenght 32
                net = IPv4Network(i)
                print(f'{net.network_address}/{net.prefixlen}')
                print(f'edit {net.network_address}/{net.prefixlen}')
                print(f'set subnet {net.network_address} {net.netmask}')
                print("next")
    

                #if grpname:
                #    print(f'edit "{grpname}"')
                #    print(f'append member "{net.network_address}/{net.prefixlen}"')
                #    print('next')
                

        
create_pfx_lenght_32()

