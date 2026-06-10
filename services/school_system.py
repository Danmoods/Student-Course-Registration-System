import json

class SchoolSystem:
    def __init__(self):
        self.students_file = "data/students.json"
        self.courses_file = "data/courses.json"
        self.registrations_file = "data/registrations.json"

    
    def load_students(self):

        try:

            with open(self.students_file, "r") as file:

                return json.load(file)
        
        except FileNotFoundError:

            return[]
    
    def save_students(self, students):

        with open(self.students_file, "w") as file:

            json.dump(
                students,
                file,
                indent=4
            )

    def add_student(self, student):

        if not student.student_id.strip():

            print("Student ID cannot be empty.")

            return

        if not student.name.strip():

            print("Student name cannot be empty.")

            return

        if not student.email.strip():

            print("Email cannot be empty.")

            return

        if not student.phone_number.strip():

            print("Phone number cannot be empty.")

            return

        if "@" not in student.email:

            print("Invalid email address.")

            return

        students = self.load_students()

        for existing_student in students:

            if (
                existing_student["student_id"]
                ==
                student.student_id
            ):

                print(
                    "Student ID already exists."
                )

                return

        students.append(
            student.to_dict()
        )

        self.save_students(students)

        print(
            f"{student.name} saved successfully."
        )


    def view_students(self):

        students = self.load_students()

        if not students:
            print("No students found.")
            return

        for student in students:
            print("\n-----Available Students-----")

            print(f"Student ID: {student['student_id']}")
            print(f"Name: {student['name']}")
            print(f"Email: {student['email']}")
            print(f"Phone: {student['phone_number']}")

    def load_courses(self):

        try:

            with open(self.courses_file, "r") as file:

                return json.load(file)

        except FileNotFoundError:

            return []


    def save_courses(self, courses):

        with open(self.courses_file, "w") as file:

            json.dump(
                courses,
                file,
                indent=4
            )


    def add_course(self, course):

        if not course.course_id.strip():

            print("Course ID cannot be empty.")

            return

        if not course.course_name.strip():

            print("Course name cannot be empty.")

            return

        if not course.trainer_name.strip():

            print("Trainer name cannot be empty.")

            return

        if course.capacity <= 0:

            print("Capacity must be greater than zero.")

            return

        courses = self.load_courses()

        for existing_course in courses:

            if (
                existing_course["course_id"]
                ==
                course.course_id
            ):

                print(
                    "Course ID already exists."
                )

                return

        courses.append(
            course.to_dict()
        )

        self.save_courses(courses)

        print(
            f"{course.course_name} saved successfully."
        )


    def view_courses(self):

        courses = self.load_courses()

        if not courses:

            print("No courses found.")
            return

        for course in courses:

            print("\n----- Available Courses -----")

            print(
                f"Course ID: {course['course_id']}"
            )

            print(
                f"Course Name: {course['course_name']}"
            )

            print(
                f"Trainer: {course['trainer_name']}"
            )

            print(
                f"Capacity: {course['capacity']}"
            )

    def search_student(self, search_term):

        students = self.load_students()

        for student in students:

            if (
                student["student_id"].lower()
                == search_term.lower()
            ):

                print("\nStudent Found")

                print(
                    f"Student ID: {student['student_id']}"
                )

                print(
                    f"Name: {student['name']}"
                )

                print(
                    f"Email: {student['email']}"
                )

                print(
                    f"Phone: {student['phone_number']}"
                )

                return

            elif (
                student["name"].lower()
                == search_term.lower()
            ):

                print("\nStudent Found")

                print(
                    f"Student ID: {student['student_id']}"
                )

                print(
                    f"Name: {student['name']}"
                )

                print(
                    f"Email: {student['email']}"
                )

                print(
                    f"Phone: {student['phone_number']}"
                )

                return

        print("Student not found.")

    def search_course(self, search_term):

        courses = self.load_courses()

        for course in courses:

            if (
                course["course_id"].lower()
                == search_term.lower()
            ):

                print("\nCourse Found")

                print(
                    f"Course ID: {course['course_id']}"
                )

                print(
                    f"Course Name: {course['course_name']}"
                )

                print(
                    f"Trainer: {course['trainer_name']}"
                )

                print(
                    f"Capacity: {course['capacity']}"
                )

                return

            elif (
                course["course_name"].lower()
                == search_term.lower()
            ):

                print("\nCourse Found")

                print(
                    f"Course ID: {course['course_id']}"
                )

                print(
                    f"Course Name: {course['course_name']}"
                )

                print(
                    f"Trainer: {course['trainer_name']}"
                )

                print(
                    f"Capacity: {course['capacity']}"
                )

                return

        print("Course not found.")

    def load_registrations(self):
    
        try:
    
            with open(
                self.registrations_file,
                "r"
            ) as file:
    
                return json.load(file)
    
        except FileNotFoundError:
    
            return []

    def save_registrations(
        self,
        registrations
    ):
    
        with open(
            self.registrations_file,
            "w"
        ) as file:
    
            json.dump(
                registrations,
                file,
                indent=4
            )

    def register_student(
        self,
        student_id,
        course_id
    ):

        students = self.load_students()

        courses = self.load_courses()

        registrations = (
            self.load_registrations()
        )

        student = None

        for s in students:

            if s["student_id"] == student_id:

                student = s
                break

        if not student:

            print("Student not found.")
            return

        course = None

        for c in courses:

            if c["course_id"] == course_id:

                course = c
                break

        if not course:

            print("Course not found.")
            return

        current_registrations = 0

        for registration in registrations:
            if registration["course_id"] == course_id:
                
                current_registrations += 1


        if current_registrations >= course["capacity"]:

            print(
                "Registration failed. "
                "This course is already full."
            )

            return

        for registration in registrations:

            if (
                registration["student_id"]
                == student_id
                and
                registration["course_id"]
                == course_id
            ):

                print(
                    "Student already "
                    "registered."
                )

                return

        registrations.append(
            {
                "student_id": student_id,
                "course_id": course_id
            }
        )

        self.save_registrations(
            registrations
        )

        print(
            f"{student['name']} "
            f"successfully "
            f"registered for "
            f"{course['course_name']}."
        )

    def view_students_in_course(self, course_id):

        registrations = self.load_registrations()

        students = self.load_students()

        found = False

        print("\nStudents Registered:")

        for registration in registrations:

            if registration["course_id"] == course_id:

                for student in students:

                    if (
                        student["student_id"]
                        ==
                        registration["student_id"]
                    ):

                        print(
                            f"{student['student_id']} - "
                            f"{student['name']}"
                        )

                        found = True

        if not found:

            print(
                "No students registered "
                "for this course."
            )

    def view_courses_for_student(
        self,
        student_id
    ):

        registrations = (
            self.load_registrations()
        )

        courses = self.load_courses()

        found = False

        print("\nCourses Registered:")

        for registration in registrations:

            if (
                registration["student_id"]
                ==
                student_id
            ):

                for course in courses:

                    if (
                        course["course_id"]
                        ==
                        registration["course_id"]
                    ):

                        print(
                            f"{course['course_id']} - "
                            f"{course['course_name']}"
                        )

                        found = True

        if not found:

            print(
                "Student has no "
                "course registrations."
            )

    def save_data(self):
        print("Data saved Successfully.")

    def load_data(self):
        self.load_students()
        self.load_courses()
        self.load_registrations()

        print("Data load successfully.")
