class Device:

    def __init__(self, on=False):
        self.on = on

    def turn_on(self):
        self.on = True

    def turn_off(self):
        self.on = False

class SmartDevice(Device):

    def __init__(self, on=False, processor_speed=2_000_000):
        super().__init__(on)
        self.processor_speed = processor_speed

    def run_software(self):
        print('Running software')

class SmartPhone(SmartDevice):

    def __init__(self, on=False, processor_speed=3_000_000, phone_number="0912 345 6789"):
        super().__init__(on, processor_speed)
        self.phone_number = phone_number

    def call(self, number):
        print(f'Calling {number}')

class Laptop(SmartDevice):

    def __init__(self, on=False, processor_speed=10_000_000, keyboard_type="membrane"):
        super().__init__(on, processor_speed)
        self.keyboard_type = keyboard_type

    def numlock(self):
        print('Locked number pad')