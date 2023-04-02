# Nama   : Zidan Khoirul Rizki
# NIM    : 210511049
# Kelas  : R2
# Matkul : Pemrogaman Berorientasi Objek 2

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def compute_salary(self):
        pass


class HourlyEmployee(Employee):
    def __init__(self, name, salary, hours):
        super().__init__(name, salary)
        self.hours = hours

    def compute_salary(self):
        return self.salary * self.hours


class SalariedEmployee(Employee):
    def compute_salary(self):
        return self.salary / 12


hourly_employee = HourlyEmployee("John Cena", 20, 160)
salaried_employee = SalariedEmployee("Ferdy Sambo", 60000)

# Output: John Cena gaji: 3200
print(hourly_employee.name, "gaji:", hourly_employee.compute_salary())
# Output: Ferdy Sambo gaji: 5000.0
print(salaried_employee.name, "gaji:", salaried_employee.compute_salary())
