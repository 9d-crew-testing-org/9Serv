wtvhome = Service("wtv-home")

@wtvhome.addhandl("playlist-load")
def playlist_load(data):
    out = f"""200 OK\n
    Content-Type: text/html\n
    Content-Length: 0\n
    wtv-backgroundmusic-clear: no_zits\n
    """
    return out

@wtvhome.addhandl("splash")
def splash_handl(data):
    return Responce(200, data=open("./ServiceVault/wtvhome/splash.html").read())

@wtvhome.addhandl("home")
def splash_handl(data):
    return Responce(200, data=open("./ServiceVault/wtvhome/home.html").read())

m.addservice(wtvhome)
