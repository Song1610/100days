# 25-02-18

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

# Pause 1. MAX
max = 0
for score in student_scores:
    if max <= score:
        max = score
    elif max > score:
        max = max

print(max)