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
def keyTyped():
    global timeStop
    if current_page == "Timer" and timer_load == True:
        if key == " ":
            Timer.timeStop = functions.isTimeStopped(Timer.timeStop)
            
# mouseclcik registrater    
def mousePressed():
    global box_width, box_height, box_x, box_y, current_page, main_menu_load, tutorial_load
    if current_page == "Tutorial_Bot" and tutorial_load == True:
        # box clicker
        def isMouseWithinSpace(x, y, w, h):
            if x < mouseX < x + w and y < mouseY < y + h:
                return True
            else:
                return False
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
    
