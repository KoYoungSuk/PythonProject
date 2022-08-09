import python_moduletest as pm

a = input('첫번째 숫자 입력: ')

b = input('두번째 숫자 입력: ')

a = int(a)
b = int(b)

print(str(a), "+", str(b), "=", str(pm.plus(a,b)))
print(str(a), "-", str(b), "=", str(pm.minus(a,b)))
print(str(a), "*", str(b), "=", str(pm.multiple(a,b)))
print(str(a), "/", str(b), "=", str(pm.division(a,b)))