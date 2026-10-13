import threading, urllib.request, urllib.error, json
from server import make_server

srv = make_server(0)  # port 0 = pick any free port
port = srv.server_address[1]
threading.Thread(target=srv.serve_forever, daemon=True).start()
base = f"http://127.0.0.1:{port}"

r = urllib.request.urlopen(base + "/")
assert r.status == 200 and "text/html" in r.headers["Content-Type"] and b"Hello" in r.read()
r = urllib.request.urlopen(base + "/api/time-zone")
assert r.status == 200 and json.loads(r.read()) == {"zone": "UTC"}
try:
    urllib.request.urlopen(base + "/missing")
    raise SystemExit("expected a 404")
except urllib.error.HTTPError as e:
    assert e.code == 404
srv.shutdown()
print("server: all checks passed")
