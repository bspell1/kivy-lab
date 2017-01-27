#!/usr/bin/env python3

from kivy.app import App
from kivy.uix.gridlayout import GridLayout


class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)


class Main(App):

    def __init__(self, **kwargs):
        super(Main, self).__init__(**kwargs)

    def build(self):
        screen = LoginScreen()
        return screen


if __name__ == '__main__':
    Main().run()
