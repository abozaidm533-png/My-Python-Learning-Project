class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []
    
    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.grades.append(grade)
        else:
            print(f"Invalid grade {grade}. Grade must be between 0 and 100.")
    
    def get_average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)
    
    def get_result(self):
        average = self.get_average()
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Grades: {self.grades}")
        print(f"Average: {self.get_average():.2f}")
        print(f"Result: {self.get_result()}")


class StudentManagementSystem:
    def __init__(self):
        self.students = []
    
    def add_student(self, name, student_id):
        student = Student(name, student_id)
        self.students.append(student)
        return student
    
    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None
    
    def get_class_average(self):
        if len(self.students) == 0:
            return 0
        total_average = sum(student.get_average() for student in self.students)
        return total_average / len(self.students)
    
    def display_all_students(self):
        if len(self.students) == 0:
            print("No students in the system.")
            return
        for student in self.students:
            student.display_info()
            print("-" * 30)
    
    def get_top_performer(self):
        if len(self.students) == 0:
            return None
        return max(self.students, key=lambda s: s.get_average())


if __name__ == "__main__":
    system = StudentManagementSystem()
    
    student1 = system.add_student("Ahmed", 1)
    student1.add_grade(95)
    student1.add_grade(88)
    student1.add_grade(92)
    
    student2 = system.add_student("Fatima", 2)
    student2.add_grade(78)
    student2.add_grade(85)
    student2.add_grade(82)
    
    student3 = system.add_student("Omar", 3)
    student3.add_grade(65)
    student3.add_grade(70)
    student3.add_grade(68)
    
    print("=== All Students ===\n")
    system.display_all_students()
    
    print(f"\nClass Average: {system.get_class_average():.2f}")
    
    top = system.get_top_performer()
    print(f"\nTop Performer: {top.name} with average {top.get_average():.2f}")
