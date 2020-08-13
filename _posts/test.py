class Student:
    def __init__(self, name, korean, math):
        self.name = name
        self.korean = korean
        self.math = math

    def get_sum(self):
        return self.korean + self.math

    def get_avg(self):
        return self.get_sum() / 2  # ()는 자동적으로 self

student = [Student("장보고",85,95), Student("이순신",90,93), Student("손오공",85,90)]
for i in student:
    print("{}의 평균 : {}".format(i.name,i.get_avg()))
    