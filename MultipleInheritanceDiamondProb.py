class Student:
    def __init__(self,rollno=0,name=""):
        print("Student Constructor")
        self.rollno=rollno
        self.name=name

    def read(self):
        self.rollno=int(input("Enter roll numbr:"))
        self.name=input("Enter Name:")
    def display(self):
        print("Roll Number:",self.rollno, "Name:",self.name,end=' ')
        
        
class Marks(Student):
    def __init__(self, rollno=0, name="",marks1=0,marks2=0):
        Student.__init__(self,rollno,name)
        #super().__init__(rollno,name)
        print("Marks Constructor")
        self.marks1=marks1
        self.marks2=marks2


    def read(self):
        #super().read()
        Student.read(self)
        self.marks1=int(input("Enter Marks1:"))
        self.marks2=int(input("Enter Marks2:"))
    def display(self):
        Student.display(self)
        print("Marks:",self.marks1,self.marks2)
    
class Sports(Student):
    def __init__(self,grade=''):
        #super().__init__(rollno,name)
        #Student.__init__(self,rollno,name)
        print("Sports Constructor")
        self.grade=grade

    def read(self):
        #super().read()
        self.grade=input("Enter the grade:")
    def display(self):
        #super().display()
        print("Sports Grade:", self.grade)

class Result(Marks, Sports):
    def __init__(self, rollno=0, name='',marks1=0,marks2=0,grade=""):
        #super().__init__(rollno, name, marks1, marks2)
        #super().__init__(rollno, name,grade)
        print("Result Constructor")
        Marks.__init__(self,rollno, name, marks1, marks2)
        Sports.__init__(self,grade)
        
        self.total=self.marks1+self.marks2
        self.per=self.total/2

      
    def read(self):
        Marks.read(self)
        Sports.read(self)
        self.total=self.marks1+self.marks2
        self.per=self.total/2

    def display(self):
        Marks.display(self)
        
        print("Total:", self.total, "Percetage:",self.per)
        Sports.display(self)
        
if __name__=="__main__":
    
    #sm=Marks(1001,'Rakesh',67,89)
    #ss=Sports(1002,'Rakhi','A')
    #r=Result()
    #sm.display()
    #ss.display()
    
    #r=Result(1001, 'Anil', 67,78,'A')
    #r=Result(int(input("Roll no.")),input("Name:"),int(input("M1:")),int(input("M2:")),input("Grade:"))
    #r.display()
    
    r=Result()
    r.read()
    r.display()
    

              
