# Dictionaries for students and categories
students = {}
categories = {}


def generateUniqueID(item_dict):
  if item_dict:
    return max(item_dict.keys()) + 1
  else:
    return 1

# add student fn
def addStudent():
  firstName = input("Enter student's first name: ")
  lastName = input("Enter student's last name: ")
  studentID = generateUniqueID(students)
  students[studentID] = {
    'firstName': firstName,
    'lastName': lastName,
    'assignements': []
  }
  print(f"Student {firstName} {lastName} added with ID {studentID}.")

def listStudents():
  if not students:
    print("No students found.")
  else:
    print("\nStudent Roster:")
    for studentID, studentData in students.items():
      print(f"ID: {studentID}, Name: {studentData['firstName']} {studentData['lastName']}")

  
def mainMenu():
    while True:
      print("\nMain Menu:")
      print("1. Add Student")
      print("2. List All Students")
      print("3. Exit")
      
      choice = input("Choose an option: ")
      if choice == '1':
        addStudent()
      elif choice == '2':
        listStudents()
      elif choice == '3':
        print("Exiting program...")
        break
      else:
        print("Please choose a valid option.")
        
# Run program
mainMenu()