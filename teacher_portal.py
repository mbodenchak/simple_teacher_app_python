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
    'assignments': []
  }
  print(f"Student {firstName} {lastName} added with ID {studentID}.")

def listStudents():
  if not students:
    print("No students found.")
  else:
    print("\nStudent Roster:")
    for studentID, studentData in students.items():
      print(f"ID: {studentID}, Name: {studentData['firstName']} {studentData['lastName']}")

def viewStudentAssignments():
  studentID = int(input("Enter student ID: "))
  if studentID in students:
    print(f"\nAssignments for student {students[studentID]['firstName']} {students[studentID]['lastName']}:")
    if not students[studentID]['assignments']:
      print("No assignments found.")
    else:
      for assignment in students[studentID]['assignments']:
        print(f"ID: {assignment['id']}, Title: {assignment['title']}, Date: {assignment['date']}, Grade: {assignment['grade']}, Category: {assignment['category']}")
  else:
    print("Students not found.")

def addGrade():
  studentID = int(input("Enter student ID: "))
  if studentID in students:
    title = input("Enter assignment title: ")
    date = input("Enter assignment date (MM-DD-YYYY): ")
    grade = float(input("Enter grade: "))
    category = input("Enter assignment category: ").upper()
    
    assignmentID = generateUniqueID(students[studentID]['assignments'])
    students[studentID]['assignments'].append({
      'id': assignmentID,
      'title': title,
      'date': date,
      'grade': grade,
      'category': category
    })
    print(f"Assignment {title} added for student {studentID}.")
  else:
    print("Student not found.")
  
  
def mainMenu():
    while True:
      print("\nMain Menu:")
      print("1. Add Student")
      print("2. List All Students")
      print("3. View Students Assignments")
      print("4. Add Grade")
      print("5. Edit Grade")
      print("6. Delete Grade")
      print("7. Delete Student")
      print("8. Edit Gradebook Weights")
      print("9. Calculate Overall Grade")
      print("10. Exit")
      
      choice = input("Choose an option: ")
      if choice == '1':
        addStudent()
      elif choice == '2':
        listStudents()
      elif choice == '3':
        viewStudentAssignments()
      elif choice == '4':
        addGrade()
      elif choice == '5':
        print("Edit Grade")
      elif choice == '6':
        print("Delete Grade")
      elif choice == '7':
        print("Delete Student")
      elif choice == '8':
        print("Edit Gradebook Weights")
      elif choice == '9':
        print("Calculate Overall Grade")
      elif choice == '10':
        print("Exiting program...")
        break
      else:
        print("Please choose a valid option.")
        
# Run program
mainMenu()