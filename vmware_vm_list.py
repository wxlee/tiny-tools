#!/usr/bin/python
#coding=utf8

# 2015 08 28 Walker
# Connect to VMware vsphere and list all vms in one program

import paramiko
import getpass

# the list of vmware vsphere ip
ZONE_A=['172.25.1.1', '172.25.1.2']

ZONE_B=['10.10.1.1', '10.10.1.2']

# the login admin user
USER='root'

# ask for password
PASSWD = getpass.getpass('password: ')

TIMEOUT=5

# show all vm
CMD='vim-cmd vmsvc/getallvms'

def list_vm(ip):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
   
    print "......{}......".format(ip)
   
    # connect to host
    try:
        ssh.connect(ip, 22, USER, PASSWD, timeout=TIMEOUT)
    except Exception, e:
        print "Exception on Connect: %s" % e
        return
   
    # run command
    try:
        stdin, stdout, stderr = ssh.exec_command(CMD)
    except:
        print "Exception on exec: %s" % e
        return
   
    # get vm name
    for i in stdout.readlines():
        j = i.split()
        # ignore first row
        if j[0] != 'Vmid':
            print j[1]
   
    ssh.close()
    print "========================="


for host in ZONE_A:
    list_vm(host)
   

for host in ZONE_B:
    list_vm(host)
