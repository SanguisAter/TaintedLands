import sprite_module

class UnitAnimator:
    def __init__(self, sprite_element):
        self.sprite_element = sprite_element
        self.loaded = False
        self.unit_sprite = None


    def animate(self, position, vector, canvas, delta, unit):
        print self.loaded
        current_order = unit.order_list

        if current_order == []:
            prefix = "Idle"
        else:
            raise Exception("Unable to animate unit order")

        if vector[0] > 0:
            suffix = "_R"
        else:
            suffix = "_L"

        self.unit_sprite._draw(position, canvas, delta, prefix + suffix)
        pass


    def load(self):
        sprite_element = self.sprite_element
        w = int(sprite_element["w"])
        h = int(sprite_element["h"])
        sx = int(sprite_element["sx"])
        sy = int(sprite_element["sy"])
        frame_size = (w,h)
        hook_point = (sx,sy)
        path = sprite_element["path"]
        self.unit_sprite = sprite_module.UnitSprite(path, frame_size, hook_point)
        self.loaded = True

