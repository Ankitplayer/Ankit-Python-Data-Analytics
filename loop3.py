from turtle import*
speed('fastest')
pencolor('blue')
bgcolor('green')

for i in range(5):
    fd(75)
    for i in range(5):
        fd(75)
        lt(360/5)
    lt(360/5)
    dot(20)

hideturtle()
mainloop()