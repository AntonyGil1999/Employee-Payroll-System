# Employee Payroll System - Main program

from employee import Employee, ApprenticeEmployee, FullTimeEmployee, PartialTimeEmployee
from company import Company
from tools import run_menu


if __name__ == "__main__":
    # Create company
    company = Company("Gil and Co.")

    # Add demo employees - Method 1: Direct objects
    company.add_employee(PartialTimeEmployee("Jérôme", 72, nb_hours_per_month=120, hourly_salary=20))
    company.add_employee(FullTimeEmployee("Toto", 142, 1500))

    # Method 2: Using convenience methods
    company.add_fulltime_employee(name="Cocotte", id=1402, monthly_salary=3000)
    company.add_PartialTime_employee(name="Coco", id=1408, nb_hours_per_month=130, hourly_salary=18)

    # Method 3: Add multiple employees at once
    employee_list = []
    employee_list.append(FullTimeEmployee("Titi", 15, 2000))
    employee_list.append(ApprenticeEmployee("Tata", 18))
    company.add_employees(employee_list)

    # Show demo data
    company.display_employees()
    company.calculate_all_salaries()

    # Run interactive menu
    run_menu(company)