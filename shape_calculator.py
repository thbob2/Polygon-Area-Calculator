import math



class Rectangle(object):

    def __init__(self,width,height):
        self.width = width
        self.height = height
    
    def set_width(self,width):
        self.width = width
    
    def set_height(self,height):
        self.height = height
    
    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (self.width + self.height) * 2
    
    def get_diagonal(self):
        return math.sqrt(self.width**2 + self.height**2)
    
    def get_picture(self):
        
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        picture = ""
        for line in range(self.height):
            picture += "*" * self.width +"\n"
        
        return picture
    
    def get_amount_inside(self,rectangle):
        if self.get_area() < rectangle.get_area():
            return 0
        
        return int(self.get_area() / rectangle.get_area())
        
    
    def __str__(self):
        return "Rectangle(width={}, height={})".format(self.width,self.height)
    
    
    
    
class Square(Rectangle):
    
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side    
    def set_side(self,side):
        self.height = side
        self.width = side
        self.side = side
    
    def set_height(self, height):
        self.set_side(height)
    
    def set_width(self, width):
        self.set_side(width)

    def __str__(self):
        return "Square(side={})".format(self.side)