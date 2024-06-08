#!/usr/bin/env python3
import argparse
import subprocess
import re

def get_arguments():
    parser = argparse.ArgumentParser(description="Herramienta para cambiar la dirección MAC de una interfaz de red en linux")
    parser.add_argument("-i", "--interface", required=True, dest="interface", help="Nombre de la interfaz de red")
    parser.add_argument("-m", "--mac", required=True, dest="mac_address", help="Nueva dirección MAC para la interfaz de red")
    return parser.parse.args()

def is_valid_input(interface, mac_address):
    is_valid_mac_address = re.match(r'^([A-Fa-f0-9]{2}[:]){5}[A-Fa-f0-9]{2}$', mac_address)
    
    return is_valid_mac_address

def change_mac_address(interface, mac_address):
    if is_valid_input(interface, mac_address):
        subprocess.run(['ifconfig', interface, 'down'])
        subprocess.run(['ifconfig', interface, 'hw', "ether", mac_address])
        subprocess.run(['ifconfig', interface, 'up'])
        print("La mac ha sido cambiada!")
    else:
        print("Hubo un error en los datos de interfaz o mac address")
def main():
    args=get_arguments()
    change_mac_address(args.interface, args.mac_address)

if __name__=='__main__':
    main()
