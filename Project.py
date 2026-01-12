# ================================================================
# Python Project : Employee Payroll System by GIL Antony
# ================================================================

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        # print("Object constructor", self, name, id)

    def display_info(self):
        print(f"I am {self.name} and I have id {self.id}")

    def calculate_salary(self):
        raise Exception("calculate_salary must be implemented in all child classes of Employee")
    
    def get_nb_hours_per_month(self):
        raise Exception("get_nb_hours_per_month must be implemented in all child classes of Employee")

class FullTimeEmployee(Employee):
    def __init__(self, name, id, monthly_salary):
        super().__init__(name, id)   
        self.monthly_salary = monthly_salary  
        self.nb_hours_per_month = 156

    def calculate_salary(self):
         self.salary = self.monthly_salary
         print(f"The salary of {self.name} (FullTimeEmployee) is {self.salary} €") 

    def get_nb_hours_per_month(self):
        return self.nb_hours_per_month

class PartialTimeEmployee(Employee):
    def __init__(self, name, id, nb_hours_per_month, hourly_salary):
        super().__init__(name, id)   
        self.nb_hours_per_month = nb_hours_per_month  
        self.hourly_salary = hourly_salary  

    def calculate_salary(self):
         self.salary = self.nb_hours_per_month * self.hourly_salary
         print(f"The salary of {self.name} (PartialTimeEmployee) is {self.salary} €")  

    def get_nb_hours_per_month(self):
        return self.nb_hours_per_month

class ApprenticeEmployee(Employee):
    # Like the FullTime class, but earns 70% of minimum wage
    def __init__(self, name, id):
        super().__init__(name, id)   
        self.minimum_wage = 1380
        self.nb_hours_per_month = 151

    def calculate_salary(self):
         self.salary = self.minimum_wage * 0.7
         print(f"The salary of {self.name} (ApprenticeEmployee) is {self.salary:.2f} €")  

    def get_nb_hours_per_month(self):
        return self.nb_hours_per_month

class Company:    
    def __init__(self, name: str, employee_list=None):
        self.name = name
        if employee_list is not None:
            self.employee_list = employee_list
        else:
            self.employee_list = []

    def add_employee(self, emp: Employee):
         self.employee_list.append(emp)

    def add_fulltime_employee(self, name, id, monthly_salary):
        emp = FullTimeEmployee(name, id, monthly_salary)
        self.employee_list.append(emp)

    def add_PartialTime_employee(self, name, id, nb_hours_per_month, hourly_salary):
        emp = PartialTimeEmployee(name, id, nb_hours_per_month, hourly_salary)
        self.employee_list.append(emp)

    def add_apprentice_employee(self, name, id):
        emp = ApprenticeEmployee(name, id)
        self.employee_list.append(emp)

    def add_employees(self, employee_list: list):
        self.employee_list.extend(employee_list)

    def display_employees(self):
        print(f"\n*****   List of employees at {self.name}:   *****")
        for e in self.employee_list:
            e.display_info()
        print("*********************************************")

    def calculate_all_salaries(self):
        print("\n*****   Calculating employee salaries:   *****")
        for e in self.employee_list:
            e.calculate_salary()
            print(f"...for {e.get_nb_hours_per_month()} hours worked")
        print("***********************************")
         
         
# I create the company object
company = Company("Gil and Co.")

# Adding employees
company.add_employee(PartialTimeEmployee("Jérôme", 72, nb_hours_per_month=120, hourly_salary=20))
company.add_employee(FullTimeEmployee("Toto", 142, 1500))
company.add_fulltime_employee(name="Cocotte", id=1402, monthly_salary=3000)
company.add_PartialTime_employee(name="Coco", id=1408, nb_hours_per_month=130, hourly_salary=18)
company.display_employees()
company.calculate_all_salaries()

employee_list = []
employee_list.append(FullTimeEmployee("Titi", 15, 2000))
employee_list.append(ApprenticeEmployee("Tata", 18))
company2 = Company("Cora", employee_list)
company2.display_employees()
company2.calculate_all_salaries()