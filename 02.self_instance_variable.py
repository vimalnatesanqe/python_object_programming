#self is not a key word
#self is a current object variable, it is used to pointing the current object

#self

class self():
    '''this class creted for self variable practice'''
    #constructor it will call automatically while object creation
    def __init__(self): # this self is poting the current object
        self.name="vimal"
        print(self.name)
ref=self()

#instance variable
#instance variable basically used for dynamic values, when the input values are changed freuently

#instance var creation 
#inside the constructior
#inside the instance method
#out side the class

# whenever we create the instace variable inside of the class use self key word.
#if it is out side then use refeence variable

class c_instance():

    def __init__(self):
        #inside the constructor
        self.name="vimalathithan"
        self.age=36
        self.location='nkl'
    def ins_md(self):
        #inside the instance method
        self.currentlocation='coimbatore'
        self.mobno=9952350445
        self.isactive=True
ref_v=c_instance()
#out side instance variable creation
#use ref var instaed of self
ref_v.iswhatsappactive=True

#checking instance variable in the liist
print(ref_v.__dict__)

#Accessing instance variables

class a_instance():

    def __init__(self):
        #inside the constructor
        
        self.name="vimalathithan"
        self.age=36
        self.location='nkl'
        print("*"*20)
        #accesiing inside of constructor
        
        print("Accessing inside constructor")
        print("*"*20)
        print(f"{self.name},{self.age},{self.location}")

        self.ins_md()
        
    def ins_md(self):
        #inside the instance method
        self.currentlocation='coimbatore'
        self.mobno=9952350445
        self.isactive=True
        print("Accessing inside instance method")
        print("*"*20)
        print(f"{self.currentlocation},{self.mobno}")
ref_v=a_instance()
#out side instance variable creation
#use ref var instaed of self
ref_v.iswhatsappactive=True


print("Accessing out side of the class")
print("*"*20)
print(f"{ref_v.name},{ref_v.age},{ref_v.location}")
print(f"{ref_v.currentlocation},{ref_v.mobno}")
print(f"{ref_v.iswhatsappactive}")

#deleting instance variable three ways using del
#if it is inside constructor del self.
#inside ithe instance method del self.
#out side the constructor use del ref_var.


#practice

class practice():
    class_var="constant value"
    def __init__(self,changable_value):
        self.changable_value=changable_value
        self.cstr_declare="value"
        print('constructor call statment')
        print(self.changable_value)
        print(self.cstr_declare)
        self.instnd_md()
    def instnd_md(self):
        print('this is instand md call')
        print(self.changable_value)
        print(self.cstr_declare)
for i in range(1,10):
    ref_var=practice(i)



