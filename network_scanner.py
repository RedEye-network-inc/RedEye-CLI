import scapy.all as scapy
from colorama import Fore
import ipaddress

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=0.1, verbose=False)[0]

    client_list = []

    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        client_list.append(client_dict)

    return client_list

def print_result(result_list):
    print(Fore.LIGHTBLUE_EX + "IP\t\t\tMAC Address\n----------------------------------------------------------")
    for client in result_list:
        print(client["ip"] + "\t\t" + client["mac"])

def get_ip_range():
    while True:
        ip_range = input(Fore.MAGENTA + "╔═════$ Ingrese el rango de IP de la red que desea escanear (ej. 192.168.1.0/24): " + Fore.RESET)
        if ip_range:
            try:
                network = ipaddress.ip_network(ip_range, strict=False)
                return network
            except ValueError:
                print(Fore.LIGHTRED_EX + "═════╝ Rango de IP inválido." + Fore.RESET)
        else:
            print(Fore.LIGHTRED_EX + "═════╝ Debe ingresar un rango de IP válido." + Fore.RESET)

def scan_network(network):
    result = []
    for ip in network.hosts():
        result.extend(scan(str(ip)))
    return result

network = get_ip_range()
result = scan_network(network)
print_result(result)
