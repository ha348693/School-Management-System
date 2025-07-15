from User_Management_System import Teacher
from Course_Management_System import Course

class TimeTable:
    timetable_records = []
    def __init__(self):
        self.class_id = None
        self.class_name = None
        self.teacher_id = None
        self.teacher_name = None
        self.subject_id = None
        self.subject_name = None
        self.day_of_week = None
        self.time_slot = None

        TimeTable.timetable_records.append(self)
    
    def get_class_id(self):
        return self.class_id

    def set_class_id(self, class_id):
        self.class_id = class_id

    def get_class_name(self):
        return self.class_name

    def set_class_name(self, class_name):
        self.class_name = class_name

    def get_teacher_id(self):
        return self.teacher_id

    def set_teacher_id(self, teacher_id):
            self.teacher_id = teacher_id

    def get_teacher_name(self):
        return self.teacher_name

    def set_teacher_name(self, teacher_name):
        self.teacher_name = teacher_name

    def get_subject_id(self):
        return self.subject_id

    def set_subject_id(self, subject_id):
        self.subject_id = subject_id

    def get_subject_name(self):
        return self.subject_name

    def set_subject_name(self, subject_name):
        self.subject_name = subject_name

    def get_day_of_week(self):
        return self.day_of_week

    def set_day_of_week(self, day_of_week):
        self.day_of_week = day_of_week

    def get_time_slot(self):
        return self.time_slot

    def set_time_slot(self, time_slot):
        self.time_slot = time_slot
    
    def verifying_teacher(self ,teacher_id):
        for teacher in Teacher.all_teachers:
            if teacher.get_user_id() == teacher_id:
                return True
        return False
    
    def verifying_teacher_name(self, teacher_name):
        for teacher in Teacher.all_teachers:
            if teacher.get_name() == teacher_name:
                return True
        return False
    
    def checking_for_teacher_clash(self, teacher_id, day_of_week):
        for record in TimeTable.timetable_records:
            if record.get_teacher_id() == teacher_id and record.get_day_of_week() == day_of_week:
                return True
        return False
    
    def verifying_subject(self, subject_id ,subject_name):
        for course in Course.courses_list:
            if course.get_course_code() == subject_id and course.get_course_name() == subject_name:
                return True
        
        return False
    
    def veriftying_day_of_week(self, day_of_week):
        valid_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

        return day_of_week in valid_days
    
    def checking_for_class_clash(self, class_id, day_of_week):
        for record in TimeTable.timetable_records:
            if record.get_class_id() == class_id and record.get_day_of_week() == day_of_week:
                return True
        return False
    
    def checking_for_timeslot_clash(self, time_slot , class_id, day_of_week):
        for record in TimeTable.timetable_records:
            if record.get_class_id() == class_id and record.get_day_of_week() == day_of_week and record.get_time_slot() == time_slot:
                return True
        return False
    
    def add_timetable(self):
        while True:
            class_name = input('Enter Class Name: ')
            if not class_name:
                print('Class name cannot be empty. Please try again.')
                continue
            self.set_class_name(class_name)

            class_id = input('Enter Class ID: ')
            if not class_id:
                print('Class ID cannot be empty. Please try again.')
                continue
            self.set_class_id(class_id)

            day_of_week = input('Enter Day of Week: ')
            if not day_of_week:
                print('Day of week cannot be empty. Please try again.')
                continue

            if self.veriftying_day_of_week(day_of_week):
                if self.checking_for_class_clash(class_id, day_of_week):
                    print("This class is already scheduled on this day. Please choose another day or class.")
                    continue
                else:
                    self.set_day_of_week(day_of_week) 
            else:
                print("Invalid day of week. Please enter a valid day (e.g., Monday, Tuesday, etc.).")
                continue

            teacher_id = input('Enter Teacher ID: ')
            if not self.verifying_teacher(teacher_id):
                print("Invalid Teacher ID. Please try again.")
                continue
            if self.checking_for_teacher_clash(teacher_id, self.get_day_of_week()):
                print("This teacher is already assigned to a class on this day. Please choose another day or teacher.")
                continue
            self.set_teacher_id(teacher_id)

            teacher_name = input('Enter Teacher Name: ')
            if not teacher_name:
                print('Teacher name cannot be empty. Please try again.')
                continue
            self.set_teacher_name(teacher_name)

            subject_id = input('Enter Subject ID: ')
            if not subject_id:
                print('Subject ID cannot be empty. Please try again.')
                continue
            subject_name = input('Enter Subject Name: ')
            if not subject_name:
                print('Subject name cannot be empty. Please try again.')
                continue 

            if not self.verifying_subject(subject_id, subject_name):
                print("Invalid Subject ID or Name. Please try again.")
                continue

            self.set_subject_id(subject_id)
            self.set_subject_name(subject_name)

            time_slot = input('Enter Time Slot: ')
            if not time_slot:
                print('Time slot cannot be empty. Please try again.')
                continue

            if self.checking_for_timeslot_clash(time_slot ,self.get_class_id(), self.get_day_of_week()):
                print("This time slot is already booked. Please choose another time slot.")
                continue

            self.set_time_slot(time_slot)    
            print("\n[✓] Timetable Entry Added Successfully:") 
    
    @classmethod
    def show_timetable(cls):
        for timetable in cls.timetable_records:
            print(f"Class: {timetable.get_class_name()} | Teacher: {timetable.get_teacher_name()} | Subject: {timetable.get_subject_name()} | Day: {timetable.get_day_of_week()} | Time: {timetable.get_time_slot()}")
    @classmethod
    def remove_timetable(cls):
        while True:
            class_id = input("Enter Class ID to remove timetable entry: ").strip()
            if not class_id:
                print("Class ID cannot be empty.")
                continue
            break

        for timetable in cls.timetable_records:
            if timetable.get_class_id() == class_id:
                cls.timetable_records.remove(timetable)
                print(f"Timetable entry for Class ID {class_id} has been removed.")
                return
        print(f"No timetable entry found for Class ID {class_id}.")
    
    @classmethod
    def Update_timetable(cls):
        found = False
        while True:
            class_id = input("Enter Class ID to update timetable entry: ").strip()
            if not class_id:
                print("Class ID cannot be empty.")
                continue
            break

        for timetable in cls.timetable_records:
            if timetable.get_class_id() == class_id:
                found = True
                print(f"Updating timetable for Class ID {class_id}.")
                print('1. Update Class Name')
                print('2. Update Teacher ID')
                print('3. Update Teacher Name')
                print('4. Update Subject ID ,Name')
                print('5. Update Day of Week')
                print('6. Update Time Slot')

                while True:
                    choice = input('Enter Your Choice (1-7): ').strip()
                    if choice.isdigit() and 1 <= int(choice) <= 6:
                        choice = int(choice)
                        break
                    else:
                        print('Invalid Input! Please enter a number between 1 and 7.')
                        continue
                
                choice = int(choice)

                if choice == 1:
                    new_class_name = input("Enter new Class Name: ").strip()
                    if not new_class_name:
                        print("Class Name cannot be empty.")
                        continue
                    timetable.set_class_name(new_class_name)
                elif choice == 2:
                    new_teacher_id = input("Enter new Teacher ID: ").strip()
                    if not timetable.verifying_teacher(new_teacher_id):
                        print("Invalid Teacher ID. Please try again.")
                        continue
                    if timetable.checking_for_teacher_clash(new_teacher_id, timetable.get_day_of_week()):
                        print("This teacher is already assigned to a class on this day. Please choose another day or teacher.")
                        continue
                    timetable.set_teacher_id(new_teacher_id)
                elif choice == 3:
                    new_teacher_name = input("Enter new Teacher Name: ").strip()
                    if not new_teacher_name:
                        print("Teacher Name cannot be empty.")
                        continue
                    if timetable.verifying_teacher_name(new_teacher_name):
                        timetable.set_teacher_name(new_teacher_name)
                    else:
                        print("Invalid Teacher Name. Please try again.")
                        continue
                elif choice == 4:
                    while True:
                        new_subject_id = input("Enter new Subject ID: ").strip()
                        if not new_subject_id:
                            print("Subject ID cannot be empty.")
                            continue
                        new_subject_name = input("Enter new Subject Name: ").strip()
                        if not new_subject_name:
                            print("Subject Name cannot be empty.")
                            continue
                        break

                    if not timetable.verifying_subject(new_subject_id, new_subject_name):
                        print("Invalid Subject ID or Name. Please try again.")
                        continue
                    timetable.set_subject_id(new_subject_id)
                    timetable.set_subject_name(new_subject_name)
                
                elif choice == 5:
                    while True:
                        new_day_of_week = input("Enter new Day of Week: ").strip()
                        if not timetable.veriftying_day_of_week(new_day_of_week):
                            print("Invalid day of week. Please enter a valid day (e.g., Monday, Tuesday, etc.).")
                            continue
                        if timetable.checking_for_class_clash(timetable.get_class_id(), new_day_of_week):
                            print("This class is already scheduled on this day. Please choose another day or class.")
                            continue
                        break
                    timetable.set_day_of_week(new_day_of_week)
                
                elif choice == 6:
                    while True:
                        new_time_slot = input("Enter new Time Slot: ").strip()
                        if not new_time_slot:
                            print("Time slot cannot be empty.")
                            continue
                        if timetable.checking_for_timeslot_clash(new_time_slot , timetable.get_class_id(), timetable.get_day_of_week()):
                            print("This time slot is already booked. Please choose another time slot.")
                            continue
                        break
                    timetable.set_time_slot(new_time_slot)
        
        if not found:
            print(f"No timetable entry found for Class ID {class_id}.")