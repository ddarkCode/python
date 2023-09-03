# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
total_students_height = 0
count = 0

for student_height in  student_heights:
    total_students_height += student_height
    count += 1

average_height = round(total_students_height/count)

print(average_height)


