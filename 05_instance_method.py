#if you want access and perform any action in instance variable
#then use instance method

#instance method

class ins_md():

    def __init__(self):
        self.name="vimal"
        self.age=36
        self.locatin='nkl'
    #ins_md
    def ins_md(self,a,b):
        self.a=a 
        self.b=b
        print(self.a)
        print(self.b)
        self.location="namakkal"
        print(self.location)
    def ins_md2(self):
        print("you are in the md2")
        print(self.name)
        print(self.age)

ref=ins_md()
ref.ins_md("hey guys you are in the md1","you are in the taminadu state and below mentioned city")
ref.ins_md2()


class ins_md_call_inside_instance_md():

    def __init__(self):
        self.name="vimal"
        self.age=36
        self.locatin='nkl'
        self.ins_md(self.name,self.locatin)
    #ins_md
    def ins_md(self,a,b):
        self.a=a 
        self.b=b
        print(self.a)
        print(self.b)
        self.location="namakkal"
        print(self.location)
        self.ins_md2()
    def ins_md2(self):
        print("you are in the md2")
        print(self.name)
        print(self.age)

ref=ins_md_call_inside_instance_md()
