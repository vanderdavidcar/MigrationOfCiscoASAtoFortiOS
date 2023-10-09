#! /usr/bin/env python3

from netmiko import ConnectHandler
import dev_connection
import re
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

start_time = datetime.now()

"""
Call function dev_connection that have all device and user information
to connect and collect
"""
net_connect = ConnectHandler(**dev_connection.iosv)
net_connect.enable()


cmd_std = net_connect.send_command(f"show run access-list | in standard")
show_run_std = cmd_std.splitlines()
print(show_run_std)

untrustintf = "UNTRUST-1/39.1505"

"""
Handle exception when does not have a specific match
"""

pattern_standsslsub = "access-list.(\S+).*\bstandard\b.permit.(\d.*)"
standsslasub = re.findall(pattern_standsslsub, cmd_std)
print(standsslasub)

pattern_standsslhst = "access-list.(\S+).*\bstandard\b.permit.host.(\S+)"
standsslahst = re.findall(pattern_standsslhst, cmd_std)

# Pattern to find only access-list extended IP
#pattern_any = "access-list (?P<name_rule>\S+) (?=.*\bpermit\b).+ip (?P<srcaddr>\S+) object-group (?P<dstaddr>\S+)"
#match_any = re.findall(pattern_any, cmd)
#
#
#pattern_objgr = "access-list (?P<name_rule>\S+) (?=.*\bpermit\b).+ip object-group (?P<srcaddr>\S+) object-group (?P<dstaddr>\S+)"
#match_objgr = re.findall(pattern_objgr, cmd)
#
#pattern_obj = "access-list (?P<name_rule>\S+) (?=.*\bpermit\b).+ip object (?P<srcaddr>\S+.) object (?P<dstaddr>\S+.)"
#match_obj = re.findall(pattern_obj, cmd)

#pattern_acc_std = "access-list (?P<name_rule>\S+) extended permit ip (?P<srcaddr>\S.+) (?P<dstaddr>any)"
#match_acc_std = re.findall(pattern_acc_std, cmd)





# Creating policy to permite network on SSL (Split tunnel)
def ip_access_standard():

    for i in standsslasub:
            if standsslasub:
                print(i)
            #print("edit 0")
            #print(f'set name "{i[0]}"')
            #print('set srcintf "Shared"')
            #print(f'set dstintf "{untrustintf}"')
            #print(f'set srcaddr "{i[1]}"')
            #print("set action accept")
            #print('set schedule "always"')
            #print('set service "ALL"')
            #print("set fsso disable")
            #print("next")


