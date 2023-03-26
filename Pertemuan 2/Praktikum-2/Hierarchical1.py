# Nama   : Zidan Khoirul Rizki
# NIM    : 210511049
# Kelas  : R2
# Matkul : Pemrogaman Berorientasi Objek 2


class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


class Manager(Employee):

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display_info(self):

        super().display_info()
        print("Department:", self.department)


class Engineer(Employee):

    def __init__(self, name, salary, skill):
        super().__init__(name, salary)
        self.skill = skill

    def display_info(self):
        super().display_info()
        print("Skill:", self.skill)


employee1 = Employee("John Doe", 5000)
manager1 = Manager("Jane Smith", 7000, "Marketing")
engineer1 = Engineer("Bob Johnson", 6000, "Python")


employee1.display_info() # Output: Name: John Doe, Salary: 5000
manager1.display_info() # Output: Name: Jane Smith, Salary: 7000, Department: Marketing
engineer1.display_info() # Output: Name: Bob Johnson, Salary: 6000, Skill: Python