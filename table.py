class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

def sort_and_print_employees(employees, sort_param):
    if sort_param == 1:
        sorted_employees = sorted(employees, key=lambda x: x.age)
        print("Sorted by Age:")
    elif sort_param == 2:
        sorted_employees = sorted(employees, key=lambda x: x.name)
        print("Sorted by Name:")
    elif sort_param == 3:
        sorted_employees = sorted(employees, key=lambda x: x.salary)
        print("Sorted by Salary:")
    else:
        print("Invalid sorting parameter.")
        return

    print("Employee ID\tName\tAge\tSalary (PM)")
    for emp in sorted_employees:
        print(f"{emp.emp_id}\t\t{emp.name}\t{emp.age}\t{emp.salary}")

if __name__ == "__main__":
    employees = [
        Employee("161E90", "Ramu", 35, 59000),
        Employee("171E22", "Tejas", 30, 82100),
        Employee("171G55", "Abhi", 25, 100000),
        Employee("152K46", "Jaya", 32, 85000)
    ]

    print("Choose sorting parameter:")
    print("1. Age")
    print("2. Name")
    print("3. Salary")
    sorting_param = int(input("Enter your choice: "))

    sort_and_print_employees(employees, sorting_param)
