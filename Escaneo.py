from scapy.all import *
import socket



def ip_scan():
    print("---------") 
    ip=0
    hostname = socket.gethostname()                 
    IPAddr = str(socket.gethostbyname(hostname))    
    dd=(IPAddr[len(IPAddr)-3:])
    x=dd.find(".")
    match x:
        case -1:
            IPAddr=IPAddr[:len(IPAddr)-3]
            IPAddr=IPAddr+"1/24"
        case 0:
            IPAddr=IPAddr[:len(IPAddr)-2]
            IPAddr=IPAddr+"1/24"
        case 1:
            IPAddr=IPAddr[:len(IPAddr)-1]
            IPAddr=IPAddr+"1/24"
    ip=IPAddr
    range_ip= ARP(pdst=ip)
    broadcast=Ether(dst="ff:ff:ff:ff:ff:ff")
    final_packet=broadcast/range_ip
    res= srp(final_packet, timeout=2, verbose=False)[0]
    for n in res:
        print("[+] HOST: {}     MAC: {}".format(n[1].psrc, n[1].hwsrc)) 
        