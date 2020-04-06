#import Library
import paramiko
import time
import sys

try:
#variabel ip (untuk ip yang diremote), username (untuk masuk ssh), password (password ssh)
    ip_address = ["192.168.122.65","192.168.122.190","192.168.122.152","192.168.122.4"]
    username = "admin"
    password = ""
    i = 0
    
#perintah untuk melakukan koneksi ssh client ke mikrotik

    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    for ip in ip_address :
        i += 1
        ssh_client.connect(hostname=ip,username=username,password=password)
        print (f"sukses login to {ip}")
        ssh_client.exec_command(f"/system identity set name=R{i}")
        ssh_client.exec_command("/tool romon set enabled=yes secrets=very")
        ssh_client.exec_command("/ip dhcp-client add dhcp-options=hostname,clientid disabled=no interface=ether1")
        ssh_client.exec_command("/ip address add address=192.168.1.1/24 interface=ether2 network=192.168.1.0")
        ssh_client.exec_command("/ip dhcp-server network add address=192.168.1.0/24 gateway=192.168.1.1")
        ssh_client.exec_command("/ip pool add name=dhcp_pool0 ranges=192.168.1.2-192.168.1.254")
        ssh_client.exec_command("/ip dhcp-server add address-pool=dhcp_pool0 disabled=no interface=ether2 name=dhcp1")
        ssh_client.exec_command("/ip service disable telnet,ftp,www,api-ssl")
        ssh_client.exec_command("/ip firewall nat add chain=srcnat out-interface=ether1 action=masquerade")
        ssh_client.exec_command("/user set admin name=very password=123456")
        print (f"Konfigurasi Router Identity R{i} berhasil")
        print (f"Konfigurasi ip address {ip} berhasil")
        time.sleep(0.5)
    sys.exit()

except KeyboardInterrupt:
    print ("\n Exit \n")
    sys.exit()
