direction = "right"
my_list = [0,1,0,0]
def move(my_list, direction):
  index = my_list.index(1)
  if direction == "right":
    if index < len(my_list) -1:
      my_list.remove(1)
      my_list.insert(index + 1,1)
    else:
      print("you are already at the end of the screen")
  elif direction == "left":
    if index > 0:
      my_list.remove(1)
      my_list.insert(index - 1,1)
    else:
      print("the pig is already at the end of the screen")
  return my_list
my_list = move(my_list,direction)
print(my_list)
