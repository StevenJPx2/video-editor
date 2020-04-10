import pyglet
import math
from video_objects import AnimatedText

window = pyglet.window.Window(width=1920, height=1080)

label = AnimatedText(
    "Hello, world",
    font_name="Avenir Next",
    font_size=36,
    x=window.width // 2,
    y=1,
    stop_value=window.height // 2,
    anchor_x="center",
    anchor_y="center",
    duration=10,
    style="ease_in_out_sine",
)


def update(dt):
    label.y += label.update(dt, label.y)


@window.event
def on_draw():
    window.clear()
    label.draw()


pyglet.clock.schedule_interval(update, 1 / 60.0)
pyglet.app.run()
