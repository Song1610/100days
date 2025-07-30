# import another_module

# print(another_module.another_variable)


from turtle import Turtle, Screen

timmy = Turtle()

print(timmy)
timmy.shape("turtle")
timmy.color("DeepPink")     # challenge 1
timmy.forward(100)          # challenge 2 거북이가 100걸음 걷게하기

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()