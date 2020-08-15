import datetime

now = datetime.datetime.now()

# 여러가지 시간 출력 방법 : strftime
output_a = now.strftime("%Y년 %m월 %d일 %H:%M:%S")
output_b = "{}년 {}월 {}일 {}시 {}분 {}초".format(now.year,\
    now.month,now.day,now.hour,now.minute,now.second)
output_c = now.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초")
# 문자열, 리스트 등 앞에 *를 붙이면 요소 하나하나가 매개변수로 지정

print(output_a)
print(output_b)
print(output_c)

# 특정 시간 이후의 시간 구하기 : timedelta
after = now + datetime.timedelta(\
    weeks=1, days=1, hours=1, minutes=1, seconds=1)
print(after.strftime("%Y년 %m월 %d일 %H:%M:%S"))

# 특정 시간 요소 교체: replace
output = now.replace(year=(now.year+1))
print(output.strftime("%Y년 %m월 %d일 %H:%M:%S"))