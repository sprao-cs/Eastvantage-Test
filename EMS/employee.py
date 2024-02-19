class Employee:
    def __init__(self, name=None, id=None, title=None, department=None):
        self.name = name
        self.id = id
        self.title = title
        self.department = department

    def get_details(self):
        return {
            "name": self.name,
            "id": self.id,
            "title": self.title,
            "department": self.department,
        }
    
    def __str__(self):
        return f"{self.name} ({self.id})"
    
