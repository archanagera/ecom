def checkPrime(n):
    for i in range(2,n):
        if(n%i==0):
            return False
    else:
        return True

def prime(n1,n2):
    lst=[]
    for i in range(n1,n2+1):
        if checkPrime(i):
            lst.append(i)
    return lst

lst=prime(10,50)

print(lst)