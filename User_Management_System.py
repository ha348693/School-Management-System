class User:
    all_user_list = list()

    def __init__(self):
        self.name = None
        self.user_id = None
        self.email = None
        self.password = None
        self.role = None

        
        User.all_user_list.append(self)
    
    def set_name(self ,name):
        self.name = name
    
    def set_user_id(self ,userId):
        self.user_id = userId
    
    def set_email(self ,email):
        self.email = email
    
    def set_password(self ,password):
        self.password = password

    def get_name(self):
        return self.name
    
    def get_user_id(self):
        return self.user_id
    
    def get_email(self):
        return self.email
    
    def get_password(self):
        return self.password

class Student(User):
    all_students = []

    def __init__(self):
        super().__init__()
        self.role = 'Student'

        Student.all_students.append(self)

class Teacher(User):
    all_teachers = []

    def __init__(self):
        super().__init__()
        self.role = 'Teacher'

        Teacher.all_teachers.append(self)

class Admin(User):
    all_admins = []

    def __init__(self):
        super().__init__()
        self.role = 'Admin'

        Admin.all_admins.append(self)

class UserManager:
    def __init__(self):
        pass
    
    @staticmethod
    def show_all_users():
        for user in User.all_user_list:
            print(user.get_user_id())
    
    def create_initial_admin(self):
        if not User.all_user_list:
            print('User Database is Empty! Creating Admin Account')
            self.create_admin_account()

    def create_admin_account(self):
        admin = Admin()
        Name = input('Enter Admin Full Name:- ')
        UserId = input('Enter Admin UserId:- ')
        Email = input('Enter Admin Email:- ')
        Password = input('Enter Admin Password:- ')
        admin.set_name(Name)
        admin.set_user_id(UserId)
        admin.set_email(Email)
        admin.set_password(Password)
        
    @staticmethod
    def show_students():
        for student in Student.all_students:
            print(student.get_user_id())
    
    @staticmethod
    def show_teachers():
        for teacher in Teacher.all_teachers:
            print(teacher.get_user_id())
    
    @staticmethod
    def checking_ceredentials(userid ,password):
        for user in User.all_user_list:
            if (user.get_user_id() == userid) and (user.get_password() == password) and (user.role == 'Admin'):
                return True
        return False
    
    def user_database_empty(self):
        admin = Admin()

        Name = input('Enter Admin Full Name:- ')
        UserId = input('Enter Admin UserId:- ')
        Email = input('Enter Admin Email:- ')
        Password = input('Enter Admin Password:- ')

        admin.set_name(Name)
        admin.set_user_id(UserId)
        admin.set_email(Email)
        admin.set_password(Password)
    
    def login(self):
        tries = 3
        print("\n========== LOGIN Menu ==========")
        while tries >= 1:
            userid = input('Enter Admin User ID:- ')
            password = input('Enter Admin User Password:- ')

            if self.checking_ceredentials(userid ,password):
                print(f'Access Granted Welcome {userid}')
                return True
            else:
                print(f'Invalid UserID or Password Try Again')
                tries -= 1
                print(f'You Got {tries} tries left')
        
        print('You Exhausted Your 3 tries please try later!!')
        return False
    
    def determining_roles(self):
        role_avaliable = ['Teacher' ,'Student']

        print('Roles Avalible: ')
        for index,role in enumerate(role_avaliable):
            print(f'Press {index + 1} For {role}')
        
        while True:
            choice = input('Enter Your Choice:- ')

            if (choice.isdigit()) and (1 <= int(choice) <= len(role_avaliable)):
                print(f'So You Choose {role_avaliable[int(choice) - 1]} role')
                print('Are You Sure Press \'y\' for yes and \'n\' for no.')
                while True:
                    sub_choice = input().lower()
                    if sub_choice == 'y':
                        return role_avaliable[int(choice) - 1]
                    elif sub_choice == 'n':
                        print('You want another role!')
                        break
                    else:
                        print('Invalid Sub Choice Input!!')
            else:
                print('Invalid Choice Input!!!')
    
    @staticmethod
    def check_if_user_present(user_id):
        for user in User.all_user_list:
            if user_id == user.get_user_id() and user.role != Admin:
                return True
        
        return False
    
    def update_user(self):
        tries = 3
        while tries >= 1:
            user_id = input('Enter User ID of user you want to delete:- ')

            if self.check_if_user_present(user_id):
                for user in User.all_user_list:
                    if user_id == user.get_user_id():
                        print('User Found!!')
                        print('What You want to Update!!')
                        print('1. Update Name')
                        print('2. Update User Id')
                        print('3. Update Email')
                        print('4. Update Password')
                        print('5. Update Role')

                        while True:
                            choice = input('Enter Your Choice:- ')

                            if choice.isdigit() and 1 <= int(choice) <= 5:
                                break

                            else:
                                print('Invalid Input !!')
                        
                        choice = int(choice)
                        if choice == 1:
                            print(f'You are Updating User Name of {user.get_user_id()}') 
                            name = input('Enter Updated Name:- ')
                            user.set_name(name)
                            return
                        elif choice == 2:
                            print(f'You are Updating User UserId of {user.get_user_id()}') 
                            user_id = input('Enter Updated UserID:- ')
                            user.set_user_id(user_id)
                            return
                        elif choice == 3:
                            print(f'You are Updating User Email of {user.get_user_id()}') 
                            Email = input('Enter Updated Email:- ')
                            user.set_email(Email)
                            return
                        elif choice == 4:
                            print(f'You are Updating User Password of {user.get_user_id()}') 
                            password = input('Enter Updated Password:- ')
                            user.set_email(password)
                            return
                        elif choice == 5:
                            print(f'You are Updating User Role of {user.get_user_id()}') 
                            Role = self.determining_roles()
                            user.role = Role

                            if Role == 'Teacher':
                                Student.all_students.remove(user)
                                Teacher.all_teachers.append(user)
                            
                            elif Role == 'Student':
                                Teacher.all_teachers.remove(user)
                                Student.all_students.append(user)
                            
                            return
            else:
                print('User Not Found')
                tries -= 1
                print(f'Try Again (You got {tries} left)')

    def delete_user(self):
        tries = 3
        while tries >= 1:
            user_id = input('Enter User ID of user you want to delete:- ')

            if self.check_if_user_present(user_id):
                for user in User.all_user_list:
                    if user_id == user.get_user_id():
                        User.all_user_list.remove(user)
                        print(f'{user_id} deletion successfull')
                        return
            else:
                print('User Not Found')
                tries -= 1
                print(f'Try Again (You got {tries} left)')

    def add_user(self):
        role = self.determining_roles()
        print(role)

        if role == 'Teacher':
            teacher = Teacher()
            teacher_name = input('Enter New Teacher Full Name:- ')
            teacher_user_id = input('Enter New Teacher User ID:- ')
            teacher_email = input('Enter New Teacher Email:-')
            teacher_password = input('Enter New Teacher Password')

            teacher.set_name(teacher_name)
            teacher.set_user_id(teacher_user_id)
            teacher.set_email(teacher_email)
            teacher.set_password(teacher_password)

        elif role == 'Student':
            student = Student()
            student_name = input('Enter New Student Full Name:- ')
            student_user_id = input('Enter New Student User ID:- ')
            student_email = input('Enter New Student Email:-')
            student_password = input('Enter New Student Password')

            student.set_name(student_name)
            student.set_user_id(student_user_id)
            student.set_email(student_email)
            student.set_password(student_password)