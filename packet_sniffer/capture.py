
from scapy.all import sniff, IP, TCP, UDP, DNS
from .models import Packet


def sniff_packets(packet_count, protocol):
    if protocol == 'tcp':
        packets = sniff(filter="tcp", count=packet_count)
    elif protocol == 'udp':
        packets = sniff(filter="udp", count=packet_count)
    elif protocol == 'ip':
        packets = sniff(filter="ip", count=packet_count)
    elif protocol == 'dns':
        packets = sniff(filter="udp and port 53", count=packet_count)  
        packets = []
    return packets


def save_packets(packet_count, protocol):
    # packets = sniff(filter=protocol, count=packet_count)

    if protocol == 'dns':
        packets = sniff(filter="udp and port 53", count=packet_count)  # DNS packets
    else:
        packets = sniff(filter=protocol, count=packet_count) 

    for packet in packets:
        try:
            new_packet = Packet(
                protocol=protocol.upper(),
                source_ip=str(packet[0][1].src),
                destination_ip=str(packet[0][1].dst),
                source_port=int(packet[0][2].sport),
                destination_port=int(packet[0][2].dport),
                summary=packet.summary()
            )
            new_packet.save()
        except Exception as e:
            print(f"Error saving packet: {e}")