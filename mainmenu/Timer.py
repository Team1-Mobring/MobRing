
import time, functions

def setup():
    global running, time_left, last_millis, start_timer, time_left_2, \
            last_millis_2, running_2, spatie, timer_start, user_input_1, user_input_2, \
            step_count, typing, four_timer
    background(240)
    
    rect(100, 200, 100, 200)
    
    four_timer = False
    
    typing = True
    step_count = 0
    
    user_input_1 = ''
    user_input_2 = ''
    
    spatie = 1
    timer_start = False
    
    time_left = 0 * 1000
    added_time = 0
    last_millis = millis()
    running = False
    
    time_left_2 = time_left
    last_millis_2 = millis()
    running_2 = False
    

def draw():

    global time_left, last_millis, running, start_timer, time_left_2, last_millis_2, \
            running_2, timer_start, user_input_1, user_input_2, step_count
    background(240)
    
    fill(23, 97, 97)
    rect(500, 300, 325, 100)
    rect(1090, 300, 325, 100)
    
    # Menu button
    fill(200)
    rect(100, 100, 200, 100)
    functions.drawText3("Main Menu", 200, 160, 0, 0, 0, 30)
    
    # Timer modes buttons
    fill(200)
    rect(860, 765, 200, 100) # 4 minutes
    rect(630, 765, 200, 100) # 10 minutes
    rect(1090, 765, 200, 100) # 20 minutes
    functions.drawText3("4 Mins + 15", 885, 830, 0, 0, 0, 30)
    functions.drawText3("10 Mins", 675, 830, 0, 0, 0, 30)
    functions.drawText3("20 Mins", 1135, 830, 0, 0, 0, 30)
    
    # User Input stuff   
    if step_count == 0:
        functions.drawText3("Please input the name of Player 1", 580, 200, 0, 0, 0, 48)
    elif step_count == 1:
        functions.drawText3("Please input the name of Player 2", 580, 200, 0, 0, 0, 48)
    elif step_count == 2:
        functions.drawText3("Pick a time mode!", 770, 200, 0, 0, 0, 48)

    # Draws the user name on the screen.
    functions.drawText3(user_input_1, 530, 365, 0, 0, 0, 48)
    functions.drawText3(user_input_2, 1120, 295, 0, 0, 0, 48)
    
    
    # Timer stuff
    if timer_start:
        if running:
            time_left = (time_left - (millis() - last_millis))
        else:
            pass    
        if running_2:
            time_left_2 = (time_left_2 - (millis() - last_millis_2))
        else:
            pass    
        #last_millis = millis()
        #last_millis_2 = millis()
        if time_left < 1000:
            running = False
            timer_start = False
    
        if time_left_2 < 1000:
            running_2 = False
            timer_start = False
        fill(0, 100, 0)
        rect(860, 610, 200, 100) # Pauze knop!
        functions.drawText3("Switch!", 910, 670, 0, 0, 0, 30)
        functions.drawText3("'Spacebar'", 910, 690, 0, 0, 0, 20)
        functions.drawText3("Press 'Enter' to pause", 860, 730, 0, 0, 0, 20)
            
    # Voor de pauze knop "Enter"       
    elif step_count == 2:
        fill(100, 0, 0)
        rect(860, 610, 200, 100) # Start knop! (Visueel)
        functions.drawText3("Start!", 910, 670, 0, 0, 0, 30)
        functions.drawText3("Press 'Enter' to start", 860, 730, 0, 0, 0, 20)
        
    last_millis = millis()
    last_millis_2 = millis()

    # For testing purposes
    functions.drawText2(functions.convertSeconds(time_left), width*0.37, height/2, 0, 0, 0, 48)
    functions.drawText2(functions.convertSeconds(time_left_2), width*0.6, height/2, 0, 0 ,0, 48)
