# Given list of tuples (name, surname, age, profession, City location)
# 1 - Add your new record at the beginning of the given list
# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result

people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]
people_records.insert(0,("Maria", "Shevchenko", 31, "QA", "Kyiv")) # adding a new record at the beginning of the list
print(people_records)

people_records[1], people_records[5] = people_records[5], people_records[1] # swapping elements at positions 1<->5
print(people_records)

if people_records[6][2] >= 30 and people_records[10][2] >= 30 and people_records[13][2] >= 30: # checking if all people at indexes 6, 10, and 13 are 30 or older
    print("Everyone at indexes 6, 10, and 13 in the list is 30 or older")
else:
    print("Not all people at indexes 6, 10, and 13 in the list are 30 years old or older")