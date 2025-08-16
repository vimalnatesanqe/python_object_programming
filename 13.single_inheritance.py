#using of inheritance we can access the members one class to another class

#single inheritance - one parent and one child

class parent():
    name="vimalthithann"
    def __init__(self,age,location):
        self.age=age
        self.location=location
    def ins_imd(self):
        print(self.age)
        print(self.location)
    def cls_cmd(cls):
        print(cls.name)
        cls.country="india"
        print(cls.country)
    def sta_smd(a,b):
       c=a+b
       print(c)
       print("this is static method")
        

class child(parent):
    pass


child_obj=child(36,'nkl')
#child_obj=child()

#accessed all the members except local var from static method
print(child_obj.name)
print(child_obj.age)
print(child_obj.location)
print(child_obj.cls_cmd())
print(child_obj.country)
print(child.sta_smd(10,20))


