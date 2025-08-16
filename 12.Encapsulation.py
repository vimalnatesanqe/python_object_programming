#encapsulation used for binding the members and variables as per modifiers

#there are 3 modifiers 
#1public
#2.private
#3.protect 

#encapsulation concepts basically used for private var concepts
#we cannot acces this private variable outside of the class
#but we can achive thngs using getter and setter method

class car():

    def __intit__(self):
        self.__phone_no=9952350445  
        self.car="bmw"
        self.location="namakkal"
        self.owner_name="vimal"
        
    
car1=car()
car1.car="scoda"
print(car1.car)




#we can achive this using getter and setter
############getter#######
class car1():

    def __intit__(self):
        self.car="bmw"
        self.location="namakkal"
        self.owner_name="vimal"
        self.__phone_no=9952350445  
    def get_phone_nbr(self):
        return self.__phone_no

car2=car1()
print(car2.get_phone_nbr())
