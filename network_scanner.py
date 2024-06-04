import scapy.all as scapy
from colorama import Fore
from scapy.all import srp, Ether, ARP, conf
import json




def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1)[0]
    print(Fore.LIGHTBLUE_EX + "IP\t\t\tMAC Address\n----------------------------------------------------------")
    client_list = []
    
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        client_list.append(client_dict)
        print(Fore.LIGHTGREEN_EX + element[1].psrc + "\t\t" + element[1].hwsrc)
        json.dump(client_list, open("ipMac.json", "w"))
        client_list.sort(key=lambda y: sorted(y.keys()))
scan("192.168.0.104/24")
