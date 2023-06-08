class Parent:
    def __init__(self,name, age, hair_color,hieght):
        self.name = name
        self.age = age
        self.hair_color = hair_color
        self.hieght = hieght

#inheritance    
class Child(Parent):
    def __init__(self, name, age, hair_color, hieght):
        super().__init__(name, age, hair_color, hieght)


p1 = Parent("Ali",30,"black",5.9)
ch = Child('Asif',5,"black",5.9)
print("Father name is",p1.name, "and his child name is",ch.name, "father age is",p1.age, "and his son age is ", ch.age, ".")
