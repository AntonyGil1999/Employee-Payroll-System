class Employee:
    # Base class for all employee types
    
    def __init__(self, name, id):
        # Initialize employee with name and id
        self.name = name
        self.id = id
        self.salary = 0.0

    def display_info(self):
        # Display employee name and id
        print(f"I am {self.name} and I have id {self.id}")

    def calculate_salary(self):
        # This method must be implemented by child classes
        raise NotImplementedError("calculate_salary must be implemented in all child classes")
    
    def get_nb_hours_per_month(self):
        # This method must be implemented by child classes
        raise NotImplementedError("get_nb_hours_per_month must be implemented in all child classes")

class FullTimeEmployee(Employee):
    # Full-time employee class: works 156 hours per month
    
    def __init__(self, name, id, monthly_salary):
        # Initialize with name, id, and monthly salary
        super().__init__(name, id)   
        self.monthly_salary = monthly_salary  
        self.nb_hours_per_month = 156

    def calculate_salary(self):
        # Calculate salary for full-time employee
        self.salary = self.monthly_salary
        print(f"The salary of {self.name} (FullTimeEmployee) is {self.salary:.2f} €") 

    def get_nb_hours_per_month(self):
        # Return hours per month
        return self.nb_hours_per_month

class PartialTimeEmployee(Employee):
    # Part-time employee class: variable hours and hourly pay
    
    def __init__(self, name, id, nb_hours_per_month, hourly_salary):
        # Initialize with name, id, hours per month, and hourly rate
        super().__init__(name, id)   
        self.nb_hours_per_month = nb_hours_per_month  
        self.hourly_salary = hourly_salary  

    def calculate_salary(self):
        # Calculate salary = hours * hourly rate
        self.salary = self.nb_hours_per_month * self.hourly_salary
        print(f"The salary of {self.name} (PartialTimeEmployee) is {self.salary:.2f} €")  

    def get_nb_hours_per_month(self):
        # Return hours per month
        return self.nb_hours_per_month

class ApprenticeEmployee(Employee):
    # Apprentice class: earns 70% of minimum wage
    
    def __init__(self, name, id):
        # Initialize with name and id
        super().__init__(name, id)   
        self.minimum_wage = 1380
        self.nb_hours_per_month = 151

    def calculate_salary(self):
        # Calculate salary = minimum_wage * 0.7
        self.salary = self.minimum_wage * 0.7
        print(f"The salary of {self.name} (ApprenticeEmployee) is {self.salary:.2f} €")  

    def get_nb_hours_per_month(self):
        # Return hours per month
        return self.nb_hours_per_month