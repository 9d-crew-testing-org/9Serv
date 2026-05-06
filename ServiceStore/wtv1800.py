wtv1800 = Service("wtv-1800")
@wtv1800.addhandl("preregister")
def preregister(data):
    return f"""200 OK
Connection: Keep-Alive
wtv-initial-key: BCK9Zzas8So=
Content-Type: text/html
wtv-client-time-zone: GMT -0000
wtv-client-time-dst-rule: GMT
wtv-client-date: Fri, 28 Apr 2023 19:12:37 GMT
Content-length: 0
wtv-visit: wtv-head-waiter:/ValidateLogin
wtv-service: reset
wtv-home: wtv-home:/home
{wtv_svcs_add()}
"""
m.addservice(wtv1800)