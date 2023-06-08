class Parent:
    def __init__(self,name, age, hair_color):
        self.name = name
        self.age = age
        self.hair_color = hair_color

#inheritance    
class Child(Parent):
    def __init__(self, name, age, hair_color):
        super().__init__(name, age, hair_color)


p1 = Parent("Ali",30,"black")
ch = Child('Asif',5,"black")
print("Father name is",p1.name, "and his child name is",ch.name, "father age is",p1.age, "and his son age is ", ch.age, ".")
