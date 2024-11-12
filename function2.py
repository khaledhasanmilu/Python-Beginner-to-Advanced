def calculateMarks(att,ct=0,mid=0,final=35):
  return att+ct+mid+final

# print(calculateMarks()) required 1 positional argument
print(calculateMarks(5))
print(calculateMarks(5,10))
print(calculateMarks(ct=19,att=5))
# print(calculateMarks(ct=19,5)) positional argument follows keyword argument
print(calculateMarks(5,ct=19))
print(calculateMarks(5,ct=19,final=37,mid=25))
print(calculateMarks(final = 100,att=5))