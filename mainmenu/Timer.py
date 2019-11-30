
import time, functions

def setup():
    global running, time_left, last_millis, start_timer, time_left_2, last_millis_2, running_2, spatie, timer_start
    background(240)
    
    spatie = 1
    timer_start = False
    
    time_left = 5 * 1000
    last_millis = millis()
    running = False
    
    time_left_2 = time_left
    last_millis_2 = millis()
    running_2 = False

def draw():
    global time_left, last_millis, running, start_timer, time_left_2, last_millis_2, running_2, timer_start
    background(240)
    
    if running:
        time_left = (time_left - (millis() - last_millis))
    else:
        pass
        
    if running_2:
        time_left_2 = (time_left_2 - (millis() - last_millis_2))
    else:
        pass    
    
    last_millis = millis()
    last_millis_2 = millis()
    
    if time_left < 1000:
        running = False
        timer_start = False
        functions.drawText2(functions.convertSeconds(time_left), width*0.4, height/2, 220, 0, 0)
        functions.drawText2(functions.convertSeconds(time_left_2), width*0.6, height/2, 0, 0 ,0)
    
    if time_left_2 < 1000:
        running_2 = False
        timer_start = False
        
        functions.drawText2(functions.convertSeconds(time_left), width*0.4, height/2, 0, 0, 0)
        functions.drawText2(functions.convertSeconds(time_left_2), width*0.6, height/2, 220, 0 ,0)
        
    if timer_start:
        functions.drawText2(functions.convertSeconds(time_left), width*0.4, height/2, 0, 0, 0)
        functions.drawText2(functions.convertSeconds(time_left_2), width*0.6, height/2, 0, 0 ,0)
