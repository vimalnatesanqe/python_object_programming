#local variable values are temprorray variable
#it will assign the values in the run time and after compltetion of the program 
# it will destory #from the memmory

# we can cretate this local variable multiple ways
#inside the constructor
#inside the ins mtd
#inside the clss mtd
#inside the static mtd

class loc_var():

    #constructoe
    def __init__(self):
        self.country=input("share your conutry name:: ")
        #local var
        print("*"*30)
        print("this is constructor call")
        print("*"*30)
        l_var="hey user your country name is"
        print(f"{l_var} {self.country}")
        self.ins_mtd()
    def ins_mtd(self):
        print("*"*30)
        print("this is ins_md call")
        print("*"*30)
        l_var="hey user your country name is"
        print(f"{l_var} {self.country}")
        loc_var.cl_md()
    @classmethod
    def cl_md(cls):
        cls.country=input("share your conutry name:: ")
        print("*"*30)
        print("this is cl_md call")
        print("*"*30)
        l_var="hey user your country name is"
        print(f"{l_var} {cls.country}")
        loc_var.st_md()
    @staticmethod
    def st_md():
        loc_var.country=input("share your conutry name:: ")
        print("*"*30)
        print("this is cl_md call")
        print("*"*30)
        l_var="hey user your country name is"
        print(f"{l_var} {loc_var.country}")
ref=loc_var()



