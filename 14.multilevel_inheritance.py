# continuesly one class inherit another class

#grand parent- parent-child

class a():
    name="vimalathithan"
class b(a):
    age=36
class c(b):
    #this c class can able to acees the members a, b both
    pass

c_obj=c()
print(c_obj.name)
print(c_obj.age)

