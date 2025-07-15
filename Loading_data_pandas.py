import csv
from User_Management_System import Student ,Teacher ,Admin
from Course_Management_System import Course
from Grade_Management_System import Grade
from Attendence_Management_System import AttendanceSystem
from TimeTable_Management_System import TimeTable

class FileManager:
    @staticmethod
    def saveUserDataToCsv(filename ,user_list):
        with open(filename ,mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name' ,'UserID' ,'Email' ,'Password' ,'Role'])

            for user in user_list:
                writer.writerow([user.get_name(), user.get_user_id(), user.get_email(), user.get_password(), user.role])
    
    @staticmethod
    def loadUserDataFromCsv(filename ,user_list):
        users = []
        try:
            with open(filename ,mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    role = row['Role']

                    if role == 'Student':
                        user = Student()
                        Student.all_students.append(user)
                    
                    elif role == 'Teacher':
                        user = Teacher()
                        Teacher.all_teachers.append(user)
                    
                    elif role == 'Admin':
                        user = Admin()
                        Admin.all_admins.append(user)
                    else:
                        continue

                    
                    user.set_name(row['Name'])
                    user.set_user_id(row['UserID'])
                    user.set_email(row['Email'])
                    user.set_password(row['Password'])

                    users.append(user)
        except FileNotFoundError:
            print(f'{filename} not found. Starting with an empty list.')
        
        return users
    
    @staticmethod
    def saveCourseToCsv(filename ,course_list):
        with open(filename ,mode='w',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['CourseName', 'CourseCode', 'CourseInstructor', 'EnrolledStudents', 'CourseSection', 'CourseDays'])
        
            for course in course_list:
                enrolled_students_str = ','.join(course.enrolledStudent)
                course_days_str = ','.join(course.courseDays)

                writer.writerow([
                        course.courseName,
                        course.courseCode,
                        course.courseInstructor,
                        enrolled_students_str,
                        course.courseSection,
                        course_days_str
                    ])
    
    @staticmethod
    def loadCourseFromCsv(filename):
        courses = []
        try:
            with open(filename, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    course = Course()
                    course.courseName = row['CourseName']
                    course.courseCode = row['CourseCode']
                    course.courseInstructor = row['CourseInstructor']
                    
                    # Split comma-separated strings back to lists (handle empty string too)
                    enrolled_str = row['EnrolledStudents']
                    course.enrolledStudent = enrolled_str.split(',') if enrolled_str else []
                    
                    course.courseSection = row['CourseSection']
                    
                    days_str = row['CourseDays']
                    course.courseDays = days_str.split(',') if days_str else []
                    
                    courses.append(course)
        except FileNotFoundError:
            print(f'{filename} not found. Starting with an empty course list.')
        return courses
    
    @staticmethod
    def marks_dict_to_str(marks_dict):
        # Convert dict to "key:value,key:value" string
        return ','.join(f'{k}:{v}' for k, v in marks_dict.items())
    
    @staticmethod
    def marks_str_to_dict(marks_str):
        # Convert string back to dict
        marks = {}
        if marks_str:
            items = marks_str.split(',')
            for item in items:
                if ':' in item:
                    k, v = item.split(':', 1)
                    marks[k] = v
        return marks

    @staticmethod
    def saveGradeToCsv(filename, grade_list):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['StudentID', 'CourseCode', 'Marks', 'Grade'])
            for grade in grade_list:
                marks_str = FileManager.marks_dict_to_str(grade.marks)
                writer.writerow([grade.student, grade.course, marks_str, grade.grade])

    @staticmethod
    def loadGradeFromCsv(filename):
        grades = []
        try:
            with open(filename, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    grade = Grade()
                    grade.student = row['StudentID']
                    grade.course = row['CourseCode']
                    grade.marks = FileManager.marks_str_to_dict(row['Marks'])
                    grade.grade = row['Grade']
                    grades.append(grade)
        except FileNotFoundError:
            print(f'{filename} not found. Starting with empty grade list.')
        return grades
    
    @staticmethod
    def saveAttendenceToCsv(filename, attendance_list):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['StudentID', 'Date', 'Status', 'CourseName'])
            for attendance in attendance_list:
                writer.writerow([attendance.student_id, attendance.date, attendance.status, attendance.course_name])
    
    @staticmethod
    def loadAttendenceFromCsv(filename):
        attendance_list = []
        try:
            with open(filename, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    attendance = AttendanceSystem()
                    attendance.student_id = row['StudentID']
                    attendance.date = row['Date']
                    attendance.status = row['Status']
                    attendance.course_name = row['CourseName']
                    attendance_list.append(attendance)
        except FileNotFoundError:
            print(f'{filename} not found. Starting with empty attendance list.')
        return attendance_list
    
    @staticmethod
    def saveTimetableToCsv(filename, timetable_list):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                'ClassID', 'ClassName', 
                'TeacherID', 'TeacherName', 
                'SubjectID', 'SubjectName', 
                'DayOfWeek', 'TimeSlot'
            ])
            for record in timetable_list:
                writer.writerow([
                    record.class_id,
                    record.class_name,
                    record.teacher_id,
                    record.teacher_name,
                    record.subject_id,
                    record.subject_name,
                    record.day_of_week,
                    record.time_slot
                ])

    @staticmethod
    def loadTimeTableFromCsv(filename):
        timetable_list = []
        try:
            with open(filename, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    timetable = TimeTable()
                    timetable.class_id = row['ClassID']
                    timetable.class_name = row['ClassName']
                    timetable.teacher_id = row['TeacherID']
                    timetable.teacher_name = row['TeacherName']
                    timetable.subject_id = row['SubjectID']
                    timetable.subject_name = row['SubjectName']
                    timetable.day_of_week = row['DayOfWeek']
                    timetable.time_slot = row['TimeSlot']
                    timetable_list.append(timetable)
        except FileNotFoundError:
            print(f'{filename} not found. Starting with empty timetable list.')
        return timetable_list