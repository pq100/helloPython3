def add(x, y):
    return x + y

def minus(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

# 모듈사용하기 1 - 모듈명.함수명

import snicuz

val = snicuz.calc.add(10, 5)
print(val)

# 모듈사용하기 2 - 함수명
from snicuz.calc import add

val = add(10, 5)
print(val)
val = div(10, 5)
print(val)

# 모듈사용하기 3 - 함수명
from snicuz.calc import  *

val = mul(10,5)
print(val)
val = minus(10,5)
print(val)


