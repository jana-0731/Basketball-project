#game file2
from gamelib import*

game = Game(800,600,"Basketball")
bk = Image("basketball court.jpg",game)
bk.resizeTo(800,600)

player1 = Image("player1.png",game)
player1.resizeBy(-50)
player1.setSpeed(3,60)

player2 = Image("player2.png",game)
player2.resizeBy(-50)
player2.setSpeed(6,90)

ball = Image("basketball.jpg",game)
ball.resizeBy(-80)
ball.setSpeed(2,80)

#essential game loop
while not game.over:
    game.processInput()

    bk.draw()
    player1.move(True)
    player2.move(True)
    ball.moveTo(mouse.x,mouse.y)
    game.update(30)

game.quit()
