
import time, functions

def setup():
    global timeStop, counter, timeleft
    background(240)
    timeStop = True
    counter = 0
    timeleft = 90   #The input, variable to change
    
def draw():
    global counter
    background(240)
    
    if timeleft - counter > 0:
        if not timeStop:
            functions.drawText2((functions.convertSeconds(timeleft - counter)), 50, 80, 0)
            counter += 1
            time.sleep(1)
        
        if timeStop:
            functions.drawText2((functions.convertSeconds(timeleft - counter)), 50, 80, 0)
    else:
        functions.drawText2((functions.convertSeconds(timeleft - counter)), 50, 80, 0)


    
