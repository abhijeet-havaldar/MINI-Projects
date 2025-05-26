student_grades = {}

def add_student(name, grade):
    student_grades[name] = grade
    print(f"Added {name} with a grade of {grade}")

def update_student(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"{name}'s grade has been updated to {grade}")
    else:
        print(f"{name} is not found!")

def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} has been deleted successfully!")
    else:
        print(f"{name} is not found!")

def display_all_students():
    if student_grades:
        print("\n--- All Students ---")
        for name, grade in student_grades.items():
            print(f"{name} : {grade}")
    else:
        print("No student found/added")

def main():
    while True:
        print("\nStudent Grades Management System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View All Students")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if choice == 1:
            name = input("Enter student name: ").strip()
            try:
                grade = int(input("Enter student grade: "))
                add_student(name, grade)
            except ValueError:
                print("Grade must be an integer!")

        elif choice == 2:
            name = input("Enter student name: ").strip()
            try:
                grade = int(input("Enter new grade: "))
                update_student(name, grade)
            except ValueError:
                print("Grade must be an integer!")

        elif choice == 3:
            name = input("Enter student name to delete: ").strip()
            delete_student(name)

        elif choice == 4:
            display_all_students()

        elif choice == 5:
            print("Thank You! Exiting the system.")
            break

        else:
            print("Invalid choice, please try again.")

# Run the program
main()
