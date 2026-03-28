"""
Define a Label widget using glyph Sprites

This approach yields slightly faster initialization and draw times,
in exchange for not having all the features of the pyglet Label class
"""

import pyglet as pg
from pyglet.sprite import Sprite


# default font
font = pg.font.load()

class SpriteLabel:
    "Custom Label implemented from glyph sprites"
    def __init__(self, text: str, batch=None):
        self.x = 0
        self.y = 0

        self._text = text
        self.glyphs, self.positions = font.get_glyphs(text)

        self.sprites = []
        for glyph, pos in zip(self.glyphs, self.positions):
            self.sprites.append(Sprite(glyph, batch=batch))

        # initialize sprite positions
        self.place(self.x, self.y)


    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text: str):
        self._text = text
        self.glyphs, self.positions = font.get_glyphs(text)

    def place(self, x, y):
        self.x = x
        self.y = y
        w = 0
        # letters are aligned to the baseline
        # some letters, like g, go under the baseline
        # letter.baseline is the offset for these letters
        y_baseline = y + font.ascent - font.descent
        for glyph, position, sprite in zip(self.glyphs, self.positions, self.sprites):
            sprite.x = x + w + glyph.lsb
            sprite.y = y_baseline - glyph.baseline
            w += glyph.advance


        self.content_width = w
        self.content_height = font.ascent - font.descent # font height

    def draw(self):
        for sprite in self.sprites:
            sprite.draw()

