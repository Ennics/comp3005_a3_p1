from database import *

def main():
    # Loop to display menu and handle user input
    while True:
        print("\n1. Display all students")
        print("2. Add a new student")
        print("3. Update student email")
        print("4. Delete a student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        # Option to display all students
        if choice == '1':
            getAllStudents()
        # Option to add a new student
        elif choice == '2':
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            email = input("Enter email: ")
            enrollment_date = input("Enter enrollment date (YYYY-MM-DD): ")
            addStudent(first_name, last_name, email, enrollment_date)
        # Option to update student email
        elif choice == '3':
            student_id = input("Enter student ID: ")
            new_email = input("Enter new email: ")
            updateStudentEmail(student_id, new_email)
        # Option to delete a student
        elif choice == '4':
            student_id = input("Enter student ID: ")
            deleteStudent(student_id)
        # Option to exit the program
        elif choice == '5':
            break
        # Handling invalid input
        else:
            print("Invalid choice. Please try again.")

main()
