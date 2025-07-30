class Shape:
    def __init__(self, dim1 = 0.0, dim2 = 0.0):
        self.dim1 = dim1
        self.dim2 = dim2
    def readDimensions (self):
        self.dim1 = float (input ("Enter Dimension 1: "))
        self.dim2 = float(input("Enter Dimension 2: "))
    def displayDimensions (self):
        print ("\nDimension 1:", self.dim1, "\nDimension 2:", self.dim2)

class Rectangle (Shape):
    def __init__(self, dim1 = 0.0, dim2 = 0.0):
        super().__init__(dim1,dim2)
        self.area = self.dim1 * self.dim2
    def calc (self):
        self.area = self.dim1 * self.dim2
    def display (self):
        print ("Area of Rectangle:", self.area)

class Triangle (Shape):
    def __init__(self, dim1 = 0.0, dim2 = 0.0):
        super().__init__(dim1,dim2)
        self.area = 0.5 * self.dim1 * self.dim2
    def calc (self):
        self.area = 0.5 * self.dim1 * self.dim2
    def display (self):
        print ("Area of Triangle:", self.area)

class Box (Rectangle):
    def __init__(self, dim1 = 0.0, dim2 = 0.0, dim3 = 0.0):
        super().__init__(dim1, dim2)
        self.dim3 = dim3
        self.vol = self.dim1 * self.dim2 * self.dim3
    def readDimensions(self):
        super().readDimensions()
        self.dim3 = float (input ("Enter Dimension 3: "))
    def displayDimensions(self):
        super().displayDimensions()
        print ("Dimension 3:", self.dim3)
    def calc(self):
        self.vol = self.dim1 * self.dim2 * self.dim3
    def display (self):
        print ("Volume of Box:", self.vol)

if __name__ == '__main__':
    shp = []
    while True:
        s = None
        print ("","1: Rectangle", "2: Triangle", "3: Box", "0: Exit", "", sep = '\n')
        ch = int (input ("Enter your choice: "))
        if ch == 1:
            s = Rectangle()
        elif ch == 2:
            s = Triangle()
        elif ch == 3:
            s = Box()
        elif ch == 0:
            break
        else:
            print ("Invalid choice")
            continue
        s.readDimensions()
        s.calc()
        shp.append (s)
    for a in shp:
        a.displayDimensions()
        a.display()