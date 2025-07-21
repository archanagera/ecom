class Student:
    def __init__(self,rno,name):
        self.rno=rno
        self.name=name

    def __str__(self):
        print("in str")
        return self.name

rno=int(input("Enter rno"))
name=input("Enter name")
obj1=Student(rno,name)

print(obj1)
        


