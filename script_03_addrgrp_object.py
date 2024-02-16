from netmiko import ConnectHandler
import dev_connection
import re
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()

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

"""
Module to use external file created by function create_external_file() on script_files_addrgrp.py to create address group on FortiOS
"""

def addrgrp():
    print('config firewall addrgrp')
    for hosts in show_objgrp:
        # Create objects address group name
        if grpname_regex.search(hosts):
            grpname = hosts.split()[2]
            try:
                with open(f'output_{grpname}.txt', 'r') as fa:
                    ipadd = fa.read().splitlines()

                    print(f'edit "{grpname}"')
                    print(f'append member  {ipadd}')
                    print('next')
            except:
                print("Not found")
    print("end")
addrgrp() 

