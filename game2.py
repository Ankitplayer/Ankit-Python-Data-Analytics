import random
import pgzrun

class Hero(Actor):
    def move(self, dx=3, dy=0):
        if keyboard.left:
            self.x -= 5
        elif keyboard.right:
            self.x += 5
        elif keyboard.up:
            self.y -= 5
        elif keyboard.down:
            self.y += 5

HEIGHT = 500
WIDTH = 800
p = Hero('naruto', (100, 100))
b = Rect((300, 100), (50, 50))  # position, size
def draw():
    screen.fill('white')
    p.draw()
    screen.draw.filled_rect(b, 'blue')
def update():
    p.move(dx=3)

pgzrun.go()