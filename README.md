#School Management System - Comprehensive Documentation
Overview
The School Management System is a comprehensive web application designed to streamline administrative tasks in educational institutions. This full-stack solution features a Flask backend with RESTful APIs and a modern frontend interface, providing seamless management of users, courses, attendance, grades, and timetables.

Key Features
User Management: Create/update/delete students, teachers, and admins

Course Management: Manage courses, sections, instructors, and enrollments

Attendance Tracking: Record and manage student attendance

Grade Management: Track and update student grades

Timetable Scheduling: Create and manage class schedules

Data Persistence: CSV-based storage for all system data

Responsive UI: Clean, modern interface with intuitive navigation

System Architecture
text
Frontend (HTML/CSS/JS) 
       ↓
Backend API (Flask/Python)
       ↓
Data Storage (CSV Files)
Installation Guide
Prerequisites
Python 3.8+

Flask

Flask-CORS

Setup Instructions
Clone the repository:

bash
git clone https://github.com/your-repo/school-management-system.git
cd school-management-system
Install dependencies:

bash
pip install flask flask-cors
Create required data directories:

bash
mkdir data
touch data/users.csv data/courses.csv data/attendence.csv data/grades.csv data/timetable.csv
Start the backend server:

bash
python backendAPI.py
Open main.html in your browser to access the frontend interface

File Structure
text
├── backendAPI.py             # Main Flask application
├── main.html                 # Frontend interface
├── data/                     # Data storage directory
│   ├── users.csv
│   ├── courses.csv
│   ├── attendence.csv
│   ├── grades.csv
│   └── timetable.csv
├── modules/                  # Core system modules
│   ├── User_Management_System.py
│   ├── Course_Management_System.py
│   ├── Attendence_Management_System.py
│   ├── Grade_Management_System.py
│   ├── TimeTable_Management_System.py
│   └── Loading_data_pandas.py
API Endpoints
User Management
GET /api/users - List all users

POST /api/users - Create new user

PUT /api/users/<user_id> - Update user

DELETE /api/users/<user_id> - Delete user

Course Management
GET /api/courses - List all courses

POST /api/courses - Create new course

PUT /api/courses/<course_code> - Update course

DELETE /api/courses/<course_code> - Delete course

Attendance Management
GET /api/attendance - List attendance records

POST /api/attendance - Create attendance record

PUT /api/attendance - Update attendance record

DELETE /api/attendance - Delete attendance record

Grade Management
GET /api/grades - List all grades

POST /api/grades - Create/update grade

DELETE /api/grades - Delete grade

Timetable Management
GET /api/timetable - List timetable entries

POST /api/timetable - Create timetable entry

PUT /api/timetable/<class_id> - Update timetable entry

DELETE /api/timetable/<class_id> - Delete timetable entry

Usage Guide
User Management
Navigate to the Users section

Fill the form to add new users (students or teachers)

Use the delete button to remove users

All changes are saved automatically

Course Management
Go to the Courses section

Add new courses with details (name, code, section, instructor)

Manage existing courses using the action buttons

Courses automatically track enrolled students

Attendance Tracking
Access the Attendance section

Mark attendance with student ID, date, course, and status

View and manage existing attendance records

Update status or delete incorrect records

Grade Management
Navigate to the Grades section

Add or update grades using student ID and course code

View all student grades in a tabular format

Delete grades when needed

Timetable Management
Go to the Timetable section

Add new schedule entries with class, teacher, subject, day and time

View the complete timetable

Update or delete existing entries

Data Model
User
python
class User:
    name: str
    user_id: str
    email: str
    password: str
    role: str  # Student/Teacher/Admin
Course
python
class Course:
    courseName: str
    courseCode: str
    courseInstructor: str
    enrolledStudent: list
    courseSection: str
    courseDays: list
Attendance
python
class AttendanceSystem:
    student_id: str
    date: str  # YYYY-MM-DD
    status: str  # Present/Absent
    course_name: str
Grade
python
class Grade:
    student: str  # Student ID
    course: str   # Course code
    grade: str    # Letter grade
Timetable
python
class TimeTable:
    class_id: str
    class_name: str
    teacher_id: str
    teacher_name: str
    subject_id: str
    subject_name: str
    day_of_week: str
    time_slot: str
