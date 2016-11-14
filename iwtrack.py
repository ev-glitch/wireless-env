#!/usr/bin/python

import subprocess
import time

# Add specification for Device class - holds a scan record for a given addr.
class Device(object):
    def __init__(self, addr):
        self.hw_addr = addr
#        self.firstseen = 
#        self.lastseen = 
#    def add_element(self, el):

Cells = {}

def new_scan ():
    scan_result = subprocess.check_output(["iwlist", "scan"])
    return scan_result

def parse_scan (scan_string):
    scan_lines = scan_string.splitlines()
    for l in scan_lines:
        line = l.strip().split()
        if not line:
            break
        #print line.strip()
        if "Cell" in line[0]:
            if not line[-1] in Cells:
                Cells[line[-1]] = 1
                print "New cell ", line[-1]
            


if __name__ == "__main__":
    # check permissions. If not root, kick warning

    while(True):
        print "starting new scan: "
        result = new_scan()
        parse_scan(result)
        time.sleep(1)
