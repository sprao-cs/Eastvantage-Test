class Department:
    def __init__(self, name=None):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        return

    def remove_employee(self, employee_id):
        for employee in self.employees:
            if employee.id == employee_id:
                self.employees.remove(employee)
                return

        raise ValueError(f"Employee with ID {employee_id} not found in department {self.name}")
    
    def list_employees(self):
        employee_details = []
        for employee in self.employees:
            employee_details.append(employee.get_details())
        return employee_details
    
    def __str__(self):
        return f"{self.name} ({len(self.employees)} employees)"