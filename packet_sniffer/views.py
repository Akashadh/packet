# packet_sniffer/views.py

from django.shortcuts import render
from .capture import sniff_packets
from .capture import save_packets
from .models import Packet



def home(request):
    if request.method == 'POST':
        packet_count = int(request.POST.get('packet_count', 10))  # Default to 10 packets
        protocol = request.POST.get('protocol', 'tcp')  # Default protocol is TCP


        # Capture and save packets
        save_packets(packet_count, protocol)

        # Fetch saved packets from database
        packets = Packet.objects.all().order_by('-timestamp')[:packet_count]
        data = {
            'packets': packets, 
             'protocol': protocol
        }
        
        return render(request, 'packet_sniffer/result.html', data)
    
    return render(request, 'packet_sniffer/home.html')