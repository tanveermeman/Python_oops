# motorbike
class motorbike:  # this is the constructor
    def __init__(self, speed):
        self.speed = speed
        print(speed)
        print("Motorbike instance created ")

    def increase_speed(self, how_much):
        self.speed += how_much

    def decrease_speed(self,how_much):
        if self.speed - how_much > 0 :
            self.speed -= how_much

        else :
            print("get a life bruh!!")


honda = motorbike(50)
ducati = motorbike(250)
ducati_2 = motorbike(200)

honda.speed = 50
ducati.speed = 250

print(honda.speed, 'honda speed')
print(ducati.speed, 'ducati speed\n')

honda.increase_speed(100)
ducati.increase_speed(200)

print(honda.speed, 'honda increased')
print(ducati.speed, 'ducati increased\n')

honda.decrease_speed(125)
ducati.decrease_speed(500)

print(honda.speed, 'hoda decreased')
print(ducati.speed, 'ducati decreased\n')
#
# honda.speed = 150
#
# print(honda.speed)
# print(ducati.speed)
