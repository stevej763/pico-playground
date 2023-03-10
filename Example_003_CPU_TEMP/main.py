from time import sleep

from cpu_temperature import CpuTemperature

cpu_temperature = CpuTemperature(4)

while True:
    sleep(1)
    print(f'Temperature: {cpu_temperature.getCurrentTemperature("c")}°C')
