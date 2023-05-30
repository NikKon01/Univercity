class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def rate_hw(self, student, course, grade):
        student.grades[course] = [grade]

    def __bool__(self, student):
        for course in student.courses_in_progress:
            if self.courses.__contains__(course):
                return True
        return False


class Lecturer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.grades = {}

    def rate_hw(self, student, course, grade):
        if student is Student and course in student.finished_courses and course in self.courses:
            if course in self.grades:
                self.grades[course].append(grade)

    def __str__(self):
        if len(self.grades) == 0:
            return 'нет оценок'
        avg_grade = sum(self.grades) / len(self.grades)
        return f'Имя: {self.name} Фамилия: {self.surname} Средняя оценка за лекции {avg_grade:.1f}'


class Reviewer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)

    def rate_hw(self, student, course, grade):
        if course in self.courses and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]

    def __str__(self):
        return f"Имя: {self.name} Фамилия: {self.surname}"


class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.grades = {}
        self.courses_in_progress = []
        self.finished_courses = []

    def add_course(self, course_name):
        self.courses_in_progress.append(course_name)

    def finish_course(self, course_name):
        if course_name in self.courses_in_progress:
            self.courses_in_progress.remove(course_name)
            self.finished_courses.append(course_name)

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses:
            if course in self.grades:
                self.grades[course].append(grade)
            else:
                self.grades[course] = [grade]

    def __float__(self):
        total_sum = 0
        count = 0
        for grades in self.grades.values():
            for grade in grades:
                total_sum += grade
                count += 1
        if len(count) == 0:
            return 'нет оценок'
        return total_sum / count

    def __str__(self):
        avg_grade = sum(sum(grades) for grades in self.grades.values()) / sum(
            len(grades) for grades in self.grades.values())
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return f'Имя: {self.name} Фамилия: {self.surname}\nСредняя оценка за домашние задания {avg_grade:.1f} \n' \
               f'Курсы в процессе изучения: {courses_in_progress}\nЗавершенные курсы: {finished_courses}'

course1 = 'Algebra'
course2 = 'English'


reviewer1 = Reviewer('Tatyana', 'Kupr')
reviewer2 = Reviewer('Alexey', 'Privalov')

lecturer1 = Lecturer('Galina', 'Emgusheva')
lecturer2 = Lecturer('Marina', 'Shatkova')

student1 = Student('Nikolay', 'Konyahin')
student2 = Student('Ivan', 'Razin')

student1.add_course(course1)
student2.add_course(course2)
lecturer1.add_course(course1)
lecturer2.add_course(course2)

student1.rate_lecture(lecturer1, course2, 3)
student1.rate_lecture(lecturer2, course2, 5)
student2.rate_lecture(lecturer1, course2, 3)
student2.rate_lecture(lecturer2, course1, 4)

student1.add_course(course2)
student1.add_course(course1)
student2.add_course(course2)
student2.add_course(course1)
student1.grades = {course2: [5, 4], course1: [4]}
student2.grades = {course2: [4, 3], course1: [5]}

student1.finish_course(course1)
student2.finish_course(course2)

print(f"Проверяющий 1: {reviewer1}")
print(f"Проверяющий 2: {reviewer2}")

print(f"Лектор 1: {lecturer1}")
print(f"Лектор 2: {lecturer2}")

print(f"Студент 1: {student1}")
print(f"Студент 2: {student2}")

print(f"Лектор ведет пары у студента: {lecturer1.__bool__(student1)}")

def avg_grade_hw(person_list, course_name):
    grade_sum = 0
    courses = 0
    for person in person_list:
        if course_name in person.courses_in_progress:
            grade_sum += sum(map(lambda sublist: sum(sublist), person.grades.values()))
            courses += 1
    return grade_sum / courses


print(f"Средняя оценки за курс {course2} ученика {student1}: {avg_grade_hw([student1], course2)}")
print(f"Cредняя оценка за курс {course1} учеников {student1} {student2}: {avg_grade_hw([student1, student2], course1)}")