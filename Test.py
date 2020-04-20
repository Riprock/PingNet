from scapy.all import *
def cmd_mon(pkt):
    if str(pkt.getlayer(ICMP).type) == "0":
            print(f'Packet:\n {pkt.show()}')
            print(f'ICMP Type: {pkt.getlayer(ICMP).type}')
            print(f'Source IP:{pkt.getlayer(IP).src}')


conf.sniff_promisc = 1
sniff(filter="icmp", prn=cmd_mon)
