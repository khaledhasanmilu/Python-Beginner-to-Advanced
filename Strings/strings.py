# There are three way for define strings
a = "khaled hasan milu"
b = 'khaled hasan milu'
c = """ khaled hasan milu"""
print(a)
print(b)
print(c)
print(type(a))

str1 = "This is a string.\nSo be patiant."
type1 = len(str1)
print("Str1 length: ",type1)
print(str1)

str2 = "Ok vaiya"
print("Str2 length: ",len(str2))
final = str1 +" "+str2
print(final," Total final length: ",len(final))

#indexing
print(str2[1])

#slicing -- accessing parts of a strings
str = "PythonProgramming"
print(str[1:4]) #4 include nehi thats why it print 1-3
print(str[0:]) # 0 to last
print(str[3:len(str)])

#negetive slicing
#backword - {-5,-4,-3,-2,-1}
print("Backward")
print(str[-5:-2])

a = input()
