#constructor used for assign the instance variable to respective self object
#whenever object creation constructor wil call automatically

class a:
    def __init__(self,lcvar,lcvar2):
        self.lcvar=lcvar
        self.lcvar2=lcvar2
        print("this is a construcor call")

a1=a("value1","value2")

#we can call the constructor manualy

a1.__init__("value1","value2")