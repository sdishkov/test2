#! /home/slavey/learn-yang/bin/python3.10
# Slavey Dishkov, ICTNET
# Filename: 05_Fliter_intf.py

from ncclient import manager

RTR1_MGR = manager.connect(host='sandbox-iosxr-1.cisco.com',
                    port=830,
                    username='admin', 
                    password='C1sco12345',
                    hostkey_verify=False, device_params={'name':'csr'})

FILTER = """
<filter>
<interface-configurations
			xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg">
<interface-configuration>
<interface-name>GigabitEthernet0/0/0/2</interface-name>
</interface-configuration>
</interface-configurations>
</filter>"""
print(RTR1_MGR.get_config('running',FILTER))

RTR1_MGR.close_session()