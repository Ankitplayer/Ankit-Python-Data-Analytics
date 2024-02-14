from turtle import *
speed(0)

def polygon(side, size, color):
    fillcolor(color)
    begin_fill|()
    for _ in range(side):
        fd(100)
        lt(360/side)
        end_fill

#testing the function
for i in range(6):
    polygon(side = 10, size = 50, color = 'blue')
    polygon(side = 6, size = 80, color = 'yellow')
    polygon(4, 100, color = 'green')
    lt(60)

hideturtle()
mainloop()    



