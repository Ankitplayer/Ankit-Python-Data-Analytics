from turtle import*
speed(0)
def hexagon():
    for _ in range(6):
        fd(100)
        lt(60)

def pentragon():
    for _ in range(5):
        fd(50)
        lt(72)

# testing the functions
for i in range(6):
    fd(100)
    hexagon()
    pentragon()
    lt(50)

hideturtle()
mainloop()


