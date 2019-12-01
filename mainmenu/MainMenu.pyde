import TutorialBot, functions, Generator, Timer, Handleiding

handleidingY = 360
tutorialY = 420
randomDeckGeneratorY = 480
timedGameplayY = 540
x = 200
w = 200
h = 50

current_page = "Main_Menu"
main_menu_load = False
tutorial_load = False
generator_load = False
timer_load = False
handleiding_load = False

def setup():
    fullScreen()
    #size(600, 700)
    global f
    f = createFont('arial',32)
    img = loadImage('mobringlogo2.0.jpg')
    image(img, 150, 100, 300, 200)
    img2 = loadImage('icons8-settings-100.png')
    image(img2, 550, 650, 50, 50)
    stroke(255)
    textFont(f, 28)
    
    # knop handleiding
    background(0)
    fill(255, 255, 255)
    rect(x, handleidingY, w, h)
    fill(0,)    
    text('Manual Course', 206, 395)    
    
    # knop tutorial
    fill(255, 255, 255)
    rect(x, tutorialY, w, h)
    fill(0)
    text('Tutorial', 206, 455)
        
    #Random deck generator
    fill(255, 255, 255)
    rect(x, randomDeckGeneratorY, w, h)
    fill(0)
    text('Random deck', 206, 515)
        
    #Timed gameplay 
    fill(255, 255, 255)
    rect(x, timedGameplayY, w, h)
    fill(0)
    text('Timed Gameplay', 205, 575)
    fill(0 ,100)

def draw():
    global current_page, tutorial_load, generator_load, timer_load, main_menu_load, handleiding_load

    if current_page == "Main_Menu":
        if main_menu_load == False:
            setup()
            main_menu_load = True
        else:
            img = loadImage('mobringlogo2.0.jpg')
            image(img, 150, 100, 300, 200)
            img2 = loadImage('icons8-settings-100.png')
            image(img2, 550, 650, 50, 50)
            
    if current_page == "Tutorial_Bot":
        if tutorial_load == False:
            TutorialBot.setup()
            tutorial_load = True
        else:
            TutorialBot.draw()

    if current_page == "Random Deck Generator":
        if generator_load == False:
            Generator.setup()
            generator_load = True
        else:
            Generator.draw(f)
            
    if current_page == "Timer":
        if timer_load == False:
            Timer.setup()
            timer_load = True
        else:
            Timer.draw()
            
    if current_page == "Handleiding":
        if handleiding_load == False:
            Handleiding.setup()
            handleiding_load = True
        else:
            Handleiding.draw()
        
# Timer spatie registratie
def keyPressed():
    if current_page == "Timer" and timer_load == True:
        
        # "Spatie" functie in de timer
        if keyCode == 32 and Timer.timer_start == True:
            Timer.spatie = Timer.spatie + 1
            if Timer.running:
                Timer.running = not Timer.running
            
            if Timer.running_2:
                Timer.running_2 = not Timer.running_2
            
            if Timer.spatie % 2 == 0:
                # Even getal, gaat de eerste keer af.
                Timer.running = not Timer.running
                if Timer.four_timer: #Als de 4 minute timer aan staat.
                    Timer.time_left_2 += 15000
            else:
                # Oneven getal, gaat de tweede keer af.
                Timer.running_2 = not Timer.running_2
                if Timer.four_timer:
                    Timer.time_left += 15000
       
        # "Enter" functie tijdens het typen
        if keyCode == 10 and Timer.typing == True and Timer.step_count < 2:
            Timer.step_count += 1
           
            
        if Timer.step_count == 0:
            if keyCode == 8:
                Timer.user_input_1 = Timer.user_input_1 [0:-1]
            # De naam mag 10 characters lang zijn.
            elif len(Timer.user_input_1) <= 10:
                Timer.user_input_1 += key
        
        if Timer.step_count == 1:
            if keyCode == 8:
                Timer.user_input_2 = Timer.user_input_2 [0:-1]
            # De naam mag 10 characters lang zijn.
            elif len(Timer.user_input_2) <= 10:
                Timer.user_input_2 += key
            
        # "Enter" functie in de timer /is tijdelijk.
        if keyCode == 10 and Timer.step_count == 2:
            Timer.timer_start = not Timer.timer_start
            Timer.running = True


    # TO exit the program!.
    if keyCode == 27:
        exit()
    
                    
