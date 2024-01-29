# EmployeeID Name Age Salary(PM)
# 161E90 Ramu 35 59000
# 171E22 Tejas 30 82100
# 171G55 Abhi 25 100000
# 152K46 Jaya 32 85000

class Employee:
    def __init__(self, id, name, age, salary):
        self.id = id
        self.name = name
        self.age = age
        self.salary = salary

    @staticmethod
    def from_string(data_str):
        id, name, age, salary = data_str.split()
        return Employee(id, name, int(age), int(salary))

class EmployeeDatabase:
    def __init__(self, data_strs):
        self.employees = [Employee.from_string(data_str) for data_str in data_strs]

    def sort_by(self, attribute):
        self.employees.sort(key=lambda emp: getattr(emp, attribute))

def main():
    data_strs = [
        "161E90 Ramu 35 59000",
        "171E22 Tejas 30 82100",
        "171G55 Abhi 25 100000",
        "152K46 Jaya 32 85000"
    ]

    db = EmployeeDatabase(data_strs)

    while True:
        print("Choose the sorting parameter (1. Age, 2. Name, 3. Salary, 4. Exit):")
        choice = input()

        if choice == '1':
            db.sort_by('age')
        elif choice == '2':
            db.sort_by('name')
        elif choice == '3':
            db.sort_by('salary')
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please choose again.")
            continue

        for emp in db.employees:
            print(f"{emp.id} {emp.name} {emp.age} {emp.salary}")

if __name__ == "__main__":
    main()