
# state
# make, radius, color, speed, is_on
# Behaviour
# switch_on, switch_off, increase_speed, decrease_speed

class fan:
    def __init__(self,make, radius, color):
        self.make = make
        self.radius = radius
        self.color = color
        self.speed = 0
        self.is_on = False

    def __repr__(self):
        return repr((self.make, self.radius, self.color, self.speed , self.is_on))

    def switch_on(self):
        self.is_on = True
        self.speed = 3

    def switch_off(self):
        self.is_on = False
        self.speed = 0

    def increase_speed(self):
        self.speed += 1

    def decrease_speed(self):
        self.speed -= 1

fan = fan('Manufacturer', 5, 'green')
fan.switch_on()
print(fan)
fan.switch_off()
print(fan)
fan.increase_speed()
print(fan)
fan.decrease_speed()
print(fan)


