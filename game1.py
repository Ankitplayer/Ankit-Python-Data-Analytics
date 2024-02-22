import pgzrun

WIDTH = 800
HEIGHT = 500    

def draw():
    screen.draw.text(
        "Hello, Pygame Zero!",
        topleft=(20, 20),
        fontsize=32,
        color="Yellow"
    )

def update():
    pass

pgzrun.go()