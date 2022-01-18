class Student:
  def __init__(self, info_list: list[str]) -> 'Student':
      self.StLastName = info_list[0]
      self.StFirstName = info_list[1]
      self.grade = int(info_list[2])
      self.classroom = info_list[3]
      self.bus = int(info_list[4])
      self.GPA = float(info_list[5])
      self.TlastName = info_list[6]
      self.TFirstName = info_list[7]

  def __repr__(self) -> str:
      return self.StFirstName + self.bus + self.TFirstName


def read_file(filename: str):
  with open(filename) as file:
    student_list = []
    for line in file.readlines():
      info_list = []
      for word in line.split(','):
        info_list.append(word)
      student_list.append(Student(info_list))
  return student_list

def run(student_list: list['Student']):
  print("Welcome to Student Query System!")
  command = input('>>')
  command = command.split(' ')
  if (command[0] == 'Q' or command[0] == 'Quit'):
    return
  elif (command[0] == 'S' or command[0] == 'Student'):
    st_last_query(student_list, command[1])
    run(student_list)
  elif (command[0] == 'T' or command[0] == 'Student'):
    t_last_query(student_list, command[1])
    run(student_list)
  elif (command[0] == 'B' or command[0] == 'Student'):
    run(student_list)
  elif (command[0] == 'G' or command[0] == 'Student'):
    grade_query(student_list, command[1])
    run(student_list)
  elif (command[0] == 'A' or command[0] == 'Student'):
    run(student_list)
  elif (command[0] == 'I' or command[0] == 'Student'):
    run(student_list)
  else:
    print("Not a Valid Command")

def st_last_query(student_list:list['Student'], last_name:str):
  for student in student_list:
    if (student.StLastName == last_name):
      print(student.StLastName + ' ' + student.StFirstName + ' ' + str(student.grade) + ' ' + student.classroom + ' ' + student.TFirstName + ' ' +student.TlastName)

def t_last_query(student_list:list['Student'], last_name:str):
  for student in student_list:
    if (student.TlastName == last_name):
      print(student.StFirstName + '\n' + student.StLastName + '\n')

def grade_query(student_list:list['Student'], grade:str):
  for student in student_list:
    if student.grade == int(grade):
      print(student.StFirstName + '\n' + student.StLastName + '\n')

def bus_query(student_list:list['Student'], bus:str):
  for student in student_list:
    if student.bus == int(bus):
      print(student.StFirstName + '\n' + student.StLastName + '\n' + student.grade + '\n' + student.classroom + '\n')


if __name__ == '__main__':
  student_list = read_file('students.txt')
  run(student_list)