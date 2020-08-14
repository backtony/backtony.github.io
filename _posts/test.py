"""
# 모듈 가져오기
import math

# 클래스 선언
class Circle:
    def __init__(self,radius):
        if radius <= 0:
            raise TypeError("양수를 넣어주세요")
        self.__radius = radius
    def get_circumference(self):
        return 2 * math.pi * self.__radius
    def get_area(self):
        return math.pi*(self.__radius**2)
    def get_radius(self):
        return self.__radius
    def set_radius(self,value):
        if value<=0 :
            raise TypeError("길이가 양의 숫자여야 한다.")
        self.__radius = value        

circle = Circle(10)
print("원의 둘레 :",circle.get_circumference())
print("원의 넓이 :",circle.get_area())

print("__radius 에 접근")
print(circle.get_radius())
circle.set_radius(15)
print(circle.get_radius())
"""
# 모듈 가져오기
import math

# 클래스 선언
class Circle:
    def __init__(self,radius):
        if radius <= 0:
            raise TypeError("양수를 넣어주세요")
        self.__radius = radius
    def get_circumference(self):
        return 2 * math.pi * self.__radius
    def get_area(self):
        return math.pi*(self.__radius**2)
    @property
    def radius(self):
        return self.__radius
    @radius.setter
    def radius(self,value):
        if value<=0 :
            raise TypeError("길이가 양의 숫자여야 한다.")
        self.__radius = value        

circle = Circle(10)
print("원의 둘레 :",circle.get_circumference())
print("원의 넓이 :",circle.get_area())

print("원래 반지름 :",circle.radius)
circle.radius = 15
print("변경된 반지름 :",circle.radius)
"""
print("__radius 에 접근")
print(circle.get_radius())
circle.set_radius(15)
print(circle.get_radius())"""