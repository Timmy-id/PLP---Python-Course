class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f'Hello, I am {self.name}, a {self.gender} and I am {self.age} years old.')


person1 = Person('Timi', 29, 'male')

person1.introduce()