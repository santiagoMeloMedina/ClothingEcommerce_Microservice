
import os

env = os.environ

env['DS_HOSTINSTANCE'] = "".join(open("/etc/hostname", 'r').readlines()).split()[0]

INFO_DISCOVER = {
    "PROTOCOL": env.get('DS_PROTOCOL'),
    "HOSTDISCOVER": env.get('DS_HOSTDISCOVER'),
    "PORTDISCOVER": env.get('DS_PORTDISCOVER'),
    "SERVICENAME": env.get('DS_SERVICENAME'),
    "HOSTINSTANCE": env.get('DS_HOSTINSTANCE'),
    "PORTINSTANCE": env.get('DS_POSTINSTANCE'),
    "HEARTBEATDISCOVER": env.get('DS_HEARTBEATDISCOVER')
}