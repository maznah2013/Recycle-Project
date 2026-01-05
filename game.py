import pgzrun
import random 

WIDTH=800
HEIGHT=600
TITLE="Sustainability Project"
CENTER_X=WIDTH/2
CENTER_Y=HEIGHT/2
CENTER=(CENTER_X, CENTER_Y)
FINAL_LEVEL=6
START_SPEED=10
ITEMS=["bag", "battery", "bottle", "chips"]

game_over=False
game_completed=False
current_level=1
items=[]
animations=[]

def draw():
    screen.clear()
    screen.blit("bg", (0,0))

def update():
    pass

def get_options(extra_items):
    items_to_create=["paper"]
    for i in range(extra_items):
        random_item=random.choice(ITEMS)
        items_to_create.append(random_item)
    return items_to_create

def create_items(items_to_create):
    new_items=[]
    for option in items_to_create:
        item=Actor(option+"img")
        new_items.append(item)
    return new_items

def layout_items(items_to_layout):
    number_of_gaps=len(items_to_layout)+1
    gap_size=WIDTH/number_of_gaps
    random.shuffle(items_to_layout)
    for index, item in enumerate(items_to_layout):
        new_xpos=(index+1)*gap_size
        item.x=new_xpos

def animate_items(items_to_animate):
    global animations
    for item in items_to_animate:
        duration=START_SPEED-current_level
        item.anchor=("center", "bottom")
        animation=animate(item, duration=duration, on_finished=handle_gameover, y=HEIGHT)
        animations.append(animation)

def handle_gameover():
    global game_over
    game_over=True

def on_mouse_down(pos):
    global current_level, items
    for item in items:
        if item.collidepoint(pos):
            if "paper" in item.image:
                handle_game_complete()
            else:
                handle_gameover()

def handle_game_complete():
    global current_level, FINAL_LEVEL, items, animation, game_completed
    stop_animations(animations)
    if current_level==FINAL_LEVEL:
        game_completed=True
    else:
        current_level +=1
        items=[]
        animations=[]

def stop_animations(animations_to_stop):
    for animation in animations_to_stop:
        if animation.running:
            animation.stop()

def display_msg(maintext, subtext):
    screen.draw.text(maintext, fontsize=60, center=CENTER, color="black")
    screen.draw.text(subtext, fontsize=30, center=(CENTER_X, CENTER_Y+30), color="black")


pgzrun.go()
