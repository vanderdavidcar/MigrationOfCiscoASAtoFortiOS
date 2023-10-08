## Dependencies: Install the requirements to have all dependencies used

pip install -r requirements.txt

## Credentials to connect in devices

- To protect credentials leaking, create a .env file with variables USERNAME/PASSWORD that will be used to connect on devices (USER_LAB/PASS_LAB).

.env file</br>
change only the userame and password in .env file</br>
e.g USER_LAB=vanderson PASS_LAB=cisco</br>

dev_connection</br>
A module imported in files ".py" which needed a credentials to connect on devices.

- Change only IP address in line 13</br>
nb_api = ["192.168.20.1"]</br>

# Modules

</b>Collect all interfaces on Cisco ASA</br></b>
script_collect_intf.py

</b>Looking for all network route configuration and convert them </br></b>
script_route_table.py

</b>Looking for all IP address and create them as an address object in FortiOS </br></b>
script_object_addr.py

</b>Looking for all access-list extended, standard, deny... and converting to FortiOS rules</br></b>
script_rules.py