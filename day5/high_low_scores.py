student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 300, 78, 65, 89, 86, 55, 91, 64, 89]
largest_num = student_scores[0]
small_num = student_scores[0]
for num in student_scores:
    if num > largest_num:
        largest_num = num
print(largest_num)

for num in student_scores:
    if num < small_num:
        small_num = num
print(small_num)