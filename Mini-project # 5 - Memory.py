# implementation of card game - Memory

import simplegui
import random

list1 = range(0, 8)
list2 = range(0, 8)
deck_list = list1 + list2
deck_size = [50, 100]
pos = [0, 70]
exposed = []
counter = 0
first_card_index = 0
second_card_index = 0

# helper function to initialize globals
def new_game():
    global state, exposed, counter
    state = 0
    exposed = []
    counter = 0
    random.shuffle(deck_list)
    for i in range(len(deck_list)):
        exposed.append(False)   
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, first_card_index, second_card_index, counter
    index = pos[0] // 50
    if state == 0:
        if exposed[index] == False:
            exposed[index] = True
            state = 1
            first_card_index = index
            counter += 1
    elif state == 1:
        if exposed[index] == False:
            exposed[index] = True
            state = 2
            second_card_index = index
    elif state == 2:
        if deck_list[first_card_index] != deck_list[second_card_index]:
            exposed[first_card_index] = False
            exposed[second_card_index] = False  
        if exposed[index] == False:
            exposed[index] = True
            first_card_index = index
            state = 1
            counter += 1
                
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global pos, exposed
    pos = [15, 70]
    for i in range(len(deck_list)):
        if exposed[i] == False:
            canvas.draw_line((pos[0] + 10, 0), (pos[0] + 10, 100), 49, "Green")
        else:
            canvas.draw_text(str(deck_list[i]), pos, 50, "White")
        pos[0] += 50
    label.set_text("Turns = " + str(counter))

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric