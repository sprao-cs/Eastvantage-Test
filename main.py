from EMS.employee import Employee
from EMS.department import Department

from pyfiglet import figlet_format

company = {}
dept_obj = Department()
emp_obj = Employee()

def add_department(department):
    if department.name in company:
        raise ValueError(f"Department with name '{department.name}' already exists")
    company[department.name] = department

def remove_department(department_name):
    del company[department_name]

def get_dept_list():
    print_list = [f"\t[:] {dept}" for dept in company.keys()]
    dept_list = list(company.keys())
    return print_list, dept_list

def display_departments():
    for department_name, department in company.items():
        print(f"{department_name}: {department}")

def create_default_departments(dept_obj):
    list_of_depts = ["IT", "Development", "Testing", "Engineering", "Manufacturing", "Sales"]

    for dept in list_of_depts:
        dep_obj = Department(dept)
        add_department(dep_obj)

def add_employee():
    print("[*] Please fill out the required details to Create Record of an Employee\n")
    emp_name = input("[+] Please Enter the Employee's Name: ")
    emp_id = input("[+] Please Enter the Employee's ID: ")
    emp_title = input("[+] Please Enter the Employee's Title: ")

    print(f'{":"*50}\n')
    dept_print, dept_list = get_dept_list()
    print("\n".join(dept_print))
    print(f'\n{":"*50}')
    while True:
        emp_dept = input("\n[+] Please Enter the Employee's Department: ")
        if emp_dept not in dept_list:
            print(f"[X] ERROR: {emp_dept} is not in our Departments. Please Try Again with Valid Dept name.")
        else:
            break

    emp_obj = Employee(emp_name, emp_id, emp_title, emp_dept)
    department = company.get(emp_dept)
    department.add_employee(emp_obj)
    print(f"[-] Employee '{emp_name}' registered in the {emp_dept} department")

def display_employees():
    for department_name, department in company.items():
        employees = department.list_employees()

        if len(employees) != 0:
            print(f"\n[-] Department: {department_name}")
            max_name_width = max(len(emp['name']) for emp in employees)
            header_string= f"| {'Name':^{max_name_width}} | {'ID':^{10}} | {'Title':^{20}} |"
            print(header_string + '\n' + '-'*len(header_string))

            for emp in employees:
                print(f"| {emp['name']:^{max_name_width}} | {emp['id']:^{10}} | {emp['title']:^{20}} |")
            
        else:
            continue
            # print("[X] Sorry! Currently there is no Employees List available for this Department.")

def remove_employee_by_id():
    employee_id = input("[+] Please Enter the Employee's ID to be removed: ")

    for department_name, department in company.items():
        emp_list = department.list_employees()
        if employee_id in [emp['id'] for emp in emp_list]:
        # if employee_id in department.list_employees():
            department.remove_employee(employee_id)
            print(f"[-] Employee with ID '{employee_id}' removed from the {department_name} department")
            return
    print(f"[X] ERROR: Employee with ID '{employee_id}' not found")

def print_header():
    header = figlet_format("   E M S   ", font="banner3-D")
    print(header)

def user_menu():
    while True:
        print("\n** Welcome to the Employee Management System **\n")
        print("""
        [1] Add Employee
        [2] Remove Employee
        [3] Display List of Employees
        [4] Display List of Departments
        [0] Exit
        """)

        choice = int(input("[*] Please Select your option from the Above: "))

        match choice:
            case 1:
                add_employee()
            case 2:
                remove_employee_by_id()
            case 3:
                display_employees()
            case 4:
                display_departments()
            case 0:
                print("Thankyou! Have a nice day :)")
                break
            case default:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    print_header()
    create_default_departments(dept_obj)
    user_menu()