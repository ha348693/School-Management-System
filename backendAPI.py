from flask import Flask, request, jsonify
from flask_cors import CORS
from User_Management_System import Student, Teacher, Admin, User, UserManager
from Course_Management_System import Course
from Attendence_Management_System import AttendanceSystem
from Grade_Management_System import Grade
from TimeTable_Management_System import TimeTable
from Loading_data_pandas import FileManager

app = Flask(__name__)
CORS(app)
User.all_user_list = FileManager.loadUserDataFromCsv('data/users.csv', [])
Student.all_students = [u for u in User.all_user_list if isinstance(u, Student)]
Teacher.all_teachers = [u for u in User.all_user_list if isinstance(u, Teacher)]
Admin.all_admins = [u for u in User.all_user_list if isinstance(u, Admin)]

AttendanceSystem.attendence_records = FileManager.loadAttendenceFromCsv('data/attendence.csv')
Grade.grades = FileManager.loadGradeFromCsv('data/grades.csv')
TimeTable.timetable_records = FileManager.loadTimeTableFromCsv('data/timetable.csv')

try:
    Course.courses_list = FileManager.loadCourseFromCsv('data/courses.csv')
    print(f"Loaded {len(Course.courses_list)} courses")
except Exception as e:
    print("Failed to load courses:", e)
    Course.courses_list = []

def serialize_user(user):
    return {
        'id': user.get_user_id(),
        'name': user.get_name(),
        'email': user.get_email(),
        'role': user.role
    }

def serialize_course(course):
    instructor = course.get_course_instructor() if hasattr(course, 'get_course_instructor') else None
    instructor_name = instructor.get_name() if hasattr(instructor, 'get_name') else instructor

    return {
        'code': course.get_course_code() if hasattr(course, 'get_course_code') else '',
        'name': course.get_course_name() if hasattr(course, 'get_course_name') else '',
        'section': course.get_course_section() if hasattr(course, 'get_course_section') else '',
        'instructor': instructor_name,
        'days': course.get_course_days() if hasattr(course, 'get_course_days') else [],
        'enrolledStudentIds': [
            s.get_user_id() if hasattr(s, 'get_user_id') else s for s in getattr(course, 'enrolledStudent', [])
        ]
    }

def serialize_attendance(att):
    return {
        'studentId': att.student_id,
        'date': att.date,
        'courseName': att.course_name,
        'status': att.status
    }

def serialize_grade(grade):
    studentId = grade.student.get_user_id() if hasattr(grade.student, 'get_user_id') else grade.student
    studentName = grade.student.get_name() if hasattr(grade.student, 'get_name') else None
    courseCode = grade.course.get_course_code() if hasattr(grade.course, 'get_course_code') else grade.course
    courseName = grade.course.get_course_name() if hasattr(grade.course, 'get_course_name') else None
    return {
        'studentId': studentId,
        'studentName': studentName,
        'courseCode': courseCode,
        'courseName': courseName,
        'grade': grade.grade
    }

def serialize_timetable(t):
    return {
        'classId': getattr(t, 'class_id', ''),
        'className': getattr(t, 'class_name', ''),
        'teacherId': getattr(t, 'teacher_id', ''),
        'teacherName': getattr(t, 'teacher_name', ''),
        'subjectId': getattr(t, 'subject_id', ''),
        'subjectName': getattr(t, 'subject_name', ''),
        'dayOfWeek': getattr(t, 'day_of_week', ''),
        'timeSlot': getattr(t, 'time_slot', '')
    }

###########################################
# USER APIs

@app.route('/api/users', methods=['GET'])
def api_get_users():
    # Return all non-admin users
    users = [serialize_user(u) for u in User.all_user_list if u.role != 'Admin']
    return jsonify(users), 200

