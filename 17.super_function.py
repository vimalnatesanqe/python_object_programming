# super function used for removing the duplicates
# super function poiting the parent object
# whenever we have comman properties and method then create a comman method in parent
# class the use that


class human():

    def __init__(self,name,age,college):
        self.name=name
        self.age=age
        self.college=college

    def printinfo(self):
        print(self.name)
        print(self.age)
        print(self.college)

class man(human):

    def __init__(self,name,age,college,vhle,type):
        super().__init__(name,age,college)
        self.vhle=vhle
        self.type=type
    def printinfo(self):
        super().printinfo()
        print(self.vhle)
        print(self.type)
man=man('vimal',37,"SRM",'pulsar','petrol')
man.printinfo()
