#method calling outside of the  main class and inside of inherit class

class a:

    def ins_md1(self):
        print("ins-md1-a")
        
class b(a):
    def ins_md1(self):
        print("ins-md1-b")
        
class c(b):
    def ins_md1(self):
        print("ins-md1-c")
        

class d(c):
    def ins_md1(self):
        print("ins-md1-d")
        c.ins_md1(self)
        b.ins_md1(self)
        a.ins_md1(self)
        
d=d()
d.ins_md1()

#another way
#super keyword

#method calling outside of the  main class and inside of inherit class

class a:
    def ins_md1(self):
        print("ins-md1-a")

class b(a):
    def ins_md1(self):
        print("ins-md1-b")
        super().ins_md1()

class c(b):
    def ins_md1(self):
        print("ins-md1-c")
        super().ins_md1()

class d(c):
    def ins_md1(self):
        print("ins-md1-d")
        super().ins_md1()

d1 = d()
d1.ins_md1()




