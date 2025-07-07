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

    def add_grade(self, grade):
        if isinstance(grade, float) and 0 <= grade <= 10:
            self.grades.append(grade)

    @property
    def average_grade(self):
        return sum(self.grades) / len(self.grades) if self.grades else None

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
        return sum(self.grades) / len(self.grades) if self.grades else None

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


some_reviewer = Reviewer('Some', 'Buddy')
some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.grades = {9.9, 10}

some_student = Student('Ruoy', 'Eman', 'Male')
some_student.grades = {9.9, 10}
some_student.courses_in_progress = ['Python', 'Git']
some_student.finished_courses = ['Введение в программирование']

print('Проверяющий:  ')
print(some_reviewer)
print('Лектор:  ')
print(some_lecturer)
print('Студент:  ')
print(some_student)