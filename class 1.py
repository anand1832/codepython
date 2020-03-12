class student:
    def __init__(self,a,b):
        self.rollno=a
        self.name=b
    def printvalues(self):
        print("rollno=",self.rollno)
        print("name=",self.name)
s1=student(101,"abc")
s1.printvalues()
