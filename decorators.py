class MyClass:

    class_name = "Mahavir"

    def __init__(self,version) -> None:
        self.version = version
    
    @staticmethod
    def static_method():
        print(f'This is the static method ')

    @classmethod
    def cls_method(clf,ag):
        print("This is the class method",ag)


sl = MyClass(15)
#print(MyClass.static_method())
# print(sl.class_name)
#sl.cls_method(23)
sl.cls_method(23)

sl2 = MyClass(50)
print(MyClass.static_method())
#print(sl.class_name)
#sl2.cls_method(45)