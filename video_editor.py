import pyglet
from video_objects import AnimatedText
from parser import parse_text

window = pyglet.window.Window(width=1920, height=1080)
classes = parse_text("video_timestamps.txt")


def update(dt):
    for py_class in classes:
        py_class.update(dt)


@window.event
def on_draw():
    window.clear()
    for py_class in classes:
        py_class.draw()


pyglet.clock.schedule_interval(update, 1 / 60.0)
pyglet.app.run()
