from scrapli.driver.core import IOSXEDriver
from scrapli.driver.core import IOSXRDriver
import os
import re
import json

devices = [{
    "host":"ios-xe-mgmt-latest.cisco.com",
    "auth_username":"developer",
    "auth_password":"C1sco12345",
    "auth_strict_key":False
}, {
    "host":"sbx-iosxr-mgmt.cisco.com",
    "auth_username":"admin",
    "auth_password":"C1sco12345",
    "port":8181,
    "auth_strict_key":False
}]

os.system("clear")

conn_XE = IOSXEDriver(**devices[0])
conn_XE.open()
response = conn_XE.send_command("show ip int brief")
print("RESPONSE")
print("*" * 100)
print(response.result)
conn_XE.close()


conn_XR = IOSXRDriver(**devices[1])
conn_XR.open()
response = conn_XR.send_command("show ip int brief")

print("RESPONSE")
print("*" * 100)
# print(response.result)
# print(re.findall("Giga.+", response.result))
print(json.dumps(re.findall("Giga.+", response.result), indent=2))
conn_XR.close()