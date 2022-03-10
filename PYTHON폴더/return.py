a=int(input("숫자"))
b=int(input("다음숫자"))
c=int(input("1=덧셈,2=뺄셈,3=곱셈,4=나눗셈"))
if c==1:
    print(a+b)
elif c==2:
    print(a-b)
elif c==3:
    print(a*b)
else:
    print(a/b)