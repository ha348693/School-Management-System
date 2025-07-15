# 🎓 School Management System – Comprehensive Documentation

## 📌 Overview  
The **School Management System** is a full-stack web application built to streamline administrative operations in educational institutions. Featuring a **Flask** backend with **RESTful APIs** and a **modern frontend**, it provides seamless management of users, courses, attendance, grades, and timetables.

---

## ✨ Key Features

- **👤 User Management:** Create, update, and delete student, teacher, and admin profiles  
- **📚 Course Management:** Manage courses, sections, instructors, and enrollments  
- **🗓️ Attendance Tracking:** Record and update daily student attendance  
- **📊 Grade Management:** Track and update student grades  
- **📆 Timetable Scheduling:** Create and manage weekly class schedules  
- **💾 Data Persistence:** All data stored in **CSV files** for easy access and portability  
- **🖥️ Responsive UI:** Clean, intuitive, and user-friendly frontend  

---

## 🏗️ System Architecture
Frontend (HTML/CSS/JavaScript)
↓
Flask Backend (Python REST API)
↓
CSV File-Based Storage


---

## ⚙️ Installation Guide

### ✅ Prerequisites
- Python 3.8 or above  
- `Flask`  
- `Flask-CORS`

### 🧰 Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-repo/school-management-system.git
   cd school-management-system
**Install Required Libraries**
pip install flask flask-cors
**Create Required Data Files**
mkdir data
touch data/users.csv data/courses.csv data/attendence.csv data/grades.csv data/timetable.csv
**Start the Backend Server**
python backendAPI.py
**Access the Frontend**
Open main.html in any web browser

## 📁 File Structure

```text
school-management-system/
├── backendAPI.py                   # Main Flask application
├── main.html                       # Frontend interface
├── data/                           # CSV-based data storage
│   ├── users.csv
│   ├── courses.csv
│   ├── attendence.csv
│   ├── grades.csv
│   └── timetable.csv
├── modules/                        # Core backend modules
│   ├── User_Management_System.py
│   ├── Course_Management_System.py
│   ├── Attendence_Management_System.py
│   ├── Grade_Management_System.py
│   ├── TimeTable_Management_System.py
│   └── Loading_data_pandas.py


**🌐 API Endpoints**

**👥 User Management**
Method	Endpoint	Description
GET	/api/users	List all users
POST	/api/users	Create new user
PUT	/api/users/<user_id>	Update user
DELETE	/api/users/<user_id>	Delete user

**📘 Course Management**
Method	Endpoint	Description
GET	/api/courses	List all courses
POST	/api/courses	Create new course
PUT	/api/courses/<code>	Update course
DELETE	/api/courses/<code>	Delete course

**📝 Attendance Management**
Method	Endpoint	Description
GET	/api/attendance	List attendance records
POST	/api/attendance	Create attendance record
PUT	/api/attendance	Update attendance record
DELETE	/api/attendance	Delete attendance record

**📈 Grade Management**
Method	Endpoint	Description
GET	/api/grades	List all grades
POST	/api/grades	Create/Update grade
DELETE	/api/grades	Delete grade

**🕒 Timetable Management**
Method	Endpoint	Description
GET	/api/timetable	List all timetable entries
POST	/api/timetable	Create timetable entry
PUT	/api/timetable/<class_id>	Update timetable entry
DELETE	/api/timetable/<class_id>	Delete timetable entry

**🧭 Usage Guide**

**👤 User Management**
Navigate to the Users section

Fill the form to add a new user

Use the action buttons to delete or edit users

Changes are automatically saved

**📚 Course Management**
Go to the Courses section

Add new courses with name, code, section, and instructor

Modify or delete existing courses

Tracks enrolled students automatically

**🗓️ Attendance Tracking**
Access the Attendance section

Mark attendance with Student ID, Course, Date, and Status

View, update, or delete existing attendance records

**📊 Grade Management**
Navigate to the Grades section

Add or edit grades using Student ID and Course Code

View all grades in a tabular layout

Delete incorrect entries if necessary

**🕒 Timetable Management**
Go to the Timetable section

Add new entries with Class, Teacher, Subject, Day, Time

View, update, or remove schedule entries

**🧬 Data Models**
**👤 User**
class User:
    name: str
    user_id: str
    email: str
    password: str
    role: str  # "Student" | "Teacher" | "Admin"

**📚 Course**
class Course:
    courseName: str
    courseCode: str
    courseInstructor: str
    enrolledStudent: list
    courseSection: str
    courseDays: list
    
**🗓️ AttendanceSystem**
class AttendanceSystem:
    student_id: str
    date: str  # Format: YYYY-MM-DD
    status: str  # "Present" | "Absent"
    course_name: str
    
**📈 Grade**
class Grade:
    student: str  # Student ID
    course: str   # Course code
    grade: str    # e.g., "A", "B+", "C"
    
**🕒 TimeTable**
class TimeTable:
    class_id: str
    class_name: str
    teacher_id: str
    teacher_name: str
    subject_id: str
    subject_name: str
    day_of_week: str
    time_slot: str
    
**📞 Contact**
📧 Email: ha348693@gmail.com
🌐 GitHub: your-repo
