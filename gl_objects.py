import pyglet
from pyglet.gl import *

window = pyglet.window.Window(1920, 1080)

vertex_list = pyglet.graphics.vertex_list(
    3,
    ('v2i', (500, 500, 1000, 500, 750, 1000)),
    ('c3B', (0, 0, 255, 0, 255, 0, 255, 0, 0)),
)


@window.event
def on_draw():
    window.clear()

    vertex_list.draw(GL_TRIANGLES)


def update(dt):
    pass


pyglet.clock.schedule_interval(update, 1 / 60)
pyglet.app.run()
