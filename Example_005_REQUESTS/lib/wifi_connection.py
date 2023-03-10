import network
from time import sleep
import machine


class WifiConnection:

    def __init__(self, ssid, password, status_light=None):
        self.status_light = status_light
        self.ssid = ssid
        self.password = password

    def connect(self):
        try:
            ip = self.__join_network()
            return ip
        except KeyboardInterrupt:
            machine.reset()

    def __join_network(self):
        print(f'joining network: {self.ssid}')
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        wlan.connect(self.ssid, self.password)
        while not wlan.isconnected():
            print('Waiting for connection...')
            sleep(1)
        ip = wlan.ifconfig()[0]
        print(f'Connected on {ip}')
        return ip
