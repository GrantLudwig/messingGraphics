from graphics import *
import time
import math

ballRadius = 10

def main():
    win = GraphWin("My Circle", 480, 640, autoflush=False)
    win.setBackground(color_rgb(0, 0, 0))
    ball1 = Circle(Point(250,250), ballRadius)
    ball1.setFill(color_rgb(130, 0, 130))
    ball1V = [20, 5]
    ball2 = Circle(Point(100,100), ballRadius)
    ball2.setFill(color_rgb(0, 0, 255))
    ball2V = [-15, -1]
    ball3 = Circle(Point(400,100), ballRadius)
    ball3.setFill(color_rgb(0, 255, 0))
    ball3V = [-25, 10]
    ball4 = Circle(Point(50,30), ballRadius)
    ball4.setFill(color_rgb(255, 0, 0))
    ball4V = [-5, 20]
    ball5 = Circle(Point(300,600), ballRadius)
    ball5.setFill(color_rgb(255, 255, 0))
    ball5V = [5, -15]
    balls = [ball1, ball2, ball3, ball4, ball5]
    velocities = [ball1V, ball2V, ball3V, ball4V, ball5V]

    border = Rectangle(Point(1,1), Point(479, 639))
    border.draw(win)

    for ball in balls:
        ball.draw(win)

    changed = False
    while(True):
        changed = False

        for i in range(0, len(balls)):
            location = balls[i].getCenter()

            if location.x >= 480 - ballRadius:
                velocities[i][0] = -abs(velocities[i][0])
                changed = True
            elif location.x <= ballRadius:
                velocities[i][0] = abs(velocities[i][0])
                changed = True

            if location.y >= 640 - ballRadius:
                velocities[i][1] = -abs(velocities[i][1])
                changed = True
            elif location.y <= ballRadius:
                velocities[i][1] = abs(velocities[i][1])
                changed = True

            for j in range(i + 1, len(balls)):
                ball2Loct = balls[j].getCenter()
                if math.sqrt((ball2Loct.x - location.x)**2 + (ball2Loct.y - location.y)**2) <= (2 * ballRadius):
                    temp = velocities[i][0]
                    velocities[i][0] = velocities[j][0]
                    velocities[j][0] = temp
                    temp = velocities[i][1]
                    velocities[i][1] = velocities[j][1]
                    velocities[j][1] = temp

        for i in range(0, len(balls)):
            balls[i].move(velocities[i][0], velocities[i][1])

        update(30)
    #win.getMouse() # Pause to view result
    win.close()    # Close window when done

main()