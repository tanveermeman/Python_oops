class planet:
    def rotate(self):
        print("rotate")
    def revolve(self):
        print('revolve')

    def rotate_and_revolve(self):
        self.rotate()
        self.revolve()

earth = planet()
earth.rotate_and_revolve()
earth.name = 'The Earth'

venus = planet()
venus.name = 'Venus'


print(earth.name)
print(venus.name)