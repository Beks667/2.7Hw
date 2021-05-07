class Rectangle:

    
    def __init__(self,length,width,height):
        self.length = length
        self.width = width
        self.height = height
        if type(length) and type(width) and type(height) not in [int,float] or length < 0 or width < 0 or length < 0:
            raise ValueError

    def calculate_volume(self):
        # return self.length * self.width * self.height
        try:
            return self.length * self.width * self.height
        except ValueError:
            print("oshibka") 
            


c=Rectangle(1, 4, 5)
print(c.calculate_volume())
