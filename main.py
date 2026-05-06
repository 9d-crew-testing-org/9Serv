import sys
import os
import mimetypes
from config import *
from wtvframework import Minisrv, Responce, SendFile, Service, parsehttp
from string import ascii_lowercase
from random import choice

print("starting server")
m = Minisrv()

def quickimport(filename):
    with open(filename) as f:
        code = f.read()
    exec(code)

def wtv_svcs_add(host=connect_host):
    out = "wtv-service: name=wtv-* host={connect_host} port=1615 flags=0x00000007\n".format(connect_host=host)
    sheet = "wtv-service: name={name} host={connect_host} port=1615 flags={flags}"
    for i in m.services:
        if i.name.startswith(('wtv-1800', 'wtv-star')):
            out += sheet.format(name=i.name, flags="0x00000012", connect_host=host)
        else:
            out += sheet.format(name=i.name, flags="0x00000007", connect_host=host)
        if i.name == "wtv-1800": out += " connections=15892659828057"
        out += "\n"
    return out

__builtins__.wtv_svcs_add = wtv_svcs_add

# Services
quickimport("./ServiceStore/wtv1800.py")
quickimport("./ServiceStore/headwaiter.py")
quickimport("./ServiceStore/wtvhome.py")
quickimport("./ServiceStore/wtvstatic.py")

m.runserv(host=host, port=port)