
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")



class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)  
        self.__employee_id = employee_id   
        self.__salary = salary            
    
   
    def get_salary(self):
        return self.__salary
    
    def set_salary(self, salary):
        self.__salary = salary

    def get_id(self):
        return self.__employee_id
    
    def set_id(self, emp_id):
        self.__employee_id = emp_id

    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, ID: {self.__employee_id}, Salary: ${self.__salary}")



class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary) 
        self.department = department
    
    def display(self):  
        print(f"Name: {self.name}, Age: {self.age}, ID: {self.get_id()}, Salary: ${self.get_salary()}, Department: {self.department}")


# ===================== MENU =====================

persons = []
employees = []
managers = []

while True:
    print("\n--- Python OOP Project: Employee Management System ---")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Show Details")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        p = Person(name, age)
        persons.append(p)
        print(f"Person created with name: {name} and age: {age}.")

    elif choice == "2":
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        emp_id = input("Enter Employee ID: ")
        salary = int(input("Enter Salary: "))
        e = Employee(name, age, emp_id, salary)
        employees.append(e)
        print(f"Employee created with name: {name}, age: {age}, ID: {emp_id}, and salary: ${salary}.")

    elif choice == "3":
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        emp_id = input("Enter Employee ID: ")
        salary = int(input("Enter Salary: "))
        dept = input("Enter Department: ")
        m = Manager(name, age, emp_id, salary, dept)
        managers.append(m)
        print(f"Manager created with name: {name}, age: {age}, ID: {emp_id}, salary: ${salary}, and department: {dept}.")

    elif choice == "4":
        print("\nChoose details to show:")
        print("1. Person")
        print("2. Employee")
        print("3. Manager")
        sub_choice = input("Enter your choice: ")

        if sub_choice == "1":
            for p in persons:
                p.display()
        elif sub_choice == "2":
            for e in employees:
                e.display()
        elif sub_choice == "3":
            for m in managers:
                m.display()
        else:
            print("Invalid choice!")

    elif choice == "5":
        print("Exiting the system. All resources have been freed.\nGoodbye!")
        break
    else:
        print("Invalid choice, try again!")
