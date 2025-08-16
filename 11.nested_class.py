# a class present in inside of another class call nested class

class outer():

    def __init__(self):
        print("this is outer class constructor")

        class inner():

            def __init__(self):
                print("this is inside constructor")
        

#obj creation for outer

out=outer()

#there is two way crate the object ouside for inner class

#1 war --using outer object refereance
in_obj=out.inner()

#2 using class name

inn_obj=outer.inner()

