wtvstatic = Service("wtv-static")

for fname in os.listdir("./ServiceVault/wtvstatic/"):
    full_path = os.path.join("./ServiceVault/wtvstatic/", fname)
    if os.path.isfile(full_path):
        def make_static_handler(filepath):
            def handler(data):
                try:
                    with open(filepath, "rb") as f:
                        content = f.read()
                    mime, _ = mimetypes.guess_type(filepath)
                    if not mime:
                        mime = "application/octet-stream"
                    return (
                        "200 OK\n"
                        f"Content-Type: {mime}\n"
                        f"Content-Length: {len(content)}\n\n"
                    ).encode("ascii") + content
                except Exception as e:
                    return "500 Internal Server Error\nContent-Length: 0\n\n"
            return handler
        wtvstatic.addhandl(fname)(make_static_handler(full_path))

m.addservice(wtvstatic)