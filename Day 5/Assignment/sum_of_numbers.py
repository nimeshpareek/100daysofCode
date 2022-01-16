# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
counter = 0
sum = 0
#print(type(sum))

for n in range(0, len(student_heights)):
    counter = counter + 1

for n in range(0, len(student_heights)):
 sum = sum + student_heights[n]

average = round(sum/counter)
print(average)

# length = len(student_heights)
# sum_heights = (sum(student_heights)/length)
# int_sum = int(sum_heights)
# print(int_sum)

