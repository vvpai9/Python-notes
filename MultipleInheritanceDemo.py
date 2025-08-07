class Base1:
    def __init__(self):
        print("Base1")
class Base2:
    def __init__(self):
        print("Base2")
class Derived(Base1,Base2):
#class Derived(Base2,Base1):
    def __init__(self):
        #super().__init__()
        #super().__init__()
        #super().__init__()
        Base2.__init__(self)
        Base1.__init__(self)
        print("Derived")

if __name__=="__main__":
    d=Derived()
    

    
