# template for "Stopwatch: The Game"

import simplegui

# define global variables
height = 200
width = 300
interval = 100
counter = 0
success_stops = 0
total_stops = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(tenths_of_seconds):
    minutes = tenths_of_seconds // 600
    seconds = tenths_of_seconds // 10 % 60
    if seconds < 10:
       seconds = "0" + str(seconds)
    tenths = tenths_of_seconds % 10
    return str(minutes) + ":" + str(seconds) + "." + str(tenths)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global timer_is_running
    timer.start()
    
def stop():
    global success_stops, total_stops, timer_is_running
    if timer.is_running():
        total_stops += 1
        if counter % 10 == 0:
            success_stops += 1
    timer.stop()

def reset():
    global counter, success_stops, total_stops
    counter = 0
    timer.stop()
    success_stops = 0
    total_stops = 0

# define event handler for timer with 0.1 sec interval

def timer_handler():
    global counter
    counter += 1

# define draw handler

def draw_handler(canvas):
    canvas.draw_text(format(counter), [100, 100], 24, "White")
    canvas.draw_text(str(success_stops) + "/" + str(total_stops), [270, 35], 18, "White")
    
# create frame
frame = simplegui.create_frame("Stopwatch", width, height)
timer = simplegui.create_timer(interval, timer_handler)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)

# register event handlers
frame.set_draw_handler(draw_handler)

# start frame
frame.start()


# Please remember to review the grading rubric
