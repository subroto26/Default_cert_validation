import sys
import re
import os
import socket

global icell
icell = AdminControl.getCell()
GS="\033[0;32m "
GE=" \033[0m"
RE="\033[0;31m"
GY="\033[0;33m"
f19 ="nodeagent"

def cert_val(node):
#    AdminTask.listPersonalCertificates('[-keyStoreName NodeDefaultKeyStore -keyStoreScope (cell):'+icell+':(node):'+node+' ]')

    chain_cert = AdminTask.getCertificateChain('[-certificateAlias default -keyStoreName NodeDefaultKeyStore -keyStoreScope (cell):'+icell+':(node):'+node+' ]')
    print(GY + "chain cert for " + " " + node + GE )
    print(chain_cert)

ptt = f19.strip()
serv = AdminConfig.list('Server')
servl = AdminUtilities.convertToList(serv)
print("Node synchronization started.")
try:
    for servm in servl:
        servlm = servm[0:servm.find("(")]
        node1 = servm.split("/")[3]
        servlml = re.match(ptt, servlm, re.IGNORECASE)
        if (servlml) > -1:
            cert_val(node1)
    except:
        print(RE + "Please check the Dmgr console, seems issue with Websphere. please check console and dmgr logs" + GE)