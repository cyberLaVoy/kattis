
equation = input().split()
a = int(equation[0])
b = int(equation[1])
c = int(equation[2])

if a-b == c:
    print(str(a),'-',str(b),'=',str(c),sep='')
elif a == b-c:
    print(str(a),'=',str(b),'-',str(c),sep='')
elif a+b == c:
    print(str(a),'+',str(b),'=',str(c),sep='')
elif a == b+c:
    print(str(a),'=',str(b),'+',str(c),sep='')
elif a*b == c:
    print(str(a),'*',str(b),'=',str(c),sep='')
elif a == b*c:
    print(str(a),'=',str(b),'*',str(c),sep='')
elif a/b == c:
    print(str(a),'/',str(b),'=',str(c),sep='')
elif a == b/c:
    print(str(a),'=',str(b),'/',str(c),sep='')


