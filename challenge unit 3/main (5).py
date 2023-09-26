






class Student:

   def __init__(self, name, roll_number,cgpa):
    self.name=name
    self.roll_number=roll_number
    self.cgpa =cgpa


def sort_Students(student_list): 
  
  sorted_students=sorted(student_list, key=lambda student: student.cgpa, reverse = True)


  return sorted_students



Students=[
  Student("nivetha","A123",7.8),
  Student("sruthi", "A124", 8.9),
  Student("divya", "A125",9.1),
  Student("arya", "A126",9.9),
]


sorted_students = sort_Students(Students)


for Student in sorted_students:
  print("Name: {}, Roll number:{},Cgpa:{}".format(Student.name, 
                                                  Student.roll_number, Student.cgpa))
