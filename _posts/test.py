class Student:
    def __init__(self, name, korean, math):
        self.name = name
        self.korean = korean
        self.math = math
    
    def get_sum(self):
        return self.korean + self.math
    def get_avg(self):
        return self.get_sum() / 2  # ()는 자동적으로 self
        
    def __eq__(self,value):
        return self.get_avg() == value
    def __ne__(self,value):
        return self.get_avg() != value
    def __gt__(self,value):
        return self.get_avg() > value
    def __ge__(self,value):
        return self.get_avg() >= value
    def __lt__(self,value):
        return self.get_avg() < value
    def __le__(self,value):
        return self.get_avg() <= value

student = Student("A",90,90)
print(student == 90)
print(student != 90)
print(student > 90)
print(student >= 90)
print(student < 90)
print(student <= 90)