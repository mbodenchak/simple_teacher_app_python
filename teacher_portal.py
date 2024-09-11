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

  
def mainMenu():
    while True:
      print("\nMain Menu:")
      print("1. Add Student")
      print("2. Exit")
      
      choice = input("Choose an option: ")
      if choice == '1':
        addStudent()
      elif choice == '2':
        print("Exiting program...")
        break
      else:
        print("Please choose a valid option.")
        
# Run program
mainMenu()