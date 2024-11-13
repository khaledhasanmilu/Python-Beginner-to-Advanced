student = {
    'name':'Rahim',
    'id':2,
    'cgpa':3.73,
    'course':['AI','OS','DBMS'],
    8:'Trimester'
}
print(student['course']) # course print
print(student)      #whole dictonary print
print(student.get('id'))  #print id
print(student.keys())
print(student.values())
print(student.items())
print("Key print in for loop:")
#using loop print key and values
for key in student:
    print(key,student[key])
#using items method print key value    
for k,v in student.items():
    print(k,v)    
print("Append a Key and value:")    
student['Blood Group']='A+'
print(student)
