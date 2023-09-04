# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

highest_possible_number = -1

for score in student_scores:
    if score > highest_possible_number:
        highest_possible_number = score

print(f'The highest score in the class is: {highest_possible_number}')




