from netmiko import ConnectHandler
import dev_connection
import re
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

start_time = datetime.now()

"""
Creation of all IP Addresses founded on objects using regex
"""

# Call function dev_connection that have all device and user information to connect and collect
net_connect = ConnectHandler(**dev_connection.iosv)
net_connect.enable()  # Needed beacause command below is necessary privilege 15 to be executed
term_pager0 = net_connect.send_command("terminal pager 0")
# Command executed on Cisco ASA to find a costumer configuration
show_run = net_connect.send_command(f"show running-config object")

def create_object_addr():

    # this regex is to match for object network, host, subnet and range.
    obj_pattern = "network (\S+)"
    hst_pattern = "host (\S+)"
    sub_pattern = "subnet (\S+)"
    rng_pattern = "range (\S.+)"

    # create a regex object with the pattern in place.
    regex_nam = re.compile(obj_pattern)
    regex_hst = re.compile(hst_pattern)
    regex_sub = re.compile(sub_pattern)
    regex_rng = re.compile(rng_pattern)

    # initialize this list to collect interface information.

    print(f"\nconfig firewall address")
    for line in show_run.splitlines():
        ## check for interface names only
        if regex_nam.search(line):
            name = line.split()[2]
            print(f"edit {name}")
        if regex_hst.search(line):
            host = line.split()[1]
            print(f"set subnet {host} 255.255.255.252")
            print("next")
        if regex_sub.search(line):
            sub = line.split()[1:]
            subnet = " ".join(sub)
            print(f'set subnet {subnet}')
            print("next")
        if regex_rng.search(line):
            range = line.split()[1:]
            print('set type iprange')
            print(f'set start-ip {range[0]}')
            print(f'set end-ip {range[1]}')
            print("next")
    print("end")


create_object_addr()
