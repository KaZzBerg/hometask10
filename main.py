class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, course, group, avg_grade):
        super().__init__(name, age)
        self.course = course
        self.group = group
        self.avgrade = avg_grade

    def _show_info(self):
        print(f'Student: ', end='\n'
                                f'Name: {self.name} '
                                f'Age: {self.age} '
                                f'Course: {self.course} '
                                f'Group: {self.group}')


class Teacher(Person):
    def __init__(self, name, age, discipline):
        super().__init__(name, age)
        self.discipline = discipline

    def _show_info(self):
        print(f'Teacher: ', end='\n'

                                f'Name: {self.name} '
                                f'Age: {self.age} '
                                f'Discipline: {self.discipline} ')


class Subject:
    def __init__(self, name):
        self.name = name

    def _show_info(self):
        print(f'Subject: {self.name}')


class Department:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def _show_info(self):
        print(f'Department name: {self.name}')
        for subject in self.subject:
            subject._show_info()
            print()


class Academy(Department):
    def __init__(self, name, students, teachers, departments):
        super().__init__(students, teachers)
        self.name = name
        self.students = students
        self.teachers = teachers
        self.departments = departments

    def show_info(self):
        print(f'Academy name: ', self.name)
        for students in self.students:
            students._show_info()
            print()
        for teachers in self.teachers:
            teachers._show_info()
            print()
        for departments in self.departments:
            departments._show_info()


subjects_cs = [Subject('Data protection'),
               Subject('Physics'),
               Subject('Informatics'),
               Subject('Higher Math')]
subjects_pe = [Subject('Python'),
               Subject('C#')]
my_departments = [Department('Cyber Security', subject=subjects_cs),
                  Department('Program Engineering', subject=subjects_pe)]
my_students = [Student('Anton', 20, 2, 221, 4.4),
               Student('Vlad', 21, 3, 231, 3.3)]
my_teachers = [Teacher('Sergey', 40, 'Physics'),
               Teacher('Dmitriy', 35, 'Python')]

academy = Academy('Odessа Polytechnic National University', my_students, my_teachers, my_departments)
academy.show_info()
