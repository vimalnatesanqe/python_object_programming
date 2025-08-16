#with out inherit we can pass the mebers one class to another class
#using ref obj we can achive

class class1():
    country="india"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printinfo(self):
        print(self.name)
        print(self.age)
    @classmethod
    def printinfo1(cls):
        print(cls.country)
ref1=class1("vimal",36)

class class2():
    @staticmethod
    def upper(ro):
        x=ro.name.upper()
        print(x)
        print(ro.age)
    @staticmethod
    def ref_class(cls_obj):
        x=cls_obj.country.upper()
        print(x)

ref2=class2()
ref2.upper(ref1)
ref2.ref_class(class1)