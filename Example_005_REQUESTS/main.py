import urequests
from time import sleep

from lib.api_config import api_url, api_port
from lib.status_light import StatusLight
from lib.wifi_connection import WifiConnection
from lib.wifi_settings import ssid, password
from cpu_temperature import CpuTemperature

light = StatusLight("LED")
wifi = WifiConnection(ssid, password, light)
wifi.connect()

cpu_temperature = CpuTemperature(4)


def post_cpu_temp():
    temperature = cpu_temperature.getCurrentTemperature("c")
    request_url = f'{api_url}:{api_port}/temperature/{temperature}'
    response = urequests.post(request_url)
    print(response.text)


while True:
    post_cpu_temp()
    light.flash(3, 0.1)
    sleep(2)