#!/usr/bin/python

class Shape:
    def __init__(self):
        print "Shape Constructor"
    def __del__(self):
        print "Shape Destructor"
    def __Draw(self):
        pass
    def __Area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        print "Circle Constructor"
        self.radius = radius
    def __del__(self):
        print "Circle Destructor"
    def __Draw(self):
        print "Drawing Circle of Radius {}".format(self.radius)
    def __Area(self):
        return self.radius*self.radius*22.0/7.0

class Rectangle(Shape):
    def __init__(self, length, breadth):
        print "Rectangle Constructor"
        self.length = length
        self.breadth = breadth
    def __del__(self):
        print "Rectangle Destructor"
    def __Draw(self):
        print "Drawing Rectanlge of length {} breadth {}".format(self.length, self.breadth)
    def __Area(self):
        return self.length*self.breadth
    
class Square(Shape):
    def __init__(self, length):
        print "Square Constructor"
        self.length = length
    def __del__(self):
        print "Square Destructor"
    def __Draw(self):
        print "Drawing Square of length {}".format(self.length)
    def __Area(self):
        return self.length*self.length

class ShapeManager:
    def Draw(self, obj):
        if(isinstance(obj,Square)):
            obj._Square__Draw()
        elif(isinstance(obj, Rectangle)):
            obj._Rectangle__Draw()
        elif(isinstance(obj, Circle)):
            obj._Circle__Draw()
    def Area(self, obj):
        if(isinstance(obj,Square)):
            return obj._Square__Area()
        elif(isinstance(obj, Rectangle)):
            return obj._Rectangle__Area()
        elif(isinstance(obj, Circle)):
            return obj._Circle__Area()

def Main():
    sm = ShapeManager()
    sq = Square(10)
    sm.Draw(sq)
    print sm.Area(sq)

    rt= Rectangle(5, 7)
    sm.Draw(rt)
    print sm.Area(rt)

if __name__ == "__main__":
    Main()
