#stattic variable created for constant value, we call this class variable
#whenever we run the program the class internally crate a object for assign the values

#creating statsic var inside of the class

class st_var():

    #best way to declare above the constructor
    country='Inidia'

print(st_var.__dict__) # class name act as ref var

#inside constructor #usinf class name

class st_var():

    def __init__(self):
        st_var.country='india'

#when created a object for this class the conxtructor automatically call inintate the class var to class obh
#before object creation
print(st_var.__dict__) # class name act as ref var
#after object creation
ref_var=st_var()
print(st_var.__dict__)

#inside instance method,cls mthod,static md

class st_var():

    def ins_md(self):
        st_var.country="india"
        print(st_var.country)

    @classmethod
    def cl_md(cls):
        #we can use cls keyword or class name
        cls.country="america"
        print(cls.country)
    @staticmethod
    def st_md(a):
        st_var.country=a+" "+"jappan"
        print(st_var.country,a)
ref=st_var()
ref.ins_md()
st_var.cl_md()
ref.st_md("my country is")
    



