import random
import pgzrun

HEIGHT = 500
WIDTH = 800

class Hero(Actor):
    def move(self):
        
        if keyboard.left:
            self.x -= 5
        elif keyboard.right:
            self.x += 5
        elif keyboard.up:
            self.y -= 5
        elif keyboard.down:
            self.y += 5

    def warp(self):
        if self.x > WIDTH:
            self.x = 0
        if self.x < 0:
            self.x = WIDTH
        if self.y > HEIGHT:
            self.y = 0
        if self.y < 0:
            self.y = HEIGHT

        
        
class ship(Actor):
    def track(self, player, speed=1):
        if player.x > self.x:
            self.x += speed
        elif player.x < self.x:
            self.x -= speed
        if player.y > self.y:
            self.y += speed
        elif player.y < self.y:
            self.y -= speed
        

HEIGHT = 500
WIDTH = 800
p = Hero('naruto', (100, 100))
b = Rect((300, 100), (50, 50))  # position, size
s = ship('pain', (1000, 1000))
e = ship('pain', (300, 1000))

def draw():
    screen.fill('black')
    p.draw()
    s.draw()
    e.draw()
    p.wrap()
    screen.draw.filled_rect(b, 'blue')
def update():
    p.move()
    p.wrap()
    s.track(p,2)
    e.track(p,1)

pgzrun.go()