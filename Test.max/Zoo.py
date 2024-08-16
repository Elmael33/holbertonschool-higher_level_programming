from abc import ABC, abstractmethod


class Animal(ABC):
    nombre_pattes = 4
    type_animal = "Indéfini"

    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    type_animal = "Chien"

    def speak(self):
        return "Wouf"


class Cat(Animal):
    type_animal = "Chat"

    def speak(self):
        return "Miaou"


class Employee:
    employee_count = 0

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        Employee.employee_count += 1

    @staticmethod
    def total_number_of_employees():
        return Employee.employee_count

    @staticmethod
    def is_adult(age):
        return age >= 18


class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def display_animals(self):
        for animal in self.animals:
            print(f"{animal.__class__.__name__} : {animal.speak()}")

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_employees(self):
        for employee in self.employees:
            print(f"Employee: {employee.first_name}\
                  {employee.last_name}, Age: {employee.age}")


zoo = Zoo("City Zoo")
dog = Dog()
cat = Cat()
zoo.add_animal(dog)
zoo.add_animal(cat)

employee1 = Employee("Jacky", "Fripouille", 28)
employee2 = Employee("Jean", "Gentil", 22)
employee3 = Employee("Pierrot", "Peureux", 17)

zoo.add_employee(employee1)
zoo.add_employee(employee2)
zoo.add_employee(employee3)

employee1.last_name = "Fripouille"
employee2.age = 23

zoo.display_animals()
zoo.display_employees()

print(f"Total number of employees: {Employee.total_number_of_employees()}")
print(f"Jacky is an adult: {Employee.is_adult(employee1.age)}")
print(f"Pierrot is an adult: {Employee.is_adult(employee3.age)}")
