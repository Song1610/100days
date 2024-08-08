student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
######################################################

# sum height
total_height = 0
for height in student_heights:
    total_height = total_height + height  # total_height += height
    # print(total_height)
print("total height = ", total_height)

# number count
number = 0
for student in student_heights:
    number = number + 1
    #print(number)
print("number of students = ", number)

# average height
average_height = round(total_height / number)
print("average height = ", average_height)
