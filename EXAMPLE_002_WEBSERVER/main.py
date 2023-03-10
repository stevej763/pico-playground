import socket

import machine

from lib.status_light import StatusLight
from lib.webserver import Webserver
from lib.webserver_settings import port
from lib.wifi_connection import WifiConnection
from lib import wifi_settings

import time




wifiStatusLight = StatusLight("LED")

wifi = WifiConnection(wifi_settings.ssid, wifi_settings.password, wifiStatusLight)
ipAddress = wifi.connect()

webserver = Webserver(ipAddress, port, socket)

connection = webserver.open_socket()

webserver.serve(connection)


adc = machine.ADC(4)

while True:
    ADC_voltage = adc.read_u16() * (3.3 / (65535))
    temperature_celcius = 27 - (ADC_voltage - 0.706)/0.001721
    temp_fahrenheit=32+(1.8*temperature_celcius)
    print("Temperature: {}°C {}°F".format(temperature_celcius,temp_fahrenheit))
    time.sleep_ms(500)