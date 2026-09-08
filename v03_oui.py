import ipaddress

# Byt ut mot det nät du vill räkna på.
text = "192.168.1.128/25"
#Provade 192.168.1.25/26 och denna.

# Modulen ipaddress gör räkningen åt dig.
net = ipaddress.ip_network(text, strict=False)

# Alla adresser du kan ge till en enhet.
usable = list(net.hosts())

print(f"Nät: {net.network_address}")
print(f"Nätmask: {net.netmask}")
print(f"Broadcast: {net.broadcast_address}")
print(f"Första adress: {usable[0]}")
print(f"Sista adress: {usable[-1]}")
print(f"Antal enheter: {len(usable)}")
