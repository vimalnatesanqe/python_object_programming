#when you want to perform any action for local variable then use static method
#we can the static method outside of the class and inside of the class using class name and ref var name
#we can use both

class static_mrthod():
    @staticmethod
    def st_md1_add(a,b):
        c=a+b
        print(a+b)
        static_mrthod.st_md2_sub(c,c+10)
    @staticmethod
    def st_md2_sub(a,b):
        c=a-b
        print(a-b)
        static_mrthod.st_md3_div(c,10)
    @staticmethod
    def st_md3_div(a,b):
        c=a//b
        print(a//b)
        static_mrthod.st_md4_mul(c,c+10)
    @staticmethod
    def st_md4_mul(a,b):
        c=a*b
        print(a*b)
        static_mrthod.st_md1_add(c,c+10)
ref=static_mrthod()
ref.st_md1_add(1000,10)

        