class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def add_grade(self, course, grade):
        if isinstance(grade, float) and 0 <= grade <= 10:
            self.grades.append(grade)

    @property
    def average_grade(self):
        all_grades = [grade for grades_list in self.grades.values() for grade in grades_list]
        return sum(all_grades) / len(all_grades) if all_grades else None

    def __str__(self):
        avg_grade = f"{self.average_grade:.1f}" if self.average_grade is not None else 'Нет оценок'
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {avg_grade}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.average_grade == other.average_grade

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_grade < other.average_grade


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.courses_in_progress = []
        self.grades = {}

    def add_grade(self, grade):
        if isinstance(grade, float) and 0 <= grade <= 10:
            self.grades.append(grade)

    @property
    def average_grade(self):
        all_grades = [grade for grades_list in self.grades.values() for grade in grades_list]
        return sum(all_grades) / len(all_grades) if all_grades else None

    def __str__(self):
        avg_grade = f"{self.average_grade:.1f}" if self.average_grade is not None else 'Нет оценок'
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg_grade}'

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade == other.average_grade

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade < other.average_grade


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


def average_grade_students(students, courses):
    total_grades = []
    for student in students:
        if courses in student.grades:
            total_grades.extend(student.grades[courses])
    return sum(total_grades) / len(total_grades) if total_grades else 0


reviewer1 = Reviewer('Jon', 'Snow')
reviewer1.courses_attached += ['Git']

reviewer2 = Reviewer('Sansa', 'Stark')
reviewer2.courses_attached += ['Git', 'Java']

lecturer1 = Lecturer('Daenerys', 'Targaryen')
lecturer1.courses_attached += ['Python', 'Git']
lecturer1.grades = {'Python': [8], 'Git': [10]}
lecturer2 = Lecturer('Tyrion', 'Lannister')
lecturer2.courses_attached += ['Python', 'Java']
lecturer2.grades = {'Python': [10], 'Java': [7]}

student1 = Student('Jaime', 'Lannister', 'Male')
student1.grades = {'Python': [10], 'Git': [9]}
student1.courses_in_progress = ['Python', 'Git']
student1.finished_courses = ['Введение в программирование']
student2 = Student('Arya', 'Stark', 'Female')
student2.grades = {'Python': [9], 'Java': [8]}
student2.courses_in_progress = ['Python', 'Java']
student2.finished_courses = ['Git']

students = [student1, student2]
average_python_grade = average_grade_students(students, 'Python')
average_git_grade = average_grade_students(students, 'Git')
average_java_grade = average_grade_students(students, 'Java')

print('Проверяющие:  ')
print(reviewer1)
print(reviewer2)
print('Лекторы:  ')
print(lecturer1)
print(lecturer2)
print(lecturer1.grades)
print(lecturer2.grades)
print('Студенты:  ')
print(student1)
print(student2)

print(f'Средняя оценка студентов по курсу Git: {average_git_grade:.1f}')
print(f'Средняя оценка студентов по курсу Python: {average_python_grade:.1f}')
print(f'Средняя оценка студентов по курсу Java: {average_java_grade:.1f}')