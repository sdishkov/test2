#! /home/slavey/learn-yang/bin/python3.10

from ncclient import manager

RTR1_MGR = manager.connect(host='sandbox-iosxr-1.cisco.com',
                    port=22,
                    username='admin', 
                    password='C1sco12345',
                    hostkey_verify=False, device_params={'name':'csr'})

print(RTR1_MGR.get_config('running'))

RTR1_MGR.close_session()