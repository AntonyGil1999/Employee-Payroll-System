from company import Company


def input_str(prompt: str):
    # Get non-empty string input from user
    while True:
        val = input(prompt).strip()
        if val:
            return val
        print("Empty input, please try again.")

def input_int(prompt: str):
    # Get integer input from user
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")

def input_float(prompt: str):
    # Get float input from user
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number (e.g., 1500 or 18.5).")

def display_menu():
    # Show menu options
    print("\n----- Menu -----")
    print("1. Add a full-time employee")
    print("2. Add a part-time employee")
    print("3. Add an apprentice")
    print("4. Display employee list")
    print("5. Calculate all salaries")
    print("6. Quit")

def run_menu(company: Company):
    # Main interactive menu loop
    while True:
        display_menu()
        choice = input("Choice: ").strip()

        if choice == "1":
            name = input_str("Name: ")
            id = input_int("ID (integer): ")
            monthly_salary = input_float("Monthly salary: ")
            company.add_fulltime_employee(name=name, id=id, monthly_salary=monthly_salary)
            print("Full-time employee added.")
        elif choice == "2":
            name = input_str("Name: ")
            id = input_int("ID (integer): ")
            nb_hours = input_float("Hours per month: ")
            hourly_salary = input_float("Hourly salary: ")
            company.add_PartialTime_employee(name=name, id=id, nb_hours_per_month=nb_hours, hourly_salary=hourly_salary)
            print("Part-time employee added.")
        elif choice == "3":
            name = input_str("Name: ")
            id = input_int("ID (integer): ")
            company.add_apprentice_employee(name=name, id=id)
            print("Apprentice added.")
        elif choice == "4":
            company.display_employees()
        elif choice == "5":
            company.calculate_all_salaries()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")