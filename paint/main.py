#!/usr/bin/env python3

from random import random

from kivy.app import App
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.widget import Widget


class Screen(FloatLayout):

    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)


class PaintWidget(Widget):

    def __init__(self, **kwargs):
        super(PaintWidget, self).__init__(**kwargs)

        self.start_circle = None
        self.line = None

    def on_touch_down(self, touch):
        color = random(), 1, 1
        radius = random() * 40 + 10
        with self.canvas:
            Color(*color, mode='hsv')
            pos = touch.x - radius, touch.y - radius
            self.start_circle = Ellipse(pos=pos,
                                        size=(radius * 2, radius * 2))
            self.line = Line(points=[touch.x, touch.y],
                             width=radius / 2)

    def on_touch_move(self, touch):
        if self.line:
            self.line.points += [touch.x, touch.y]

    def on_touch_up(self, touch):
        if self.start_circle:
            with self.canvas:
                radius = self.start_circle.size[0] / 2
                pos = touch.x - radius, touch.y - radius
                Ellipse(pos=pos, size=(radius * 2, radius * 2))
            self.start_circle = None
            self.line = None


class MainApp(App):

    def __init__(self, **kwargs):
        super(MainApp, self).__init__(**kwargs)
        self.screen = None

    def build(self):
        self.screen = Screen()
        return self.screen

    def on_clear(self, *args):
        self.screen.painter.canvas.clear()


if __name__ == '__main__':
    MainApp().run()
