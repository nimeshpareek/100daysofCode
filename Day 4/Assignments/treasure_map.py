# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
#print(type(position))
position_int = int(position)
#print(position_int)
####print(type(position_int))
column = position_int/10
row = position_int%10
column_int = int(column)
#print(column_int)
#print(row)
map[row-1][column_int-1] = 'X'
print(f"{row1}\n{row2}\n{row3}")

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
