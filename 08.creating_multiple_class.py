class class1():
    #class variable
    country="india"
    #constructor
    def __init__(self):
        self.name="vimal"
        self.age=36
        self.occupation='QA'
    #instant method
    def ins_md_display(self):
        print("*"*30)
        print(self.name)
        print(self.age)
        print(self.occupation)
        print(class1.country)
        print("*"*30)
    @classmethod
    def clss_md_update(cls):
        cls.occupation='python developer'
        cls.country='usa'
    @staticmethod
    def stt_md_display():
        print("*"*30)
        print(class1.occupation)
        print(class1.country)
        print("*"*30)
    
class class2():
    #class variable
    country="india"
    #constructor
    def __init__(self):
        self.name="vimal"
        self.age=36
        self.occupation='QA'
    #instant method
    def ins_md_display(self):
        print("*"*30)
        print(self.name)
        print(self.age)
        print(self.occupation)
        print(class1.country)
        print("*"*30)
    @classmethod
    def clss_md_update(cls):
        cls.occupation='python developer'
        cls.country='usa'
    @staticmethod
    def stt_md_display():
        print("*"*30)
        print(class1.occupation)
        print(class1.country)
        print("*"*30)
ref=class1()
ref.ins_md_display()
ref.clss_md_update()
ref.stt_md_display()

ref=class1()
ref.ins_md_display()
ref.clss_md_update()
ref.stt_md_display()
