#[+]installation module
#[+]developer:-shreyas zadge
#[+]script_version:-1.1
from os import name
import subprocess
import optparse
import re 
#[+]check Mac really change or not
def check_result(interfaces):
    results = subprocess.check_output(["ifconfig",interfaces])
    mac_results =re.search("\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(results))
    return mac_results.group(0)
#[+]getting mac address and interface from outside a program simple meaning 
def get_mac_outside():
    parse =optparse.OptionParser()
    parse.add_option("-i","--interface",dest="interface",help="select interface do you want to change")
    parse.add_option("-m","--mac",dest="mac",help="write mac address to change")
    (options,arguments)=parse.parse_args()
    return options
#[+]main mac changer program
def mac_changer(interface,new_mac):
    subprocess.call(["sudo","ifconfig",interface,"down"])
    subprocess.call(["sudo","ifconfig",interface,"hw","ether",new_mac])
    subprocess.call(["sudo","ifconfig",interface,"up"])
#[+]Main_Program
if __name__=='__main__':
    try:
        options = get_mac_outside()
        results1=check_result(options.interface)
        print("[+]MAC address SUCCESSFULLY CHANGED")
        print("[+]OLD_MAC="+str(results1))
        mac_changer(options.interface,options.mac)
        results2=check_result(options.interface)
        print("[+]NEW_MAC="+str(results2))
    except Exception as ex :
        print(ex)    
