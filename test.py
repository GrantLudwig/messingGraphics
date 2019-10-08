from graphics import *
import time

def main():
    win = GraphWin("My Circle", 480, 640)
    c = Circle(Point(250,250), 10)
    c.setFill(color_rgb(130, 0, 130))
    c.draw(win)
    while(True):
        c.move(10, 0)
        update(90)
    #win.getMouse() # Pause to view result
    win.close()    # Close window when done

main()