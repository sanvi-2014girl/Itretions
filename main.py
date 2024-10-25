def function1(s, m):
    result = 0
    for _ in range(s):
        result = result + m
    return result
print(function1(3,5))

def function2(s):
    sum = 0
    for i in range(1,s+1):
         sum = sum+i
    return sum
print(function2(5))

def function3(s):
    sum = 0
    for i in range(1,s+1):
        for j in range(1,i+1):
             sum = sum+1
    return sum
print(function3(5))