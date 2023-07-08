import turtle
import test
import time
isKey=False
w_size=982
h_size=443
turtle.setup(w_size,h_size)
key_rect=(330,370,110,150)
key_cord=(350,130)
exit_rect=(-460,-400,120,180)
exit_cord=(-430,150)

inLoop=True
class Sprite(turtle.Turtle):
    def __init__(self,speed,shape):
        super().__init__()
        self.shape(shape)
        self.speed(speed)
        self.speed=speed
        self.up()
    def enemy(self,speed):
        self.speed(speed)
    def check_rect(self,rect):
        x1,x2,y1,y2=rect
        x,y=self.pos()
        if x1<=x<=x2 and y1<=y<=y2:
            return 1
        else:
            return 0
    def wall_move(self):
        if self.side=="right":
            if self.check_barrier("right"):
                self.goto(self.xcor()+self.speed,self.ycor())
                self.rect=(self.xcor()-32,self.xcor()+32,self.ycor()-32,self.ycor()+32)
            else :
                self.speed*=-1
                self.side="left"
        else:
            if self.check_barrier("left"):
                self.goto(self.xcor()+self.speed,self.ycor())
                self.rect=(self.xcor()-32,self.xcor()+32,self.ycor()-32,self.ycor()+32)
            else:
                self.speed*=-1
                self.side="right"
    def check_size(self,dirr):
        x,y=self.pos()
        for x1,x2,y1,y2 in sides_cords:
            if dirr=="up":
                if x1<=x<=x2 and y1<y+20<y2:
                    self.goto(x,y-20)
            if dirr=="right":
                if y1<=y<=y2 and x1<x+20<x2:
                    self.goto(x-20,y)
            elif dirr=="left":
                if y1<=y<=y2 and x1<x-20<x2:
                    self.goto(x+20,y)
            else:
                if x1<=x<=x2 and y1<y-20<y2:
                    self.goto(x,y+20)
        return True
    
    def check_barrier(self,dirr):
        if dirr=="down":
            if self.ycor()-5>-h_size/2+10:
                return 1
            else:
                return 0
        elif dirr=="up":
            if self.ycor()+5<h_size/2-10:
                return 1
            else:
                return 0
        elif dirr=="right":
            if self.xcor()+5<w_size/2-10:
                return 1
            else:
                return 0
        else:
            if self.xcor()-5>-w_size/2+10:
                return 1
            else:
                return 0
            
    def m_right(self):
        if self.check_barrier("right") and self.check_size("right"):
            self.goto(self.xcor()+5,self.ycor())
    def m_left(self):
        if self.check_barrier("left") and self.check_size("left"):
            self.goto(self.xcor()-5,self.ycor())
    def m_up(self):
        if self.check_barrier("up") and self.check_size("up"):
            self.goto(self.xcor(),self.ycor()+5)
    def m_down(self):
        if self.check_barrier("down") and self.check_size("down"):
            self.goto(self.xcor(),self.ycor()-5)
def hide():
    lines.clear()
    lines.ht()
    screen.clear()
    player.ht()
    key.ht()
    key.clear()
    manhole.ht()
    enemy.ht()
lines=turtle.Turtle()
sides_cords=test.sides(lines,10)

turtle.register_shape("manhole.gif")
manhole=Sprite(100,"manhole.gif")
manhole.setposition(exit_cord)

turtle.register_shape("pizza.gif")
key=Sprite(100,"pizza.gif")
key.setposition(key_cord)

turtle.register_shape("ghost.gif")
enemy=Sprite(7,"ghost.gif")
enemy_cord=0,10
enemy.setposition(enemy_cord)
enemy.rect=(enemy.xcor()-32,enemy.xcor()+32,enemy_cord[1]-32,enemy_cord[1]+32)

turtle.register_shape("small_player.gif")
player=Sprite(20,"small_player.gif")
player.setpos(320,-145)

screen=turtle.getscreen()
screen.listen()
screen.onkeypress(player.m_right,"Right")
screen.onkeypress(player.m_left,"Left")
screen.onkeypress(player.m_up,"Up")
screen.onkeypress(player.m_down,"Down")
enemy.side="right"
turtle.ht()
key.start=0
while inLoop:
    enemy.wall_move()
    if player.check_rect(enemy.rect):
        inLoop=False
        hide()
        enemy.setpos((0,0))
        enemy.write("you lose",align="center",font=("Arial",15,"normal"))
    elif player.check_rect(key_rect):
        key.start=time.time()
        isKey=True
        key.ht()
        key.write("Collected", align="center",font=("Arial",10,"normal"))
        key_rect=0,0,0,0
        enemy.speed*=1.5
    elif player.check_rect(exit_rect):
        if isKey:
            hide()
            manhole.goto(0,0)
            manhole.write("You have won",align="center", font=("Arial",15,"normal"))
            inLoop=False

    if time.time()-5>=key.start:
            key.clear()
    screen.update()
turtle.done()