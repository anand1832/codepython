class grade:

    def __init__(self):
        self.rollno=0
        self.name=0
        self.marks=0
        
    def get(self,r,n,mark):
        self.rollno=r
        self.name=n
        self.marks=mark
        if self.marks>=90:
            print("Grade: A")
            print("RollNO: ",self.rollno)
            print("Name: ",self.name)
            print("Marks: ",self.marks)
        elif self.marks>=80 and mark<=89:
            print("Grade: B")
            print("RollNO: ",self.rollno)
            print("Name: ",self.name)
            print("Marks: ",self.marks)
        elif self.marks>=70 and mark<=79:
            print("Grade: c")
            print("RollNO: ",self.rollno)
            print("Name: ",self.name)
            print("Marks: ",self.marks)
        elif self.marks>=60 and mark<=69:
            print("Grade: c")
            print("RollNO: ",self.rollno)
            print("Name: ",self.name)
            print("Marks: ",self.marks)
        elif self.marks>=50 and mark<=59:
            print("Grade: D")
            print("RollNO: ",self.rollno)
            print("Name: ",self.name)
            print("Marks: ",self.marks)
        else:
            print("Grade: F")
            print("RollNO: ",self.rollno)
            print("Name: ",self.name)
            print("Marks: ",self.marks)
s=grade()
s.get(101,"Abc",99)
