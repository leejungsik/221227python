# demoLoop 다중라인 주석 ctr+/


# score = int(input("점수를 입력 :"))

# if 90 <= score <= 100:
#     grade = "A"
# elif 80 <= score <90:
#     grade = "B"
# elif 70 <= score <80:
#     grade = "C"
# else:
#     grade = "D"

# print("등급은 ",grade)

value = 5
while value > 0:
    print(value)
    value -= 1

d = {"apple":100, "orange":200, "banana":300}
for item in d.items():
    print(item)

print ("------break-------")
lst = [1,2,3,4,5,6,7,8,9,10]
for i in lst:
    if i >5:
        break
    print("item:{0}".format(i))

print ("------continue-------")
lst = [1,2,3,4,5,6,7,8,9,10]
for i in lst:
    if i %2 == 0:
        continue
    print("item:{0}".format(i))


print("--------수열함수--------")
print(list(range(10)))
print(list(range(2000,2023)))
print(list(range(1,32)))


lst=list(range(1,11))
print([i*2 for i in lst if i >5])

d={100:"apple", 200:"banana", 300:"kiwi"}
print([v.upper() for v in d.values()])

print("----filtering----")
lst=[10,25,30]
iterL = filter(None, lst)
for item in iterL:
    print(item)

#함수정의
def getBiggerThan20(i):
    return i > 20

print("filter Function")
iterL = filter (getBiggerThan20, lst)
for item in iterL:
    print(item)

print("----Lambda Function--")
iterL = filter(lambda i:i>20, lst)
for item in iterL:
    print(item)

