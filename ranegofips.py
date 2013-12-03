# Author : Avinash <a@vlabs.ac.in>
# 

import socket
import struct 

""" This module takes a valid subnet and returns the range of valid IPs in that subnet """

def ips_in_subnet(subnet=""):
    subnet = "10.1.10.0/24".split('/')
    ip = subnet[0]
    ipinbinary = ''
    #print '.'.join([bin(int(x)+256)[3:] for x in ip.split('.')])
    for each in subnet[0].split('.'):
        #ipinbinary += str(len(str(bin(int(each)+256)[2:])))
        ipinbinary += bin(int(each)+256)[2:]
    return int(ipinbinary)
#dec_to_bin = lambda ip4: bin(struct.unpack('!I', socket.inet_pton(socket.AF_INET, ip4))[0])
#print dec_to_bin("192.168.65.72")

print ips_in_subnet() & 11111111111111111111111100000000