@app.route('/api/users', methods=['POST'])
def api_add_user():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Missing JSON data'}), 400

    role = data.get('role')
    if role == 'Student':
        user = Student()
    elif role == 'Teacher':
        user = Teacher()
    else:
        return jsonify({'error': 'Role must be Student or Teacher'}), 400

    user.set_name(data.get('name'))
    user.set_user_id(data.get('id'))
    user.set_email(data.get('email'))
    user.set_password(data.get('password', 'defaultpass'))

    FileManager.saveUserDataToCsv('data/users.csv', User.all_user_list)
    return jsonify(serialize_user(user)), 201


@app.route('/api/users/<user_id>', methods=['PUT'])
def api_update_user(user_id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Missing JSON data'}), 400

    user = next((u for u in User.all_user_list if u.get_user_id() == user_id), None)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    user.set_name(data.get('name', user.get_name()))
    user.set_email(data.get('email', user.get_email()))

    FileManager.saveUserDataToCsv('data/users.csv', User.all_user_list)
    return jsonify(serialize_user(user)), 200

@app.route('/api/users/<user_id>', methods=['DELETE'])
def api_delete_user(user_id):
    user = next((u for u in User.all_user_list if u.get_user_id() == user_id), None)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    User.all_user_list.remove(user)
    if user.role == 'Student' and user in Student.all_students:
        Student.all_students.remove(user)
    elif user.role == 'Teacher' and user in Teacher.all_teachers:
        Teacher.all_teachers.remove(user)

    FileManager.saveUserDataToCsv('data/users.csv', User.all_user_list)
    return jsonify({'message': f'User {user_id} deleted'}), 200

###########################################
# COURSE APIs

@app.route('/api/courses', methods=['GET'])
def api_get_courses():
    try:
        print("GET /api/courses called")
        courses = [serialize_course(c) for c in Course.courses_list]
        print("Courses returned:", len(courses))
        return jsonify(courses), 200
    except Exception as e:
        print("Error in /api/courses:", e)
        return jsonify({'error': 'Internal server error', 'details': str(e)}), 500


@app.route('/api/courses', methods=['POST'])
def api_add_course():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Missing JSON data'}), 400

    course = Course()
    course.set_course_name(data.get('name'))
    course.set_course_code(data.get('code'))
    course.set_course_section(data.get('section'))

    instructor_name = data.get('instructor')
    instructor = next((t for t in Teacher.all_teachers if t.get_name() == instructor_name), None)
    course.courseInstructor = instructor

    course.courseDays = data.get('days', [])
    course.enrolledStudent = []
    for sid in data.get('enrolledStudentIds', []):
        student = next((s for s in Student.all_students if s.get_user_id() == sid), None)
        if student:
            course.enrolledStudent.append(student)

    FileManager.saveCourseToCsv('data/courses.csv', Course.courses_list)
    return jsonify(serialize_course(course)), 201

@app.route('/api/courses/<course_code>', methods=['PUT'])
def api_update_course(course_code):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Missing JSON data'}), 400

    course = next((c for c in Course.courses_list if c.get_course_code() == course_code), None)
    if not course:
        return jsonify({'error': 'Course not found'}), 404

    course.set_course_name(data.get('name', course.get_course_name()))
    course.set_course_section(data.get('section', course.get_course_section()))

    instructor_name = data.get('instructor')
    if instructor_name:
        instructor = next((t for t in Teacher.all_teachers if t.get_name() == instructor_name), None)
        if instructor:
            course.courseInstructor = instructor

    days = data.get('days')
    if isinstance(days, list):
        course.courseDays = days

    enrolled_ids = data.get('enrolledStudentIds')
    if isinstance(enrolled_ids, list):
        course.enrolledStudent = []
        for sid in enrolled_ids:
            student = next((s for s in Student.all_students if s.get_user_id() == sid), None)
            if student:
                course.enrolledStudent.append(student)

    FileManager.saveCourseToCsv('data/courses.csv', Course.courses_list)
    return jsonify(serialize_course(course)), 200

@app.route('/api/courses/<course_code>', methods=['DELETE'])
def api_delete_course(course_code):
    course = next((c for c in Course.courses_list if c.get_course_code() == course_code), None)
    if not course:
        return jsonify({'error': 'Course not found'}), 404

    Course.courses_list.remove(course)
    FileManager.saveCourseToCsv('data/courses.csv', Course.courses_list)
    return jsonify({'message': f'Course {course_code} deleted'}), 200

###########################################
# ATTENDANCE APIs

@app.route('/api/attendance', methods=['GET'])
def api_get_attendance():
    try:
        records = [serialize_attendance(a) for a in AttendanceSystem.attendence_records]
        return jsonify(records), 200
    except Exception as e:
        return jsonify({'error': 'Failed to serialize attendance records', 'details': str(e)}), 500

@app.route('/api/attendance', methods=['POST'])
def api_add_attendance():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Missing JSON data'}), 400

    st_id = data.get('studentId')
    date = data.get('date')
    course_name = data.get('courseName')
    status = data.get('status')

    if not AttendanceSystem.verifying_student(st_id):
        return jsonify({'error': 'Invalid student ID'}), 400
    if not AttendanceSystem.verifying_course(course_name):
        return jsonify({'error': 'Invalid course name'}), 400
    if not AttendanceSystem.validating_status(status):
        return jsonify({'error': 'Invalid status'}), 400
    if not AttendanceSystem.validating_date(date):
        return jsonify({'error': 'Invalid date format'}), 400

    for rec in AttendanceSystem.attendence_records:
        if rec.student_id == st_id and rec.date == date and rec.course_name == course_name:
            return jsonify({'error': 'Attendance record already exists'}), 400

    attendance = AttendanceSystem()
    attendance.set_student_id(st_id)
    attendance.set_date(date)
    attendance.set_course_name(course_name)
    attendance.set_status(status)

    FileManager.saveAttendenceToCsv('data/attendence.csv', AttendanceSystem.attendence_records)
    return jsonify(serialize_attendance(attendance)), 201

@app.route('/api/attendance', methods=['PUT'])
def api_update_attendance():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Missing JSON data'}), 400

    st_id = data.get('studentId')
    date = data.get('date')
    course_name = data.get('courseName')
    new_status = data.get('status')

    for rec in AttendanceSystem.attendence_records:
        if rec.student_id == st_id and rec.date == date and rec.course_name == course_name:
            if AttendanceSystem.validating_status(new_status):
                rec.set_status(new_status)
                FileManager.saveAttendenceToCsv('data/attendence.csv', AttendanceSystem.attendence_records)
                return jsonify(serialize_attendance(rec)), 200
            else:
                return jsonify({'error': 'Invalid status'}), 400

    return jsonify({'error': 'Attendance record not found'}), 404

@app.route('/api/attendance', methods=['DELETE'])
def api_delete_attendance():
    st_id = request.args.get('studentId')
    date = request.args.get('date')
    course_name = request.args.get('courseName')

    to_remove = None
    for rec in AttendanceSystem.attendence_records:
        if rec.student_id == st_id and rec.date == date and rec.course_name == course_name:
            to_remove = rec
            break

    if to_remove:
        AttendanceSystem.attendence_records.remove(to_remove)
        FileManager.saveAttendenceToCsv('data/attendence.csv', AttendanceSystem.attendence_records)
        return jsonify({'message': 'Attendance record deleted'}), 200
    else:
        return jsonify({'error': 'Attendance record not found'}), 404

###########################################
# GRADE APIs

@app.route('/api/grades', methods=['GET'])
def api_get_grades():
    try:
        grades = [serialize_grade(g) for g in Grade.grades]
        return jsonify(grades), 200
    except Exception as e:
        return jsonify({'error': 'Failed to serialize grades', 'details': str(e)}), 500

@app.route('/api/grades', methods=['POST'])
def api_add_grade():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Missing JSON data'}), 400

    student_id = data.get('studentId')
    course_code = data.get('courseCode')
    grade_value = data.get('grade')

    student = next((s for s in Student.all_students if s.get_user_id() == student_id), None)
    course = next((c for c in Course.courses_list if c.get_course_code() == course_code), None)

    if not student:
        return jsonify({'error': 'Invalid student ID'}), 400
    if not course:
        return jsonify({'error': 'Invalid course code'}), 400
    if not grade_value:
        return jsonify({'error': 'Missing grade value'}), 400

    for existing_grade in Grade.grades:
        if existing_grade.student == student and existing_grade.course == course:
            existing_grade.grade = grade_value
            FileManager.saveGradeToCsv('data/grades.csv', Grade.grades)
            return jsonify(serialize_grade(existing_grade)), 200

    grade = Grade()
    grade.student = student
    grade.course = course
    grade.grade = grade_value
    Grade.grades.append(grade)

    FileManager.saveGradeToCsv('data/grades.csv', Grade.grades)
    return jsonify(serialize_grade(grade)), 201

@app.route('/api/grades', methods=['DELETE'])
def api_delete_grade():
    student_id = request.args.get('studentId')
    course_code = request.args.get('courseCode')

    to_remove = None
    for g in Grade.grades:
        if (hasattr(g.student, 'get_user_id') and g.student.get_user_id() == student_id) and (hasattr(g.course, 'get_course_code') and g.course.get_course_code() == course_code):
            to_remove = g
            break

    if to_remove:
        Grade.grades.remove(to_remove)
        FileManager.saveGradeToCsv('data/grades.csv', Grade.grades)
        return jsonify({'message': 'Grade record deleted'}), 200
    else:
        return jsonify({'error': 'Grade record not found'}), 404

###########################################
# TIMETABLE APIs

@app.route('/api/timetable', methods=['GET'])
def api_get_timetable():
    try:
        records = [serialize_timetable(t) for t in TimeTable.timetable_records]
        return jsonify(records), 200
    except Exception as e:
        return jsonify({'error': 'Failed to serialize timetable records', 'details': str(e)}), 500

@app.route('/api/timetable', methods=['POST'])
def api_add_timetable():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Missing JSON data'}), 400

    t = TimeTable()
    t.set_class_id(data.get('classId'))
    t.set_class_name(data.get('className'))
    t.set_teacher_id(data.get('teacherId'))
    t.set_teacher_name(data.get('teacherName'))
    t.set_subject_id(data.get('subjectId'))
    t.set_subject_name(data.get('subjectName'))
    t.set_day_of_week(data.get('dayOfWeek'))
    t.set_time_slot(data.get('timeSlot'))

    FileManager.saveTimetableToCsv('data/timetable.csv', TimeTable.timetable_records)
    return jsonify(serialize_timetable(t)), 201

@app.route('/api/timetable/<class_id>', methods=['PUT'])
def api_update_timetable(class_id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Missing JSON data'}), 400

    t = next((tt for tt in TimeTable.timetable_records if tt.get_class_id() == class_id), None)
    if not t:
        return jsonify({'error': 'Timetable record not found'}), 404

    t.set_class_name(data.get('className', t.get_class_name()))
    t.set_teacher_id(data.get('teacherId', t.get_teacher_id()))
    t.set_teacher_name(data.get('teacherName', t.get_teacher_name()))
    t.set_subject_id(data.get('subjectId', t.get_subject_id()))
    t.set_subject_name(data.get('subjectName', t.get_subject_name()))
    t.set_day_of_week(data.get('dayOfWeek', t.get_day_of_week()))
    t.set_time_slot(data.get('timeSlot', t.get_time_slot()))

    FileManager.saveTimetableToCsv('data/timetable.csv', TimeTable.timetable_records)
    return jsonify(serialize_timetable(t)), 200

@app.route('/api/timetable/<class_id>', methods=['DELETE'])
def api_delete_timetable(class_id):
    t = next((tt for tt in TimeTable.timetable_records if tt.get_class_id() == class_id), None)
    if not t:
        return jsonify({'error': 'Timetable record not found'}), 404

    TimeTable.timetable_records.remove(t)
    FileManager.saveTimetableToCsv('data/timetable.csv', TimeTable.timetable_records)
    return jsonify({'message': f'Timetable record {class_id} deleted'}), 200


###########################################
if __name__ == '__main__':
    print("Starting Flask backend API server on http://127.0.0.1:5000")
    app.run(debug=True)

