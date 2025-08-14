#oop-- object orianted programig techniqe
#this is used for code re-usabiity,scalability

#opps- class, object, reference variable

#class - collection atributes or properites (var) and methods
#object - blue print of class
#ref_var- using of ref variable we can call and access the propeties and methods

#structure

class classname():
    '''doc dtring "structure of oop" '''
    def __init__(self, name, age, location='nkl'): #constructor
        self.name=name
        self.age=age
        self.location=location
    
    def in_method(self):
        print("*"*30)
        print((self.name.upper().center(20,"_")))
        print(str(self.age).center(20,"_"))
        print(self.location.upper().center(20,"_"))
        print("*"*30)
    def upper1(name):
        print(str(name).upper())
        
ref_var=classname('vimalathithan',36,"coimbatore")
ref_var.in_method()
ref_var.age=50
ref_var.in_method()

#user input by console oops concepts

class u_input():

    def __init__(self):
        self.name=input("enter user name:: ")
        self.age=int(input("enter your age"))
        self.location=input("enter your location")
        self.eligible_vote()

    def eligible_vote(self):
        if self.age>18:
            print(f"hey {self.name} you are eligible to vote")
            print(f"pleae go and poll your vote to {self.location}")
        else:
            print(f"hey {self.name} you are not eligible to vote")

ref_var=u_input()


print(ref_var.__dict__)

  