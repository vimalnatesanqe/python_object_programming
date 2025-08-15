#if you want to work with clss variable then use class methon
#we can call the class method outside of the clss by class refrence
#also we can call the function inside the class method


class cls_md():
    name="vIMathithan"
    age=36

    @classmethod
    def cls_md1_low(cls):
        print(cls.name.lower())
        cls.cls_md2_upp()
    @classmethod
    def cls_md2_upp(cls):
        print(cls.name.upper())
ref=cls_md()
ref.cls_md1_low()