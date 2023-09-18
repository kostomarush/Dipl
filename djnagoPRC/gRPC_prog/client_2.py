import grpc
import prot_pb2
import prot_pb2_grpc
import nmap


def connect():
    id_cl = '2'
    channel = grpc.insecure_channel('localhost:50051', options=(('grpc.enable_http_proxy', 0),))
    stub = prot_pb2_grpc.RPCStub(channel)
    response = stub.scan(prot_pb2.DataClient(id_client=id_cl))
    ip_address = response.ip
    port = response.port
    mode = response.mode
    scan(stub, ip_address, port, mode, id_cl)


def scan(stub, ip_address, port, mode, id_cl):
    # SYN ACK Scan:
    nm = nmap.PortScanner()
    if mode == 'SYN':
        nm.scan(ip_address, port, '-sV --script vulscan/ --script-args vulscandb=cve.csv', sudo='True')
        ip_status = nm[ip_address].state()
        protocols = nm[ip_address].all_protocols()[0]
        open_ports = nm[ip_address]['tcp'].keys()
        for ports in open_ports:
    
            stub.scan(prot_pb2.DataClient(id_client=id_cl, ip_status=ip_status, protocols=protocols, open_ports=f'{ports}',
                                          state=nm[ip_address]['tcp'][ports]['state']))

            script = nm[ip_address]['tcp'][ports].get('script','')
            if script!='':
                all_chunk = ['1', '2', '3']
                print(all_chunk)
            else:
                all_chunk = 'No'
            for data in all_chunk:
                request = prot_pb2.DataChunk(data_chunk=data)
                response = stub.chunk(request)
                



    

    # UDP Scan
    if mode == 'UDP':
        nm.scan(ip_address, port, '-v -sU')
        ip_status = nm[ip_address].state()
        protocols = nm[ip_address].all_protocols()[0]
        open_ports = nm[ip_address]['udp'].keys()
        for ports in open_ports:
            stub.scan(prot_pb2.DataClient(id_client=id_cl, ip_status=ip_status, protocols=protocols,
                      open_ports=f'{ports}', state=nm[ip_address]['udp'][ports]['state']))
    # Comprehensive Scan
    if mode == 'CS':
        nm.scan(ip_address, port, '-v -sS -sV -sC -A -O')
        ip_status = nm[ip_address].state()
        protocols = nm[ip_address].all_protocols()[0]
        open_ports = nm[ip_address]['tcp'].keys()
        for ports in open_ports:
            stub.scan(prot_pb2.DataClient(id_client=id_cl, ip_status=ip_status, protocols=protocols, open_ports=f'{ports}',
                                          state=nm[ip_address]['tcp'][ports]['state']))
    # OS Detection
    if mode == 'OS':
        os_detection = nm.scan(
            ip_address, arguments="-O")['scan'][ip_address]['osmatch']
        vendor = os_detection[0]['osclass'][0]['vendor']
        os_family = os_detection[0]['osclass'][0]['osfamily']
        osgen = os_detection[0]['osclass'][0]['osgen']
        stub.scan(prot_pb2.DataClient(id_client=id_cl,
                  vendor=vendor, os_family=os_family, osgen=osgen))

    stub.scan(prot_pb2.DataClient(id_client=id_cl, message='End'))


if __name__ == "__main__":
    connect()
