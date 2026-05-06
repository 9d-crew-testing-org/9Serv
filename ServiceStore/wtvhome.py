home = Service("wtv-home")

@home.addhandl("playlist-load")
def playlist_load(data):
    out = f"""200 OK\n
    Content-Type: text/html\n
    Content-Length: 0\n
    wtv-backgroundmusic-clear: no_zits\n
    """
    return out

@home.addhandl("splash")
def splash_handl(data):
    return Responce(200, data=open("./ServiceVault/wtvhome/splash.html").read())

@home.addhandl("home")
def splash_handl(data):
    return Responce(200, data=open("./ServiceVault/wtvhome/home.html").read())

m.addservice(home)