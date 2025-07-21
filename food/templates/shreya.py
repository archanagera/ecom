def largest(n1,n2,n3):
    lar=0
    if n1>n2 and n1>n3:
        lar= n1
    elif n2>n1 and n2>n3:
        lar= n2
    else:
        lar=n3
    return lar

x1=largest(10,6,4)
x2=largest(9.9,7.8,8)
x3=largest(4,8.6,6)

print(largest(x1,x2,x3))      