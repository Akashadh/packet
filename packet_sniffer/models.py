# packet_sniffer/models.py

from django.db import models

class Packet(models.Model):
    protocol = models.CharField(max_length=50)
    source_ip = models.CharField(max_length=50)
    destination_ip = models.CharField(max_length=50)
    source_port = models.IntegerField()
    destination_port = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    summary = models.TextField()

    def __str__(self):
        return f"{self.protocol} Packet ({self.source_ip}:{self.source_port} -> {self.destination_ip}:{self.destination_port})"
