
from scapy.all import sniff, IP, TCP, UDP, DNS

def sniff_packets(packet_count, protocol):
    if protocol == 'tcp':
        packets = sniff(filter="tcp", count=packet_count)
    elif protocol == 'udp':
        packets = sniff(filter="udp", count=packet_count)
    elif protocol == 'ip':
        packets = sniff(filter="ip", count=packet_count)
    elif protocol == 'dns':
        packets = sniff(filter="udp and port 53", count=packet_count)  # DNS packets
    else:
        packets = []
    return packets
