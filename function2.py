# function2.py
print("불변함수")
a=1.22
print(id(a))
a = 2.3
print(id(a))


print(" 가변형식")

lst = [1,2,3]
print(id(lst))

lst.append(4)
print(id(lst))
print(lst)

print(" 입력 + 출력")
def change(x):
    x[0] = "H"

wordlist = ["j","A","M"]
change(wordlist)
print("호출후", wordlist)

print(" 수정된 입력 + 출력")
def change(x):
    x1 = x[:]
    x1[0] = "H"
    print(" 함수 내부 : ", x1)

wordlist = ["j","A","M"]
change(wordlist)
print("호출후", wordlist)

import copy
lst = [100,200,300]
lst2 = copy.deepcopy(lst)
lst2[0] = 101
print(lst)
print (lst2)
print(id(lst),id(lst2))

x = 5
def func(a):
    return x+a

print(func(1))
def func2(a):
    x = 10
    return x+a

print(func2(1))