# mouseclcik registrater    
def mousePressed():
    global box_width, box_height, box_x, box_y, current_page, main_menu_load, tutorial_load, \
    timer_load
    def isMouseWithinSpace(x, y, w, h):
        if x < mouseX < x + w and y < mouseY < y + h:
            return True
        else:
            return False
        
    if current_page == "Tutorial_Bot" and tutorial_load == True:
        # box clicker
 
        if isMouseWithinSpace(TutorialBot.main_menu_x, TutorialBot.box_y, TutorialBot.box_width, TutorialBot.box_height):
            current_page = "Main_Menu"
            main_menu_load = False
            tutorial_load = False
        elif isMouseWithinSpace(TutorialBot.fed_x, TutorialBot.box_y, TutorialBot.box_width, TutorialBot.box_height):
            background(140,200,180)
            print("click2")
        elif isMouseWithinSpace(TutorialBot.maffia_x, TutorialBot.box_y, TutorialBot.box_width, TutorialBot.box_height):
            background(140,200,180)
            print("click3")
        elif isMouseWithinSpace(TutorialBot.help_x, TutorialBot.box_y, TutorialBot.box_width, TutorialBot.box_height):
            background(140,200,180)
            print("click4")
        else:
            print("wrong!")

    if current_page == "Timer" and timer_load == True:     
        # Home menu button
        if isMouseWithinSpace(100, 100, 200, 100):
            current_page = "Main_Menu"
            main_menu_load = False
            timer_load = False
        
        # 10 minute timer button
        if isMouseWithinSpace(630, 765, 200, 100) and Timer.step_count == 2:
            Timer.time_left = 300000
            Timer.time_left_2 = 300000
            Timer.timer_start = False
            Timer.four_timer = False
            Timer.time_mode_choosen = 1
    
        
        # 20 minute timer button
        if isMouseWithinSpace(1090, 765, 200, 100) and Timer.step_count == 2:
            Timer.time_left = 6000
            Timer.time_left_2 = 6000
            Timer.timer_start = False
            Timer.four_timer = False
            Timer.time_mode_choosen = 1
            
        # 4 minute timer button
        if isMouseWithinSpace(860, 765, 200, 100) and Timer.step_count == 2:
            Timer.time_left = 120000
            Timer.time_left_2 = 120000
            Timer.timer_start = False
            Timer.four_timer = True   
            Timer.time_mode_choosen = 1 
            
        # Reset score button
        if isMouseWithinSpace(910, 300, 100, 100) and Timer.step_count == 2:
            Timer.score_player_1 = 0
            Timer.score_player_2 = 0        
            
    if current_page == "Main_Menu" and main_menu_load == True:
            #mouse    
        if ((x < mouseX < 400) and ( 360 <= mouseY <= 410)):
            rect(x, handleidingY, w, h) and fill(0, 100)
            current_page = "Handleiding"
            
        if ((x < mouseX < 400) and ( 420 <= mouseY <= 460)):
            rect(x, tutorialY, w, h) and fill(0, 100)
            current_page = "Tutorial_Bot"  #Current page veranderd.
      
        
        if ((x < mouseX < 400) and ( 480 <= mouseY <= 530)):
            rect(x, randomDeckGeneratorY, w, h) and fill(0, 100)
            current_page = "Random Deck Generator"
            
        if ((x < mouseX < 400) and ( 540 <= mouseY <= 590)):
            rect(x, timedGameplayY, w, h) and fill(0, 100)
            current_page = "Timer"
