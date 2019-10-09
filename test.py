from graphics import *
import time
import math

ballRadius = 20

def main():
    win = GraphWin("My Circle", 480, 640, autoflush=False)
    #win.setBackground(color_rgb(0, 0, 0))
    ball1 = Circle(Point(250,250), ballRadius)
    ball1.setFill(color_rgb(130, 0, 130))
    ball1V = [20, 5]
    ball2 = Circle(Point(100,100), ballRadius)
    ball2.setFill(color_rgb(0, 0, 255))
    ball2V = [-15, -1]
    balls = [ball1, ball2]
    velocities = [ball1V, ball2V]

    border = Rectangle(Point(1,1), Point(479, 639))
    border.draw(win)

    for ball in balls:
        ball.draw(win)

    changed = False
    while(True):
        changed = False

        for i in range(0, len(balls)):
            location = balls[i].getCenter()
            if location.x >= 480 - ballRadius or location.x <= ballRadius:
                velocities[i][0] = -velocities[i][0]
                changed = True
            if location.y >= 640 - ballRadius or location.y <= ballRadius:
                velocities[i][1] = -velocities[i][1]
                changed = True

        # check collisions
        if not changed:
            ball1Loct = balls[0].getCenter()
            ball2Loct = balls[1].getCenter()
            if math.sqrt((ball2Loct.x - ball1Loct.x)**2 + (ball2Loct.y - ball1Loct.y)**2) <= (2 * ballRadius):
                #for i in range(0, len(velocities)):
                #    velocities[i][0] = -velocities[i][0]
                #    velocities[i][1] = -velocities[i][1]
                temp = velocities[0][0]
                velocities[0][0] = velocities[1][0]
                velocities[1][0] = temp
                temp = velocities[0][1]
                velocities[0][1] = velocities[1][1]
                velocities[1][1] = temp

        for i in range(0, len(balls)):
            balls[i].move(velocities[i][0], velocities[i][1])

        update(30)
    #win.getMouse() # Pause to view result
    win.close()    # Close window when done

main()