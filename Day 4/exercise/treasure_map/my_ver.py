line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "⬜️", "️⬜️"]
line3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure? ")  #A1 -> a1
####################################################################
num1 = position[0].lower()
spell = ['a', 'b', 'c']
num1_index = spell.index(num1)

num2_index = int(position[1]) - 1

map[num2_index][num1_index] = "X"

####################################################################
print(f"{line1}\n{line2}\n{line3}")
