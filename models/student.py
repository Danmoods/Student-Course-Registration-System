from models.person import Person

class Student(Person):
    def __init__(self, student_id, name, email, phone_number):
        super().__init__(name, email, phone_number)
        self.student_id = student_id

    def display_info(self):
        print(f"Student ID: {self.student_id}")

        super().display_info()

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "email": self.email,
            "phone_number": self.phone_number
        }
    
    def load_courses(Self):

        try:

            with open(self.courses_file, "r") as file:
                return json.load(file)
        
        except FileNotFoundError:

            return []

    def save_courses(Self, courses):

        with open(self.courses_file, "w") as file:

            json.dump(
                courses,
                file,
                indent=4
            )

    def add_course(self, course):

        courses = self.load_courses()

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