student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for score in student_scores:
    sc = student_scores[score]
    if sc > 90 :
        student_grades[score] = "Outstanding"
    elif 80 < sc <= 90 :
        student_grades[score] = "Exceeds Expectations" 
    elif 70 < sc <= 80 :
        student_grades[score] = "Acceptable" 
    elif sc <= 70 :
        student_grades[score] = "Fail" 

print(student_grades)