class Student:
    def __init__ (self):
        self.rollno = 0
        self.name = ""
        self.per = 0.0
    def readStudent (self):
        self.rollno = int (input ("Enter roll number: "))
        self.name = input ("Enter name: ")
        self.per = float (input ("Enter percentage: "))
    def displayStudent (self):
        print ("Roll number: ", self.rollno)
        print ("Name: ", self.name)
        print ("Percentage: ", self.per)
if __name__ == '__main__':
    s = Student ()
    s.displayStudent ()
    print (s.__dict__)
    s.readStudent()
    print ("")
    s.displayStudent ()
    print (s.__dict__)
    print ("")