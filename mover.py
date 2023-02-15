from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.animation import Animation
from kivy.core.window import Window
from random import random
 
Builder.load_string('''
<Root>:
    ARect:
        pos: 500, 300
<ARect>:
    canvas:
        Color:
            rgba: 0, 0, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size
''')
 
class Root(Widget):
    pass
 
class ARect(Widget):
    def circle_pos(self):
        Animation.cancel_all(self)
        random_x = random() * (Window.width - self.width)
        random_y = random() * (Window.height - self.height)
 
        anim = Animation(x=random_x, y=random_y,
                         duration=4,
                         t='out_elastic')
        anim.start(self)
 
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.circle_pos()
 
runTouchApp(Root())