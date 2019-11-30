
import time, functions

def setup():
    global running, time_left, last_millis, start_timer
    background(240)
    
    time_left = 100 * 1000
    last_millis = millis()
    running = False

def draw():
    global time_left, last_millis, running
    background(240)
    
    if running:
        time_left = (time_left - (millis() - last_millis))
    else:
        pass
    last_millis = millis()
    
    if(time_left < 1000):
        running = False

    functions.drawText2(functions.convertSeconds(time_left), width*0.4, height/2, 0)
