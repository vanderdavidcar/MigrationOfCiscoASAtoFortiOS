# https://stackoverflow.com/questions/45514792/loop-csv-content-in-a-jinja2-template

from io import StringIO
from jinja2 import Template
from itertools import groupby
from operator import itemgetter
from csv import DictReader
import csv
import os
import time

"""
Using external .csv file with all informations retrieved by Cisco ASA as SOURCE, DESTINATION and PORT, when I a was looking for that solution I found the link above and adapted by my code.
"""



# Jinja template to use external file .csv
tmpl = '\nedit 0\n'
tmpl += 'set name ALLOWED-to-{{destination}}\n'
tmpl += 'set srcintf "port1"\n'
tmpl += 'set dstintf "port2"\n'
tmpl += 'set srcaddr "all"\n'
tmpl += 'set dstaddr "{{destination}}"\n'
tmpl += 'set action accept\n'
tmpl += 'set schedule "always"\n'
tmpl += 'set service "{{services | join(",")|upper}}"\n'
tmpl += 'set fsso disable\n'
tmpl += 'next\n'

template = Template(tmpl)

# .csv file
with open(f"all_any4.csv") as file:
    rows = DictReader(file)
    for destination, groups in groupby(rows, key=itemgetter('destination')):
        services = (row['port'] for row in groups)
        output = template.render(destination=destination, services=services)
        print(output)
        fortiosFile = open(f'/home/lab/fortios_rules.cfg', "a")
        fortiosFile.write(output)