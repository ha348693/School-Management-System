from Course_Management_System import Course
class Grade:
    grades = []
    def __init__(self):
        self.student = None
        self.course = None
        self.marks = dict()
        self.grade = None
    
    @staticmethod
    def calculate_percentage(percentage):
        if percentage >= 90:
            return 'A+'
        elif percentage >= 80:
            return 'A'
        elif percentage >= 70:
            return 'B'
        elif percentage >= 60:
            return 'C'
        elif percentage >= 50:
            return 'D'
        else:
            return 'F'
    
    def enter_markstoDetermineGrade(self):
        print('Which Course You Want to Enter Marks Of: ')
        for index ,course in enumerate(Course.courses_list):
            print(f'Course No {index + 1}')
            print(f'Course Name:- {course.get_course_name()}')
            print(f'Course Code:- {course.get_course_code()}')
            print()
        
        while True:
            choice = input('Enter Your Choice:- ')
            if choice.isdigit() and 1 <= int(choice) <= len(Course.courses_list):
                break
            else:
                print('Invalid Input!!')
        
        choice = int(choice)

        self.course = Course.courses_list[choice - 1]

        for index ,student in enumerate(self.course.enrolledStudent):
            print('Which Student You Want to Enter Marks Of: ')
            print(f'Student No {index + 1}')
            print(f'Student Name:- {student.get_name()}')
            print(f'Student ID:- {student.get_user_id()}')
            print()
        
        while True:
            choice = input('Enter Your Choice:- ')
            if choice.isdigit() and 1 <= int(choice) <= len(self.course.enrolledStudent):
                break
            else:
                print('Invalid Input!!')
        
        choice = int(choice)

        self.student = self.course.enrolledStudent[choice - 1]
        
        total = 100

        while True:
            gained_marks = input(f'Enter marks of {self.course.get_course_name()}:- ')

            if gained_marks.isdigit() and 1 <= int(gained_marks) <= 100:
                break
            else:
                print('Invalid Input!!')
        
        gained_marks = int(gained_marks)

        percentage = (gained_marks / total ) * 100

        self.grade = self.calculate_percentage(percentage)
        
        for grade in Grade.grades:
            if grade.student == self.student and grade.course == self.course:
                grade.grade = self.grade
                print("Grade updated for existing student-course.")
                return
            
        Grade.grades.append(self)
    
    @staticmethod
    def show_all_students_grades():
        print('======> All Students Grades <======')
        for grade in Grade.grades:
            print(f'Student Name:- {grade.student.get_name()}')
            print(f'Student User Id:- {grade.student.get_name()}')
            print(f'Subject Name:- {grade.course.get_course_name()}')
            print(f'Subject Code:- {grade.course.get_course_code()}')
            print(f'Subject Grade Obtained:- {grade.grade}')
            print(' ')
    
    @staticmethod
    def show_specific_students_grades():
        while True:
            student_id = input('Enter Student Id you want to see grade of:- ')
            found = False
            for grade in Grade.grades:
                if student_id == grade.student.get_user_id():
                    found = True
                    print(f'Student Name:- {grade.student.get_name()}')
                    print(f'Subject Name:- {grade.course.get_course_name()}')
                    print(f'Subject Code:- {grade.course.get_course_code()}')
                    print(f'Grade Obtained:- {grade.grade}')
            if found:
                print('Student Found!! Show You His Results')
                break
            else:
                print('Student Not Found Try Again!!')