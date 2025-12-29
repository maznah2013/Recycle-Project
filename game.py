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












pgzrun.go()
