import pcap
import dpkt
import time
import wmi

filte = raw_input("input filter:")

# get network info
c = wmi.WMI()
for interface in c.Win32_NetworkAdapterConfiguration(IPEnabled=1):
    print interface.Description, interface.MACAddress
    for ip_address in interface.IPAddress:
        print ip_address

pc = pcap.pcap()
if filte != 'no':
    pc.setfilter(filte)
for ptime, pdata in pc:
    ptime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ptime))
    print("------------------get time:%s---------------" % ptime)
    print(pdata)
    p = dpkt.ethernet.Ethernet(pdata)
    print("".join((p.data.__class__.__name__, "/", p.data.data.__class__.__name__)))
    if p.data.__class__.__name__ == 'IP':
        ip_src = '%d.%d.%d.%d' % tuple(map(ord, list(p.data.src)))
        ip_dst = '%d.%d.%d.%d' % tuple(map(ord, list(p.data.dst)))
        print("IP src %s  dst %s" % (ip_src, ip_dst))
        if p.data.data.__class__.__name__ == 'TCP':
            print("TCP src port:%s dst port:%s" % (p.data.data.sport, p.data.data.dport))
            if p.data.data.dport == 80 and len(p.data.data) > 0:
                http = dpkt.http.Request(p.data.data.data)
                print("http uri:", http.uri)
                print("http body:", http.body)
        if p.data.data.__class__.__name__ == 'UDP':
            print("UDP src port:%s dst port:%s" % (p.data.data.sport, p.data.data.dport))
            if len(p.data.data) > 0:
                print(p.data.data.data)
