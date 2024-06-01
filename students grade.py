class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        if subject not in self.grades:
            self.grades[subject] = [grade]
        else:
            self.grades[subject].append(grade)

    def calculate_average_grade(self):
        total_grades = 0
        total_subjects = 0
        for subject, grades in self.grades.items():
            total_grades += sum(grades)
            total_subjects += len(grades)
        if total_subjects == 0:
            return 0
        else:
            return total_grades / total_subjects

    def calculate_letter_grade(self):
        average = self.calculate_average_grade()
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'

    def display_info(self):
        print(f"Student Name: {self.name}")
        print("Grades:")
        for subject, grades in self.grades.items():
            print(f"{subject}: {grades}")
        print(f"Average Grade: {self.calculate_average_grade()}")
        print(f"Letter Grade: {self.calculate_letter_grade()}")

def main():
    student_name = input("Enter student's name: ")
    student = Student(student_name)

    while True:
        subject = input("Enter subject (or type 'done' to finish): ")
        if subject.lower() == 'done':
            break
        grade = float(input(f"Enter grade for {subject}: "))
        student.add_grade(subject, grade)

    student.display_info()

if __name__ == "__main__":
    main()