#ip_access_standard()
#
## Creating policy IP
#
#
#def ip_access_list_ext():
#
#    for i in match_acc_std:
#        print("edit 0")
#        print(f'set name "{i[0]}"')
#        print('set srcintf "Shared"')
#        print(f'set dstintf "{untrustintf}"')
#        if "any" in i[1]:
#            print('set srcaddr "all"')
#        else:
#            print(f'set srcaddr "{i[1]}"')
#        if "any" in i[2]:
#            print('set dstaddr "all"')
#        else:
#            print(f'set dstaddr "{i[2]}"')
#        print("set action accept")
#        print('set schedule "always"')
#        print('set service "ALL"')
#        print("set fsso disable")
#        print("next")
#    for i in match_any:
#        print("edit 0")
#        print(f'set name "{i[0]}"')
#        print('set srcintf "Shared"')
#        print(f'set dstintf "{untrustintf}"')
#        if "any" in i[1]:
#            print('set srcaddr "all"')
#        else:
#            print(f'set srcaddr "{i[1]}"')
#        print(f'set dstaddr "{i[2]}"')
#        print("set action accept")
#        print('set schedule "always"')
#        print('set service "ALL"')
#        print("set fsso disable")
#        print("next")
#    for i in match_objgr:
#        print("edit 0")
#        print(f'set name "{i[0]}"')
#        print('set srcintf "Shared"')
#        print(f'set dstintf "{untrustintf}"')
#        if "any" in i[1]:
#            print('set srcaddr "all"')
#        else:
#            print(f'set srcaddr "{i[1]}"')
#        print(f'set dstaddr "{i[2]}"')
#        print("set action accept")
#        print('set schedule "always"')
#        print('set service "ALL"')
#        print("set fsso disable")
#        print("next")
#    for i in match_obj:
#        print("edit 0")
#        print(f'set name "{i[0]}"')
#        print('set srcintf "Shared"')
#        print(f'set dstintf "{untrustintf}"')
#        if "any" in i[1]:
#            print('set srcaddr "all"')
#        else:
#            print(f'set srcaddr "{i[1]}"')
#        print(f'set dstaddr "{i[2]}"')
#        print("set action accept")
#        print('set schedule "always"')
#        print('set service "ALL"')
#        print("set fsso disable")
#        print("next")
#
#
#ip_access_list_ext()
#
## Pattern to find only access-list TCP
#tcp_pattern = re.compile(
#    r"access-list (?P<name_rule>\S+).+tcp (?P<svc>\w+) object-group (?P<src>\S+) object-group (?P<dst>\S+)"
#)
#tcp_patternip = re.compile(
#    r"access-list (?P<name_rule>\S+).+tcp (?P<svc>\S+) (?P<srcaddr>\d.{1,3}.{1,3}.{1,3}.{1,3} .{1,3}.{1,3}.{1,3}.{1,3}.{1,3}) (\w+.\w+ )(?P<dstaddr>\S+)"
#)
#
## Retrieve data access-list extended TCP
#match = tcp_pattern.search(cmd)
#match = re.findall(tcp_pattern, cmd)
#matchip = re.findall(tcp_patternip, cmd)
#
#
#def tcp_access_list():
#    # # Creating policy TCP ports on Fortigate
#    for i in match:
#        print("edit 0")
#        print(f'set name "{i[0]}"')
#        print('set srcintf "Shared"')
#        print(f'set dstintf "{untrustintf}"')
#        if "any" in i[2]:
#            print('set srcaddr "all"')
#        else:
#            print(f'set srcaddr "{i[2]}"')
#        print(f'set dstaddr "{i[3]}"')
#        print("set action accept")
#        print('set schedule "always"')
#        if "any" in i[1]:
#            print('set service "all"')
#        else:
#            print(f'set service "{i[1]}"')
#        print("set fsso disable")
#        print("next")
#
#    for i in matchip:
#        print("edit 0")
#        print(f'set name "{i[0]}"')
#        print('set srcintf "Shared"')
#        print(f'set dstintf "{untrustintf}"')
#        if "any" in i[2]:
#            print('set srcaddr "all"')
#        else:
#            print(f'set srcaddr "{i[2]}"')
#        print(f'set dstaddr "{i[4]}"')
#        print("set action accept")
#        print('set schedule "always"')
#        if "any" in i[1]:
#            print('set service "all"')
#        else:
#            print(f'set service "{i[1]}"')
#        print("set fsso disable")
#        print("next")
#
#
#tcp_access_list()
#
## Pattern to find only access-list extended DENY
#denypattern = re.compile(
#    r"access-list (?P<name_rule>\S+).+ deny (\w+.\w+) (?P<service>\S+) (?P<srcaddr>\S+) (\w+.\w+) (?P<dstaddr>\S+)"
#)
#
## Retrieve data access-list extended DENY
#denymatch = re.findall(denypattern, cmd)
#
#
#def deny_access_list():
#    # Creating policy DENY on Fortigate
#    for i in denymatch:
#        print("edit 0")
#        print(f'set name "{i[0]}"')
#        print('set srcintf "Shared"')
#        print(f'set dstintf "{untrustintf}"')
#        if "any" in i[3]:
#            print('set srcaddr "all"')
#        else:
#            print(f'set srcaddr "{i[3]}"')
#        print(f'set dstaddr "{i[5]}"')
#        print("set action deny")
#        print('set schedule "always"')
#        print(f'set service "{i[2]}"')
#        print("set fsso disable")
#        print("next")
#    print("end")
#
#
#deny_access_list()
#