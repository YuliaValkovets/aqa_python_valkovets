# Створіть клас Employee, який має атрибути name та salary. Далі створіть два класи, Manager
# та Developer, які успадковуються від Employee. Клас Manager повинен мати додатковий атрибут
# department, а клас Developer - атрибут programming_language.
# Тепер створіть клас TeamLead, який успадковується як від Manager, так і від Developer.
# Цей клас представляє керівника з команди розробників. Клас TeamLead повинен мати всі атрибути
# як Manager (ім'я, зарплата, відділ),  а також атрибут team_size, який вказує на кількість
# розробників у команді, якою керує керівник.)
# Напишіть тест, який перевіряє наявність атрибутів з Manager та Developer у класі TeamLead

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        self.department = department

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        Employee.__init__(self, name,salary)
        self.programming_language = programming_language

class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        self.team_size = team_size


team_lead = TeamLead("Ivan", 2000, "IT", "Python", 5)
print(f'name: {team_lead.name},\nsalary: {team_lead.salary},\ndepartment: {team_lead.department},'
      f'\nprogramming language: {team_lead.programming_language},\nteam size: {team_lead.team_size}' )