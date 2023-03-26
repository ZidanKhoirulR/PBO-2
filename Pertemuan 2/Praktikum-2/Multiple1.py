# Nama   : Zidan Khoirul Rizki
# NIM    : 210511049
# Kelas  : R2
# Matkul : Pemrogaman Berorientasi Objek 2


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Employee:

    def __init__(self, salary, job_title):
        self.salary = salary
        self.job_title = job_title

    def show_info(self):
        print("Salary:", self.salary)
        print("Job Title:", self.job_title)


class Manager(Person, Employee):

    def __init__(self, name, age, salary, job_title, department):
        Person.__init__(self, name, age)
        Employee.__init__(self, salary, job_title)
        self.department = department
        
    def show_info(self):
        Person.show_info(self)
        Employee.show_info(self)
        print("Department:", self.department)


my_manager = Manager("John Doe", 30, 5000, "Manager", "IT")
my_manager.show_info()