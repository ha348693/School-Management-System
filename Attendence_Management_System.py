from User_Management_System import Student
from Course_Management_System import Course

class AttendanceSystem:
    attendence_records = []

    def __init__(self):
        self.student_id = None
        self.date = None
        self.status = None
        self.course_name = None

        AttendanceSystem.attendence_records.append(self)
    
    def set_student_id(self ,student_id):
        self.student_id = student_id
    
    def set_date(self, date):
        self.date = date
    
    def set_status(self ,status):
        self.status = status
    
    def set_course_name(self, course_name):
        self.course_name = course_name
    
    @staticmethod
    def verifying_student(student_id):
        for student in Student.all_students:
            if student.get_user_id() == student_id:
                return True
        return False
    
    @staticmethod
    def verifying_course(course_code):
        for course in Course.courses_list:
            if course.get_course_name() == course_code:
                return True
        return False
    
    @staticmethod
    def validating_status(status):
        valid_statuses = ['Present', 'Absent']
        return status in valid_statuses
    
    @staticmethod
    def validating_date(date):
        try:
            year, month, day = map(int, date.split('-'))
            if 1 <= month <= 12 and 1 <= day <= 31 and year > 0:
                return True
        except ValueError:
            return False
        return False
    
    def mark_attendance(self):
        while True:
            stId = input('Enter Student ID:- ')
            if not self.verifying_student(stId):
                print("Invalid Student ID. Please try again.")
                return
            
            date = input('Enter Date (YYYY-MM-DD):- ')
            if not self.validating_date(date):
                print("Invalid date format. Please enter in YYYY-MM-DD format.")
                return
            
            course = input('Enter Course Name:- ')
            if not self.verifying_course(course):
                print("Invalid Course Name. Please try again.")
                return

            status = input('Enter Status (Present/Absent):- ')
            if not self.validating_status(status):
                print("Invalid status. Please enter 'Present' or 'Absent'.")
                return
            
            if self.verifying_student(stId) and self.validating_date(date) and self.validating_status(status):
                break

        self.set_student_id(stId)
        self.set_date(date)
        self.set_status(status)
        self.set_course_name(course)
    
    def delete_attedance(self):
        if not self.attendence_records:
            print("No attendance records found.")
            return
        
        student_id = input("Enter Student ID to delete attendance record: ")
        date = input("Enter Date (YYYY-MM-DD) of the record to delete: ")
        
        for record in self.attendence_records:
            if record.student_id == student_id and record.date == date:
                self.attendence_records.remove(record)
                print(f"Attendance record for Student ID {student_id} on {date} has been deleted.")
                return
        
        print("No matching attendance record found.")
    
    def update_attendance(self):
        if not self.attendence_records:
            print('No attendance records found.')
            return
        
        student_id = input("Enter Student ID to update attendace record: ")
        date = input("Enter Date (YYYY-MM-DD) of the record to update: ")

        for record in self.attendence_records:
            if record.student_id == student_id and record.date == date:
                new_status = input("Enter new status (Present/Absent): ")
                if self.validating_status(new_status):
                    record.set_status(new_status)
                    print(f"Attendance record for Student ID {student_id} on {date} has been updated to {new_status}.")
                else:
                    print("Invalid status. Please enter 'Present' or 'Absent'.")
                return
    
    @classmethod
    def show_attendance(cls):
        if not cls.attendence_records:
            print("No attendance records found.")
            return
        
        print("Attedance Records:")
        print(f"{'Student ID':<15} {'Date':<15} {'Course Name':<20} {'Status':<10}")
        print("-" * 60)
        for record in AttendanceSystem.attendence_records:
            print(f"{record.student_id:<15} {record.date:<15} {record.course_name:<20} {record.status:<10}")