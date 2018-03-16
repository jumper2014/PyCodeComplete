# coding=utf-8

import pcap
import dpkt

pc = pcap.pcap('en0')  # 注，参数可为网卡名，如eth0

pc.setfilter('tcp port 80')    # 2.设置监听过滤器

for ts, pkt in pc:
    eth = dpkt.ethernet.Ethernet(pkt)
    ip = eth.data
    print ts
    # udp = ip.data
    # dns = dpkt.dns.DNS(udp.data)