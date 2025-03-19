#Students' Marks and Ranking Management System


student_marks = {}

def add_student(name, marks):
    student_marks[name] = marks
    print(f"Added {name} with {marks} marks.")

def update_student(name, marks):
    if name in student_marks:
        student_marks[name] = marks
        print(f"{name}'s marks has been updated to {marks}.")
    else:
        print(f"{name} not found!")

def delete_student(name):
    if name in student_marks:
        del student_marks[name]
        print(f"{name}'s name has been successfully deleted from the grade list.")
    else:
        print(f"{name} not found!")

def display_all_students():
    if student_marks:
        sorted_students = sorted(student_marks.items(), key=lambda x: x[1], reverse=True)
        
        print("\nRankings of students:")
        rank = 1
        for name, marks in sorted_students:
            print(f"Rank {rank}: {name} with {marks} marks")
            rank += 1
    else:
        print("No students found.")

def main():
    while True:
        print("\nStudent Marks and Rank Management System.")
        print("1. Add student.")
        print("2. Update student's marks")
        print("3. Delete student's name from grade list.")
        print("4. View all students and their ranks.")
        print("5.Exit.")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter student name: ")
            marks = float(input("Enter student marks: "))
            add_student(name, marks)

        elif choice == 2:
            name = input("Enter student name: ")
            marks = float(input("Enter student marks: "))
            update_student(name, marks)

        elif choice == 3:
            name = input("Enter student name: ")
            delete_student(name)

        elif choice == 4:
            display_all_students()

        elif choice == 5:
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")
            
main()
