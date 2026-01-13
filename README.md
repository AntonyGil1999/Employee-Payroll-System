# Employee Payroll System

Python Employee Payroll System for Politechnika Krakowska

## 👔 Payroll Management System

A Python object-oriented application for managing employees, including salary calculation, employee types, and company operations.


## 📋 Project Description

This project is a command-line application that simulates an employee payroll management system. It allows users to:

-  Manage different types of employees (Full-Time, Part-Time, Apprentice)
- Calculate salaries automatically based on employee type
- Display employee lists and detailed salary breakdowns
- Support multiple companies and multiple ways to add employees

## 🎯 Features

- **Interactive Menu**: User-friendly command-line interface to add employees without modifying code
- **Flexible Employee Management**: Add employees individually or in batches; create employees directly with different types
- **Salary Calculation System**: Full-time, part-time, and apprentice employees calculated according to specific rules
- **User-Friendly Output**: Clear console output with working hours and salary details
- **Company Operations**: Manage multiple companies, display employee lists, calculate all salaries at once
- **Object-Oriented Principles**: Inheritance, polymorphism, abstraction, encapsulation
- **Type Safety**: Type hinting for better readability
- **Good Practices**: Avoid mutable default arguments


## 🛠️ Technologies Used

This project demonstrates the following Python concepts:

- **Object-Oriented Programming**: Classes and objects
- **Inheritance**: Employee subclasses inherit from abstract Employee class
- **Polymorphism**: `calculate_salary()` method implemented differently per employee type
- **Abstraction**: Employee base class defines a contract for subclasses
- **Control Structures**: Loops and conditionals
- **Type Hinting**: For better code clarity and IDE support
- **List Management**: Append, extend, and iterate over lists
- **String Formatting**: F-strings for clean output


## 📁 Project Structure

```
.
├── Project.py                                    # Main entry point
├── employee.py                                   # Employee classes
├── company.py                                    # Company management
├── tools.py                                      # Utilities and menu
├── README.md                                     # Documentation
├── UML Projet Python.png                         # UML diagram
├── Poster project.jpeg                           # Project poster
├── GIL Antony Projet Python Employee...pdf       # Full report
└── System_Anatomy_A_Payroll_Case_Study.pdf      # Additional resource
```


## 🚀 Execution

### Prerequisites

- Python 3.6 or higher
- No external libraries required

### Run the project

```bash
python Project.py
```



## 💻 Usage

Once the program is running, you will see the demo data, and then an interactive menu will appear:

```
----- Menu -----
1. Add a full-time employee
2. Add a part-time employee
3. Add an apprentice
4. Display employee list
5. Calculate all salaries
6. Quit
Choice: _
```

### Menu Options

- **Option 1**: Add a full-time employee (requires name, ID, monthly salary)
- **Option 2**: Add a part-time employee (requires name, ID, hours per month, hourly salary)
- **Option 3**: Add an apprentice (requires name, ID only)
- **Option 4**: Display the list of all employees in the company
- **Option 5**: Calculate salaries for all employees
- **Option 6**: Exit the program

### Programmatic Usage

You can also use the classes directly in Python code:

```python
company.add_fulltime_employee("Cocotte", 1402, 3000)
company.add_PartialTime_employee("Coco", 1408, 130, 18)
company.display_employees()
company.calculate_all_salaries()
```



## 📊 UML Class Diagram

```
[See UML Projet Python.png]
```



## 👨‍💻 Author

**GIL Antony**

* GitHub: [@AntonyGil1999](https://github.com/AntonyGil1999)
* Project Link: [Employee Payroll System](https://github.com/AntonyGil1999/Employee-Payroll-System)



## 📝 License

This project was created as part of the Python Programming course at Politechnika Krakowska im. Tadeusza Kościuszki.



## 🙏 Acknowledgments

* Course instructor: Marcin Pawlik
* Python Programming course
* Politechnika Krakowska im. Tadeusza Kościuszki
* Python official documentation
