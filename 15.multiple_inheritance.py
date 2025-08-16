#multiple class inherit by one class

class a():
    name="vimalathithan"

class b():
    age=36
class c(a,b):
    pass


print(c.name)
print(c.age)