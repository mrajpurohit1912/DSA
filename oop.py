class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name
    
    @name.setter
    def set_name(self,new_name):
        self._name = new_name

    @property
    def age(self):
        return self._age
    
    @age.setter
    def set_age(self,new_age):
        if new_age < 90 and new_age > 18:
            self._age = new_age
        else:
            raise ValueError("Pleas Enter valid age")
        
sl = Person("Mahavir",25)

print(sl._name)
print(sl._age)

sl._name = "Ram"
sl._age = 189

print(sl._name)
print(sl._age)