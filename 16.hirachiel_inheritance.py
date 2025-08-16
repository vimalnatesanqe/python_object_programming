#difrrent child inherit from 1 parent 

class a():
    name="vimal"
    def __init__(self):
        self.age=30
        self.location='nkl'
class b(a):
    pass
class c(a):
    pass

print(c.name)
print(b.name)
b_o=b()
c_o=c()
print(b_o.age,b_o.location)
print(c_o.age,c_o.location)