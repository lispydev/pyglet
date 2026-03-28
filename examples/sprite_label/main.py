"""
Label scaling stress test

Creates 1k Labels, then quits or display a framerate
"""


import pyglet as pg
from pyglet import graphics
from pyglet.text import Label as PygletLabel

from sprite_label import SpriteLabel

# if True, will keep the window open to measure fps
# if False, will close as soon as all the labels are done creating
measure_fps = True

# which type of Label to use
# options: pyglet, sprite
label_type = "sprite"

n = 1000

win = pg.window.Window()

batch = graphics.Batch()

# create labels
labels = []
match label_type:
    case "pyglet":
        for i in range(n):
            label = PygletLabel("text", batch=batch)
            label.x = 100 + i
            label.y = 30
            labels.append(label)
    case "sprite":
        for i in range(n):
            label = SpriteLabel("text", batch=batch)
            label.place(100 + i, 30)
            labels.append(label)


# fps average
frame_counter = 0
frame_time = 0

fps_counter = PygletLabel("fps: ", batch=batch)

def update(dt):
    global frame_time
    global frame_counter
    if dt != 0:  # the first call always has dt = 0
        frame_time += dt
        frame_counter += 1
        framerate = frame_counter / frame_time
        fps_counter.text = f"fps: {framerate}"

if measure_fps:
    pg.clock.schedule(update)
else:
    # close right after loading
    pg.clock.schedule_once(lambda dt: win.close(), 0)

@win.event
def on_draw():
    win.clear()
    batch.draw()

pg.app.run()
