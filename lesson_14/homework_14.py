# Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
# Створіть об'єкт цього класу, представляючи студента.
# Потім додайте метод до класу "Студент", який дозволяє змінювати середній бал студента.
# Виведіть інформацію про студента та змініть його середній бал.


class Student:
    def __init__(self, name:str, last_name:str, age:int, average_score:float):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.average_score = average_score

    def edit_average_score(self, changed_aver_score:float):
        self.average_score = changed_aver_score

    def __str__(self):
        return (f"The student {self.name} {self.last_name} is {self.age} years old,"
                f" and his average score is {self.average_score}")

student = Student("Pavlo", "Monne", 19, 95.5)
print(f"Original data:\n{student}")
student.edit_average_score(70.8)
print(f"Data after changing:\n{student}")