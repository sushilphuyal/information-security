import ipaddress

IP_Addr = ipaddress.ip_interface(input('Enter IP address in IP/Mask Form : '))

Net_Addr = IP_Addr.network
pref_len = IP_Addr.with_prefixlen
Mask = IP_Addr.with_netmask
wildcard = IP_Addr.hostmask
broadcast_address = Net_Addr.broadcast_address

print('Network Address : ', str(Net_Addr).split('/')[0])
print('Broadcast Address : ' , broadcast_address)
print('CIDR Notation : ', pref_len.split('/')[1])
print('Subnet Mask : ', Mask.split('/')[1])
print('Wildcard Mask : ' , wildcard)
print('First IP : ' , list(Net_Addr.hosts())[0])
print('Last IP : ' , list(Net_Addr.hosts())[-1])