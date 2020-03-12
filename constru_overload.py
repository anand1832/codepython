class student:
    
   
    def __init__(self,c="Acropolis",i="101"):
        self.clg=c
        self.id=i
    def getout(self):
        print("College is: ",self.clg)
        print("Employee Id: ",self.id)
s=student()
s.getout()
s=student("IIT INDORE",99)
s.getout()
