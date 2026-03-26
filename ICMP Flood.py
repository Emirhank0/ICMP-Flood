from scapy.all import IP, ICMP, send

hedef_ip     = "127.0.0.1"
paket_sayisi = 100

paket = IP(dst=hedef_ip) / ICMP()

for i in range(paket_sayisi):
    send(paket)
    print(f"  [{i+1}/{paket_sayisi}] paket gönderildi → {hedef_ip}")

print("\nTamamlandı!")
