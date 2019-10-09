from graphics import *
import time

ballRadius = 20

def main():
    win = GraphWin("My Circle", 480, 640, autoflush=False)
    #win.setBackground(color_rgb(0, 0, 0))
    ball1 = Circle(Point(250,250), ballRadius)
    ball1.setFill(color_rgb(130, 0, 130))
    ball1V = [20, 5]
    ball2 = Circle(Point(300,300), ballRadius)
    ball1.setFill(color_rgb(130, 0, 130))
    ball2V = [12, 5]
    balls = [ball1, ball2]
    velocities = [ball1V, ball2V]

    border = Rectangle(Point(1,1), Point(479, 639))
    border.draw(win)

    for ball in balls:
        ball.draw(win)
    while(True):
        for i in range(0, len(balls)):
            location = balls[i].getCenter()
            if location.x >= 480 - ballRadius or location.x <= 0 + ballRadius:
                velocities[i][0] = -velocities[i][0]
            if location.y >= 640 - ballRadius or location.y <= 0 + ballRadius:
                velocities[i][1] = -velocities[i][1]

            balls[i].move(velocities[i][0], velocities[i][1])
        update(30)
    #win.getMouse() # Pause to view result
    win.close()    # Close window when done

main()