### 동영이 파이썬 도와주기 ###
import statistics

class Student:
    def __init__(self, name, grade):
        self._name = name
        self._grade = grade
    
    def get_grade(self):
        return self._grade
    def get_name(self):
        return self._name


def basic_stats(stu_list):
    grade_list = []
    for student in stu_list:
        grade_list.append(student.get_grade())

    mean = statistics.mean(grade_list)
    median = statistics.median(grade_list)
    mode = statistics.mode(grade_list)

    return (mean, median, mode)

s1 = Student("Kyoungmin", 73)
s2 = Student("Mercedes", 74)
s3 = Student("Avanika", 78)
s4 = Student("Marta", 74)

student_list = [s1, s2, s3, s4]
print(basic_stats(student_list))