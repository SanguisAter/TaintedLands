
import pygame
import sys
# each instance for in game unit type
# each have animations: idle x 2, move x 2, attack x 2, die x 1
import collections

ANIM_FRAME_TIME = 1/12.
ANIM_FRAME_NUMBERS = 4


def get_row(sprite, row_number, frame_size):
    Y = row_number * frame_size[1]
    ret = []
    image_width = sprite.get_rect().width
    for i in xrange(image_width / frame_size[0]):
        X = frame_size[0] * i
        rect = pygame.Rect((X,Y),frame_size)
        sprite.set_clip(rect)
        ret += [sprite.subsurface(sprite.get_clip())]
    return ret, image_width / frame_size[0]
    

class FrameAnimator():
    def __init__(self):
        self.frame_number = collections.defaultdict(lambda : 0)
        self.frame_timer = collections.defaultdict(lambda : 0.)
        self.max = 0

    def _increment_time(self, type, delta):
        self.frame_timer[type] += delta
        if self.frame_timer[type] > ANIM_FRAME_TIME:
            self.frame_timer[type] = 0
            self.frame_number[type] += 1
            self.frame_number[type] %= self.max

    def get_frame_number(self, type, delta):
        self._increment_time(type, delta)
        return self.frame_number[type]
        

class UnitSprite(pygame.sprite.Sprite):
    def __init__(self, sprite_path, frame_size, left_down_point):
        self.sheet = dict()
        self.frame_size = frame_size
        self.frames = FrameAnimator()
        self.read_sprite(sprite_path, frame_size)

    def read_sprite(self, sprite_path, frame_size):
        self.sprite= pygame.image.load(sprite_path)
        self.sheet["Idle_R"], number_of_frames = get_row(self.sprite, 0, frame_size)
        self.sheet["Idle_L"], number_of_frames = get_row(self.sprite, 1, frame_size)
        self.sheet["Move_R"], number_of_frames = get_row(self.sprite, 2, frame_size)
        self.frames.max = number_of_frames
        
    
    def _get_frame(self, name, delta):
        frame_number = self.frames.get_frame_number(name, delta)
        ret = self.sheet[name][frame_number]
        return ret
        
    def draw_idle(self, position, canvas, delta): 
        self._draw(position, canvas, delta, "Idle_R")

    def draw_move(self, position, canvas, delta):
        self._draw(position, canvas, delta, "Move_R")

    def _draw(self, position, canvas, delta, type):
        backdrop = pygame.Rect(position, self.frame_size)
        canvas.blit(self._get_frame(type, delta), backdrop)
        

