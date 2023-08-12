import random
from uuid import uuid4


departments = ["IT", "HR", "Sales", "Marketing", "Finance", "Legal", "Operations", "R&D", "Customer Service", "Production"]
employee_joining_year =['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017']
office_locations = ['New York', 'San Francisco', 'London', 'Paris', 'Tokyo', 'Sydney', 'Singapore', 'Hong Kong', 'Mumbai', 'Sao Paulo']



def make_employee():
    employee_id = str(uuid4())
    department = random.choice(departments)
    joining_year = random.choice(employee_joining_year)
    office_location = random.choice(office_locations)
    employee_salary = random.randint(50000, 500000)
    employee = {
        'employee_id': employee_id,
        'department': department,
        'joining_year': joining_year,
        'employee_salary': employee_salary,
        'office_location': office_location
    }
    return employee


