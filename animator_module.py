import sprite_module
import collections

ANIM_FRAME_TIME = 1/12.
ANIM_FRAME_NUMBERS = 4

class FrameKeeper():
    def __init__(self):
        self.frame_number = collections.defaultdict(lambda : 0)
        self.frame_timer = collections.defaultdict(lambda : 0.)
        self.current_type = None
        self.max = 0

    def _increment_time(self, type, delta):
        self.frame_timer[type] += delta
        if self.frame_timer[type] > ANIM_FRAME_TIME:
            self.frame_timer[type] = 0
            self.frame_number[type] += 1
            self.frame_number[type] %= self.max

    def get_frame_number(self, type, delta):
        if type != self.current_type:
            self.wipe()
            self.current_type = type
        self._increment_time(type, delta)
        return self.frame_number[type]

    def wipe(self):
        self.frame_number = collections.defaultdict(lambda : 0)
        self.frame_timer = collections.defaultdict(lambda : 0.)

class UnitAnimator:
    def __init__(self, sprite):
        self.sprite = sprite
        self.frame_keeper = FrameKeeper()


    def animate(self, position, vector, canvas, delta, unit):
        current_order = unit.order_list

        if current_order == []:
            prefix = "Idle"
        else:
            raise Exception("Unable to animate unit order")

        if vector[0] > 0:
            suffix = "_R"
        else:
            suffix = "_L"

        self.sprite._draw(position, canvas, delta, prefix + suffix, self.frame_keeper)
        pass
