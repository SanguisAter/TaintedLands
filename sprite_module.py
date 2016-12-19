import pygame
import sys

import collections


# each instance for in game unit type
# each have animations: idle x 2, move x 2, attack x 2, die x 1

# this function retrieves 
def get_row(sprite, row_number, frame_size):
    Y = row_number * frame_size[1]
    ret = []
    image_width = sprite.get_rect().width
    for i in xrange(image_width / frame_size[0]):
        X = frame_size[0] * i
        rect = pygame.Rect((X,Y),frame_size)
        sprite.set_clip(rect)
        ret += [sprite.subsurface(sprite.get_clip())]
    if ret == []:
        raise Exception("loaded 0 frames")
    return ret, image_width / frame_size[0]
    


class UnitTypeSprite():
    def __init__(self, sprite_element):
        self.sheet = dict()
        self.load(sprite_element)


    def load(self, sprite_element):
        w = int(sprite_element["w"])
        h = int(sprite_element["h"])
        sx = int(sprite_element["sx"])
        sy = int(sprite_element["sy"])
        frame_size = (w,h)
        hook_point = (sx,sy)
        path = sprite_element["path"]
        self.frame_size = frame_size
        self.hook_point = hook_point
        self.read_sprite(path, frame_size)
        

    def read_sprite(self, sprite_path, frame_size):
        self.sprite= pygame.image.load(sprite_path)
        self.sheet["Idle_R"], number_of_frames = get_row(self.sprite, 0, frame_size)
        self.sheet["Idle_L"], number_of_frames = get_row(self.sprite, 1, frame_size)
        self.sheet["Move_R"], number_of_frames = get_row(self.sprite, 2, frame_size)
        self.max = number_of_frames

    def _get_frame(self, name, delta, frame_keeper):
        frame_keeper.max = self.max
        frame_number = frame_keeper.get_frame_number(name, delta)
        ret = self.sheet[name][frame_number]
        return ret

    # this drawes sprite
    # position on canvas, time from last frame, type of animation
    # UnitSprite -> (int,int) -> pygame.surface -> float -> string -> None
    def _draw(self, position, canvas, delta, type, frame_keeper):
        backdrop = pygame.Rect(position, self.frame_size)
        canvas.blit(self._get_frame(type, delta, frame_keeper), backdrop)

    # TODO when game object is complete then we will be able to draw anything
    # this only should blit to canvas. Drawing of a object should be
    # undependent on how game is implemented. This is a border post of iron
    # curtain for drawing module
    def draw(self, game_object, canvas):
        pass
