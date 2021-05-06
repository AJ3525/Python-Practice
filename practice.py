# # pet introduction
# animal = "cat"
# name = "sexy"
# age = 4
# hobby = "sleeping"
# is_adult = age >= 3


# ''' ctrl + /'''

# print("my " + animal + " is " + name)
# hobby = "balling"
# #print(name + " is " + str(age) + "years old, loves " + hobby)
# print(name, " is ", age, "years old, loves ", hobby)
# print("is " + name + " an adult?" + str(is_adult))

# station = "Finch"
# print("Subway is arriving going to", station)
# station = "North York Centre"
# print("Subway is arriving going to", station)
# station = "Sheppard"
# print("Subway is arriving going to", station)
# 슬라이싱 ----------------------------------------------
# jumin = "123456-1234567"
# print("gender: " + jumin[7])
# print("Year: " + jumin[0:2])  # 0 부터 2 직전까지
# print("Month : " + jumin[2:4])
# print("date: " + jumin[4:6])

# print("BOD: " + jumin[:6])  # 첨부터 6직전까지
# print("7digits : " + jumin[7:])  # 7부터 끝까지
# print("뒤 7자리 뒤에서부터 : " + jumin[-7:])  # 맨뒤에서 7번째부터 끝까지
# 문자열 처리함수 - ------------------------
# python = "Python is Amazing"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper())
# print(len(python))
# print(python.replace("Python", "Java"))
#


# print(index)

# print("나는 %d살입니다. " % 20)
# print(" I like %s color and %s color." % ("blue", "red"))

# print("I am {} years old" .format(20))
# print(" I like {} color and {}color.".format("blue", "red"))

# print(" I like {0} color and {1}color.".format("blue", "red"))

# print(" I like {1} color and {0}color.".format("blue", "red"))

# print(" I am {age} years old, like {color} color.".format(age=20, color="red"))


# age = 20
# color = "Red"
# print(f"I am {age} years old and like {color} color.")

# print("Ang \n      Gimotti")
# print("Ang 'Gimotti'")
# print('Ang "Gimotti"')
# print("Ang \"Gimotti\"")

# # print("C:\\Users\\mseok\\Desktop\\PythonWorkspace>")
# print("Rd Apple\rPine")  # \r 는 커서 압으로 이동해서 Pine 을 Rd 덮어 씌기

# print("Redd\b Apple")  # \b 는 백스페이스

# print("Red\tApple")
# 리스트

subway = [10, 20, 30]
print(subway)

subway = ["gimotti", "Ang", "Oishi"]
print(subway)

print(subway.index("gimotti"))
