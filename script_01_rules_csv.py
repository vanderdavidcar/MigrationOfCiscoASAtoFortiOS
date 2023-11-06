from netmiko import ConnectHandler
import dev_connection
import re
from dotenv import load_dotenv
from datetime import datetime
import os 
import time
import csv
load_dotenv()

start_time = datetime.now()
print(f"{start_time}")

"""
Call function dev_connection that have all device and user information to connect and collect
"""
net_connect = ConnectHandler(**dev_connection.iosv)
net_connect.enable()  # Needed beacause command below is necessary privilege 15 to be executed
term_pager0 = net_connect.send_command("terminal pager 0")


"""
Function to find object-group names used in access-list Internet-ACL to looking for source IPs
"""


# Command executed on Cisco ASA to find a costumer configuration
shrun = net_connect.send_command(f"show running-config | in 201.31.5")
any4 = "access-list Internet-ACL.*tcp.(\S+).host.(\S+).eq.(\S+)"
any4_regex = re.findall(any4, shrun)

host = "access-list.*tcp.host.(\S+).host.(\S+).eq.(\S+)"
host_regex = re.findall(host,shrun)

object_group = "access-list.*object-group.(\S+).host.(\S+).eq.(\S+)"
regex_grp = re.findall(object_group, shrun)

for grp in any4_regex:
    print(f"\n{grp}")
    
    with open('all_any4.csv', 'a') as out_file:
        writer = csv.writer(out_file)
        #writer.writerow(('source', 'destination', 'port'))
        writer.writerow(grp)

for grp in regex_grp:
    print(f"\n{grp}")
    
    with open('all_grpaddres.csv', 'a') as out_file:
        writer = csv.writer(out_file)
        #writer.writerow(('source', 'destination', 'port'))
        writer.writerow(grp)

for grp in host_regex:
    print(f"\n{grp}")
    
    with open('all_souce_hosts.csv', 'a') as out_file:
        writer = csv.writer(out_file)
        #writer.writerow(('source', 'destination', 'port'))
        writer.writerow(grp)