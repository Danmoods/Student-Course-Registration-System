from models.student import Student
from models.course import Course
from services.school_system import SchoolSystem


system = SchoolSystem()

while True:

    print("\n===== Student Course Registration System =====")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Add Course")
    print("5. View Courses")
    print("6. Register Student to Course")
    print("7. View Students in a Course")
    print("8. View Courses for a Student")
    print("9. Search Course")
    print("10. Save Data")
    print("11. Load Data")
    print("0. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":

        student_id = input("Student ID: ")
        name = input("Name: ")
        email = input("Email: ")
        phone_number = input("Phone Number: ")

        student = Student(
            student_id,
            name,
            email,
            phone_number
        )

        system.add_student(student)

    elif choice == "2":

        system.view_students()

    elif choice == "3":

        search_term = input(
            "Enter Student ID or Name: "
        )

        system.search_student(
            search_term
        )

    elif choice == "4":

        course_id = input(
            "Course ID: "
        )

        course_name = input(
            "Course Name: "
        )

        trainer_name = input(
            "Trainer Name: "
        )

        try:

            capacity = int(
                input("Capacity: ")
            )

            course = Course(
                course_id,
                course_name,
                trainer_name,
                capacity
            )

            system.add_course(course)

        except ValueError:

            print(
                "Capacity must be a number."
            )

    elif choice == "5":

        system.view_courses()

    elif choice == "6":

        student_id = input(
            "Student ID: "
        )

        course_id = input(
            "Course ID: "
        )

        system.register_student(
            student_id,
            course_id
        )

    elif choice == "7":

        course_id = input(
            "Course ID: "
        )

        system.view_students_in_course(
            course_id
        )

    elif choice == "8":

        student_id = input(
            "Student ID: "
        )

        system.view_courses_for_student(
            student_id
        )

    elif choice == "9":
        search_term = input(
            "Enter Course ID or Name:"
        )

        system.search_course(
            search_term
        )

    elif choice == "10":
        system.save_data()

    elif choice == "11":
        system.load_data()

    elif choice == "0":

        print("Goodbye! Na Watu Wasome...(-__-)")
        break

    else:

        print(
            "Invalid option. "
            "Please try again."
        )

