def times (a=10, b=20):
    return a*b

print(times())
print(times(5))
print(times(5,6))

def connectURI(server, port):
    strURL = "http://"+ server +":" + port
    return strURL

# 호출
print(connectURI("ycampus.com","80"))
print(connectURI(port="80",server="ycampus.com"))

#가변인자(*는  tuple로 넘기는 경우)

def union (*ar):
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

print (union("HAN", "EGG"))
print (union("HAM", "EGG", "SPAM"))

#람다 함수
g = lambda x,y:x*y

print(g(3,4))
print(g(5,6))

print((lambda x:x*x)(3))
print (globals())