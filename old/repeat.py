from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.animation import Animation

class RepeatApp(App):
    def build(self):
        game = RepeatWidget()
        return game

class RepeatWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        title = "Checl"

        with self.canvas:
            def animate_the_button(self, *kwargs):
                self.rect = Rectangle(source="media/ball.png", pos=(75,10), size=(10,50))
                self.canvas.add(self.rect)
                anim = Animation(pos=(75,700))
                anim.start(self.rect)
    
    
#     anim = Animation(pos=(75,700)) + Animation(pos=(75,10))
# anim.repeat = True
# anim.start(self.rect)

if __name__ == '__main__':
    RepeatApp().run()