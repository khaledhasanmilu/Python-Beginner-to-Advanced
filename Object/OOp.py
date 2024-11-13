class student:
    def __init__(self,name,id,cgpa,trimester):
     self.name = name
     self.id  = id
     self.__cgpa = cgpa
     self.trimester = trimester
    def getCgpa(self): #for access private cgpa
       return self.__cgpa
    
    @staticmethod       #direct static method --without create any object we call this method
    def study():
       print("Studing!!")    
    def __str__(self):
        return self.name+" "+str(self.id)+" "+(self.trimester)       
st = student('Rahim',10,3.76,'5th')
print(st.name) 
print(st.getCgpa())    
student.study()  # static call
print(str)