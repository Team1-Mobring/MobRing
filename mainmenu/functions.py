import Timer

origin_netherlands_active =  False
origin_colombia_active = False
selected_dice = ""
x = 0

# Timer Functions
def fillZero(time):
    if len(str(time)) < 2:
        time = "0" + str(time)
    return time

def convertSeconds(s):
    s = s / 1000
    minutes = s // 60
    seconds = s % 60
    return str(fillZero(minutes))+":"+str(fillZero(seconds))


# Draws sexy text
def drawText(word, x, y):
    fill(255)
    #textFont(font)
    text(word, x, y)
    textAlign(CENTER)
    
def drawText2(word, x, y, r, g, b):
    textSize(48)
    #textFont(font)
    fill(r, g, b)
    text(word, x, y)
    textAlign(CENTER)

# function to attack with dices
def roll():
    white_dice = int(random(1,6))
    red_dice = int(random(1,6))
    fill(87, 99, 211)
    textSize(20)
    text(white_dice, 100, 100)
    text(red_dice, 100, 200)
    
# function part two of attack reroll(with origin effects)
def reroll():
    if origin_netherlands_active == True:
        fill(87, 99, 211)
        textSize(20)
        text(white_dice, 100, 100)
        text(red_dice, 100, 200)
    elif origin_colombia_active == True:
        if selected_dice == "white":
                fill(87, 99, 211)
                textSize(20)
                text(dice.white_dice, 100, 100)
        else:
                fill(87, 99, 211)
                textSize(20)
                text(red_dice, 100, 200)
    else:
        text(red_dice, 100, 200)

            
# buttons in the bot tutorial menu
def main_menu():
    global main_menu_x, box_x, box_y, box_width, box_height
    box_x = main_menu_x
        
        
def fed():
    global fed_x, box_x, box_y, box_width, box_height
    box_x = fed_x
    

        
def maffia():
    global maffia_x, box_x, box_y, box_width, box_height
    box_x = maffia_x
    


        
def help():
    global help_x, box_x, box_y, box_width, box_height
    box_x = help_x
