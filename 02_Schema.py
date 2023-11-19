#! /home/slavey/learn-yang/bin/python3.10

from ncclient import manager

RTR1_MGR = manager.connect(host='sandbox-iosxr-1.cisco.com',
                    port=830,
                    username='admin', 
                    password='C1sco12345',
                    hostkey_verify=False, device_params={'name':'csr'})

SCHEMA = RTR1_MGR.get_schema('Cisco-IOS-XR-es-acl-datatypes')
print(SCHEMA)

RTR1_MGR.close_session()