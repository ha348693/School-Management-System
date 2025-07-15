from User_Management_System import Student ,Teacher
class Course:
    courses_list = list()

    def __init__(self):
        self.courseName = None
        self.courseCode = None
        self.courseInstructor = None
        self.enrolledStudent = []
        self.courseSection = None
        self.courseDays = []

        Course.courses_list.append(self)
    
    def set_course_name(self ,name):
        self.courseName = name
    
    def set_course_code(self ,code):
        self.courseCode = code
    
    def set_course_Instructor(self):
        for index ,teacher in enumerate(Teacher.all_teachers):
            print(f'Press {index+1} for {teacher.get_name()} --> Role: {teacher.get_role()}')
        
        while True:
            choice = input('Enter Your Choice:- ')
            if choice.isdigit() and 1 <= int(choice) <= len(Teacher.all_teachers):
                break
            else:
                continue
        
        self.courseInstructor = Teacher.all_teachers[int(choice) - 1]
        
    def enroll_students(self):
        for index ,student in enumerate(Student.all_students):
            print(f'Press {index+1} for {student.get_name()} --> Role: {student.get_role()}')
        
        while True:
            choice = input('Enter Your Choice:- ')
            if choice.isdigit() and 1 <= int(choice) <= len(Student.all_students):
                break
            else:
                continue
        
        self.enrolledStudent.append(Student.all_students[int(choice) - 1])
    
    def set_course_section(self ,section):
        self.courseSection = section
    
    def set_course_days(self):
        days_avaliable = ['monday' ,'tuesday' ,'wednesday' ,'thursday' ,'friday']

        num_of_days = input('How many days will the course class held:- ')

        while (not num_of_days.isdigit()) or (int(num_of_days) < 1) or (int(num_of_days) > len(days_avaliable)):
            print('Invalid Input Try Again!')
            num_of_days = input('How many days will the course class held:- ')
        
        for i in range(int(num_of_days)):
            print(f'Day {i + 1}')
            day = input('Which day this course will held:- ')

            while (not day.isalpha()) or (day not in days_avaliable):
                print('Invalid Input Try Again!')
                day = input('Which day this course will held:- ')
            
            self.courseDays.append(day)
    
    def get_course_name(self):
        return self.courseName
    
    def get_course_code(self):
        return self.courseCode
    
    def get_course_instructor(self):
        return self.courseInstructor
    
    def get_enrolled_students(self):
        for student in self.enrolledStudent:
            print(student.get_user_id())
    
    def get_course_section(self):
        return self.courseSection
    
    def get_course_days(self):
        return self.courseDays
    

    def add_course(self):
        course_name = input('Enter Course Name:- ')
        course_code = input('Enter Course Code:- ')
        section = input('Enter Course Section:- ')

        self.set_course_name(course_name)
        self.set_course_code(course_code)
        self.set_course_section(section)
        self.set_course_Instructor()
        self.set_course_days()
    
    def delete_course(self):
        course_code = input('Enter Course\'s Code you want to delete:- ')

        for course in self.courses_list:
            if course_code == course.get_course_code():
                print('Course found!! Now Deleting')
                self.courses_list.remove(course)
                print('Deletion Successfull!')
                return 
        else:
            print('Course Not Found Deletion Unsuccessfull!!')
    
    def update_course(self):
        code = input('Enter Course Code of the Course you want to update:- ')

        for course in self.courses_list:
            if code == course.get_course_code():
                print('Press 1. For Update Course Name.')
                print('Press 2. For Update Course Code.')
                print('Press 3. For Update Course Section.')
                print('Press 4. For Update Course Instructor.')
                print('Press 5. For Update Enrolled Students.')
                print('Press 6. For Update Course Days')

                while True:
                    choice = input('Enter Your Choice:- ')

                    if (choice.isdigit()) and (1 <= int(choice) <= 6):
                        break
                    else:
                        print('Invalid Input!! Try Again.')
                
                choice = int(choice)

                if choice == 1:
                    print('======> Updating Course Name <======')
                    name = input('Enter new course name:- ')
                    course.set_course_name(name)
                
                elif choice == 2:
                    print('======> Updating Course Code <======')
                    code = input('Enter new course code:- ')
                    course.set_course_code(code)
                
                elif choice == 3:
                    print('======> Updating Course Section <======')
                    section = input('Enter course new section name:- ')
                    course.set_course_section(section)

                elif choice == 4:
                    print('======> Updating Course Instructor <======')
                    course.set_course_Instructor()

                elif choice == 5:
                    print('Do you want to: ')
                    print('1. Remove Student.')
                    print('2. Replace Existing Student with New One.')

                    while True:
                        sub_choice = input('Enter Your Choice:- ')

                        if (sub_choice.isdigit()) and (1 <= int(sub_choice) <= 2):
                            break
                        else:
                            print('Invalid Input!! Try Again.')
                    
                    sub_choice = int(sub_choice)

                    if sub_choice == 1:
                        removed = False

                        print('You want to remove student from enrollment:')
                        user_id = input('Enter User Id of Student:- ')

                        for student in self.enrolledStudent:
                            if user_id == student.get_user_id():
                                print(f'Removing Student Named: {student.get_name()}')
                                self.enrolledStudent.remove(student)
                                print(f'======> Removing Student Name: {student.get_name()} successfull <======')
                                removed = True

                        if not removed:
                            print('======> Student not found in database Removal Unsuccessfull <======')

                    elif sub_choice == 2:
                        Found = False

                        print('You want to replace a student:')
                        user_id = input('Enter User Id of Student:- ')

                        for student in self.enrolledStudent:
                            if user_id == student.get_user_id():
                                Found = True
                                break
                        
                        if Found:
                            replace = False

                            for index ,student in enumerate(Student.all_students):
                                print(f'Press {index + 1} for {student.get_user_id()}')
                            
                            while True:
                                sub_choice = input(f'Which Student you want to replace with {user_id}')

                                if (sub_choice.isdigit()) and (1 <= int(sub_choice) <= len(Student.all_students)):
                                    break
                                else:
                                    print('Invalid Input!! Try Again.')
                            
                            for student in self.enrolledStudent:
                                if user_id == student.get_user_id():
                                    self.enrolledStudent.remove(student)
                                    self.enrolledStudent.append(Student.all_students[int(sub_choice) - 1])
                                    print('======> Replacment Successfull <======')
                                    replace = True
                            
                            if not replace:
                                print('======< Replacement Unsuccessfull >======')

                elif choice == 6:
                    print('Do you want to change a specific day or whole schedule')
                    print('1 for specific day!')
                    print('2 for update whole schedule!')

                    while True:
                        choice = input('Enter your choice:- ')
                        
                        if (choice.isdigit()) and (1 <= int(choice) <= 2):
                            break
                        else:
                            print('Invalid Input! Try Again.')
                    
                    choice = int(choice)
                    
                    if choice == 1:
                        print('======> Updating Specific Day <======')
                        for index ,day in enumerate(self.courseDays):
                            print(f'Press {index + 1} to Update {day} slot')
                        
                        while True:
                            sub_choice = input('Enter your choice:- ')
                            
                            if (sub_choice.isdigit()) and (1 <= int(sub_choice) <= len(self.courseDays)):
                                break
                            else:
                                print('Invalid Input! Try Again.')
                        
                        sub_choice = int(sub_choice)
                        self.courseDays[sub_choice - 1] = input('Entered New day the class would held')


                    elif choice == 2:
                        print('======> Updating Whole Schedule <======')
                        previous_days = self.get_course_days()
                        self.courseDays = [item for item in self.courseDays if item not in previous_days]
                        self.set_course_days()
    
    def show_course_info(self):
        print('Do you want to see:')
        print('1. Specific Course Info.')
        print('2. Just All Course Names and Course Code Avaliable.')
        print('3. Show all Course Info At Once.')

        while True:
            choice = input('Enter Your Choice(Enter 1-3):- ')

            if choice.isdigit() and 1 <= int(choice) <= 3:
                break
            else:
                print('Invalid Input Try Again!!')
        
        choice = int(choice)

        if choice == 1:
            code = input('Enter Course Code of the course you want the information:- ')
            found = False

            for course in self.courses_list:
                if code == course.get_course_code():
                    print(f'Course Name:- {course.get_course_name()}')
                    print(f'Course Code:- {course.get_course_code()}')
                    print(f'Course Section:- {course.get_course_section()}')
                    print(f'Course Instructor:- {course.get_course_instructor()}')
                    print(f'Enrolled Students:-')
                    course.get_enrolled_students()
                    found = True
                    return
            
            if not found:
                print('Course Not Found!!')
        
        elif choice == 2:
            print('Course Name ----> Course Code')
            for course in self.courses_list:
                print(f'{course.get_course_name()} ----> {course.get_course_code()}')
        
        elif choice == 3:
            print('======> Showing All Courses Info At Once <======')
            for course in self.courses_list:
                print(f'Course Name:- {course.get_course_name()}')
                print(f'Course Code:- {course.get_course_code()}')
                print(f'Course Section:- {course.get_course_section()}')
                print(f'Course Instructor:- {course.get_course_instructor()}')
                print(f'Enrolled Students:-')
                course.get_enrolled_students()