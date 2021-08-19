![github](https://user-images.githubusercontent.com/68802737/130044861-ac0a214a-3991-41af-97a8-9d4198c083a3.png)
you can change your network interface mac_address using system command 
but here is simple script to change mac address using python the scripts only 
use in linux terminal scripts it work with python 2.7 or 3 also 

1)  git clone  https://github.com/shreyas2511/Mac_Changer_Project.git
2)  cd Mac_Changer_Project
3)  sudo pip install -r requirement.txt
4)  sudo python Mac_Changer_1.1.py -h
5)  sudo python Mac_Changer_1.1.py -i eth0 -m 12:11:22:11:22:11


output of this program 

─$ sudo python Mac_Changer_1.1.py -i eth0 -m 12:11:22:11:22:11                                                                                                                             
 [sudo] password for kali: 
 [+]MAC address SUCCESSFULLY CHANGED
 [+]OLD_MAC=18:00:00:00:00:00
 [+]NEW_MAC=12:11:22:11:22:11

