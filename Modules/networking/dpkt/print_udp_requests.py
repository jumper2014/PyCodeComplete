#!/usr/bin/env python
# coding=utf-8
"""
analysis big *.pcap file with python
to quickly locate specified udp request and response
"""

import datetime
import time
import dpkt
from dpkt.udp import UDP


def timestamp2datetime(timestamp, convert_to_local=False):
    """
    Converts UNIX timestamp to a datetime object.
    """
    if isinstance(timestamp, (int, long, float)):
        dt = datetime.datetime.utcfromtimestamp(timestamp)
        if convert_to_local:
            dt = dt + datetime.timedelta(hours=8)   # default china time zone
        return dt
    return timestamp


def print_udp_requests(pcap):
    """Print out information about each packet in a pcap

       Args:
           pcap: dpkt pcap reader object (dpkt.pcap.Reader)
    """
    # For each packet in the pcap process the contents
    for timestamp, buf in pcap:

        # Unpack the Ethernet frame (mac src/dst, ethertype)
        eth = dpkt.ethernet.Ethernet(buf)

        # Make sure the Ethernet data contains an IP packet
        if not isinstance(eth.data, dpkt.ip.IP):
            print('Non IP Packet type not supported %s\n' % eth.data.__class__.__name__)
            continue

        # Now grab the data within the Ethernet frame (the IP packet)
        ip = eth.data

        if type(ip.data) == UDP:  # checking of type of data that was recognized by dpkg
            udp = ip.data
            if udp.dport == port:
                print "["+str(timestamp2datetime(timestamp, True))+"]", "dest port", udp.dport
            if udp.sport == port:
                print "["+str(timestamp2datetime(timestamp, True))+"]", "          source port", udp.sport


if __name__ == '__main__':
    port = 10001
    pcap_file = 'e:/server.pcap'
    with open(pcap_file, 'rb') as f:
        pcap = dpkt.pcap.Reader(f)
        time1 = time.time()
        print_udp_requests(pcap)
        print("cost {0} sec".format(time.time() - time1))
