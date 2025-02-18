# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇

high_score = 0
for score in student_scores:
  if high_score <= score:
    high_score = score
    #print(high_score)
  elif high_score > score:
    high_score = high_score
    #print(high_score)
print(f"The highest score in the class is: {high_score}")