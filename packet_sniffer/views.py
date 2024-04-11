# packet_sniffer/views.py

from django.shortcuts import render
from .capture import sniff_packets

def home(request):
    if request.method == 'POST':
        packet_count = int(request.POST.get('packet_count', 10))  # Default to 10 packets
        protocol = request.POST.get('protocol', 'tcp')  # Default protocol is TCP
        packets = sniff_packets(packet_count, protocol)
        return render(request, 'packet_sniffer/result.html', {'packets': packets})
    return render(request, 'packet_sniffer/home.html')
