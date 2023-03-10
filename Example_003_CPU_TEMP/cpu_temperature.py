import machine


class CpuTemperature:

    def __init__(self, adc_pin):
        self.adc = machine.ADC(adc_pin)

    def getCurrentTemperature(self, format):
        adc_voltage = self.adc.read_u16() * (3.3 / 65535)
        temperature_celcius = 27 - (adc_voltage - 0.706) / 0.001721
        if format == "f":
            temp_fahrenheit = 32 + (1.8 * temperature_celcius)
            return temp_fahrenheit
        else:
            return temperature_celcius
