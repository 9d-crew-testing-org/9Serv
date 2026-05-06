wtvheadwaiter = Service("wtv-head-waiter")
@wtvheadwaiter.addhandl("login")
def login(data: dict):
    challenge = "".join([choice(list(ascii_lowercase)) for i in range(16)])
    login_data = """200 Error: Operation was succesful
    Connection: Keep-Alive
    Expires: Wed, 09 Oct 1991 22:00:00 GMT
    wtv-country: US
    wtv-challenge: {challenge}
    wtv-language-header: en-US,en
    wtv-visit: wtv-head-waiter:/ValidateLogin
    wtv-backgroundmusic-clear: yes
    wtv-backgroundmusic-add: wtv-music:/music
    """
    return login_data.format(challenge=challenge)
@wtvheadwaiter.addhandl("login-stage-two")
def stage2(data: dict):
    print("stage two login")
    return Responce(200, {'wtv-visit': 'wtv-home:/home'})
@wtvheadwaiter.addhandl("ValidateLogin")
def validate_login(data: dict):
    print(f"challenge: {data['headers'].get('wtv-challenge')}")
    validate_login_headers = {
    'wtv-visit': 'wtv-home:/splash',
    'wtv-backgroundmusic-load-playlist': 'wtv-home:/playlist-load'
    }
    return Responce(200, validate_login_headers)
m.addservice(wtvheadwaiter)