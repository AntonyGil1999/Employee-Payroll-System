from employee import Employee, ApprenticeEmployee, FullTimeEmployee, PartialTimeEmployee

class Company:    
    # Company class to manage employees
    
    def __init__(self, name: str, employee_list=None):
        # Initialize company with name and optional list of employees
        self.name = name
        self.employee_list = employee_list if employee_list is not None else []

    def add_employee(self, emp: Employee):
        # Add an employee object to the company
        self.employee_list.append(emp)

    def add_fulltime_employee(self, name, id, monthly_salary):
        # Create and add a full-time employee
        emp = FullTimeEmployee(name, id, monthly_salary)
        self.employee_list.append(emp)

    def add_PartialTime_employee(self, name, id, nb_hours_per_month, hourly_salary):
        # Create and add a part-time employee
        emp = PartialTimeEmployee(name, id, nb_hours_per_month, hourly_salary)
        self.employee_list.append(emp)

    def add_apprentice_employee(self, name, id):
        # Create and add an apprentice
        emp = ApprenticeEmployee(name, id)
        self.employee_list.append(emp)

    def add_employees(self, employee_list: list):
        # Add multiple employees at once
        self.employee_list.extend(employee_list)

    def display_employees(self):
        # Display all employees in the company
        print(f"\n*****   List of employees at {self.name}:   *****")
        for e in self.employee_list:
            e.display_info()
        print("*********************************************")

    def calculate_all_salaries(self):
        # Calculate salary for all employees
        print("\n*****   Calculating employee salaries:   *****")
        for e in self.employee_list:
            e.calculate_salary()
            print(f"...for {e.get_nb_hours_per_month()} hours worked")
        print("***********************************")