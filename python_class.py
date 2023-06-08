class Parent:
    def __init__(self, eye_color, age, hair_color):
        self.eye_color = eye_color
        self.age = age
        self.hair_color = hair_color


# inheritance
class Child(Parent):
    def __init__(self, eye_color, age, hair_color):
        super().__init__(eye_color, age, hair_color)


p1 = Parent("brown", 30, "black")
ch = Child("brown", 5, "black")
print(
    "Father name is",
    p1.name,
    "and his child name is",
    ch.name,
    "father age is",
    p1.age,
    "and his son age is ",
    ch.age,
    ".",
)
