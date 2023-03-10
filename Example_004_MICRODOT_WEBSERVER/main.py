from lib.microdot import Microdot
from lib.status_light import StatusLight
from lib.wifi_connection import WifiConnection
from lib.wifi_settings import ssid, password

light = StatusLight("LED")
wifi = WifiConnection(ssid, password, light)
app = Microdot()


@app.route('/')
def index(request):
    client_addr = request.client_addr
    request_method = request.method
    request_headers = request.headers
    request_json = request.json
    print(client_addr[0])
    return {'clientIp': client_addr[0],
            'requestMethod': request_method,
            'requestHeaders': request_headers,
            'requestJson': request_json}


wifi.connect()
app.run('0.0.0.0', 8080, True)
