print("Open to my quiz!!")
playing = input("Do you want to play?")
if playing.lower()!="yes":
  quit()

  print("Okay!Let's play:)")
  score = 0

answer = input("What is the capital City of Bangladesh?")

if answer=="Dhaka":
  print('Correct')
  score += 1
else:
  print('Not Correct!Try again Letter.')
  answer = input("CPU means?")

if answer=="Central Processing Unit":
  print('Correct')
  score += 1
else:
  print('Not Correct!Try again Letter')
  answer = input("GPU means")

if answer=="Graphics Processing Unit":
  print('Correct')
  score += 1
else:
  print('Not Correct!Try again Letter.')
  answer = input("What do you mean for RAM?")

if answer=="Random access Memory":
  print('Correct')
  score += 1
else:
  print('Not Correct!Try again Letter.')


print("You Got  : "+ str(score) + "correct answer")
print("You Got  : "+ str((score / 5) * 100) + "%.")