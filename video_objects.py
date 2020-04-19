import pyglet
import animation_functions as af


class AnimatedObject:
    "Base object for animation"

    def __init__(self,
                 start_value=None,
                 stop_value=None,
                 duration=None,
                 style="linear",
                 staged_values=None,
                 del_time=None):

        self.elapsed_time = 0
        self.start_value = start_value
        self.stop_value = stop_value
        self.duration = duration
        self.animation_style_fn = self.sel_style(style)
        self.staged_values = staged_values
        self.stage_count = 0
        self.del_time = del_time

    @staticmethod
    def sel_style(style):
        return eval(f"af.{style}")

    def update(self, dt):
        self.elapsed_time += dt

        if self.del_time is not None and self.elapsed_time >= self.del_time:
            self.delete()

        if self.elapsed_time - self.start_value[
                self.stage_count] >= self.duration[self.stage_count]:
            if self.stage_count + 1 < len(self.start_value):
                self.stage_count += 1
            else:
                return

        if self.start_value[self.stage_count] > self.elapsed_time:
            for stage_prop in self.staged_values:
                try:
                    exec(
                        f"self.{stage_prop} = self.staged_values[stage_prop][self.stage_count]"
                    )
                except IndexError:
                    pass
            return

        for stage_prop in self.staged_values:
            try:
                b = self.staged_values[stage_prop][self.stage_count]
                c = self.staged_values[stage_prop][self.stage_count + 1] - b
                t = self.elapsed_time - self.start_value[self.stage_count]
                value = self.animation_style_fn(
                    t, b, c, self.duration[self.stage_count])

                exec(f"self.{stage_prop} = value")
            except IndexError:
                pass

    @staticmethod
    def delete():
        pass


class AnimatedText(pyglet.text.Label, AnimatedObject):
    def __init__(self,
                 *args,
                 stop_value=None,
                 start_value=None,
                 staged_values=None,
                 duration=0,
                 del_time=None,
                 style="linear",
                 **kwargs):
        pyglet.text.Label.__init__(self, *args, **kwargs)
        AnimatedObject.__init__(self, start_value, stop_value, duration, style,
                                staged_values, del_time)
