
# Disclaimer
I'm not a dev yet, this is NOT fancy code. It does work (for me at least!) though. You can seriously mess up your producition environment with my scripts if you don't know what you're doing. I take no responsibility for that :)</br>

## Dependencies: Install the requirements to have all dependencies used

pip install -r requirements.txt

## Credentials to connect in devices

To protect credentials leaking, create a .env file with variables USERNAME/PASSWORD that will be used to connect on devices (USER_LAB/PASS_LAB).</br>

.env file</br>
change only the userame and password in .env file</br>
e.g USER_LAB=vanderson PASS_LAB=cisco</br>

dev_connection</br>
A module imported in files ".py" which needed a credentials to connect on devices.

Change only IP address in line 13</br>
nb_api = ["192.168.20.1"]</br>

## Modules

### script_01_rules_csv.py
</b>Using regex to find rules of specific network and creating .csv file. Can be using together jinja template for create a script </br></b>

### script_02_files_addrgrp.py
</b>Used to create only prefix-lenghts (subnet and host) into object-group </br></b>

### script_03_addrgrp_object.py
</b>After created all list of IP address in module above, use that function to create address group on FortiOS using external file</br></b>

### script_04_port_services.py 
</b>Used to create all services objects in Cisco ASA that have a port mentioned in regex pattern "port-object.eq (\S+)</br></b>

### script_05_tcp_services.py
</b>Used to create all services objects in Cisco ASA using many regex pattern to find TCP/UDP ports" (\S+)</br></b>

### script_06_object_addr.py
</b>Used to create all IP Addresses founded on objects using host, subnet, range, network </br></b>

### script_07_route_table.py
</b>Looking for all network route configuration and convert them </br></b>

### script_08_collect_intf.py
</b>Collect all interfaces on Cisco ASA</br></b>