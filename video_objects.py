import pyglet
import animation_functions as af


class AnimatedText(pyglet.text.Label):
    def __init__(self, text, stop_value, *args, duration=0, style="linear", **kwargs):
        super().__init__(text, *args, **kwargs)
        self.text = text
        self.elapsed_time = 0
        self.velocity = 0.0
        self.start_value = None
        self.stop_value = stop_value
        self.duration = duration
        self.style = style
        self.animation_style_fn = self.sel_style(self.style)

    def sel_style(self, style):
        return eval(f"af.{style}")

    def update(self, dt, value):

        if self.start_value is None:
            self.start_value = value

        change_value = self.stop_value - value

        if change_value < 0:
            return 0

        self.elapsed_time += dt

        value = self.animation_style_fn(
            self.elapsed_time, self.start_value, change_value, self.duration
        )

        return value
