from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy.clock import Clock

# on_touch_down() - when a finger/mouse touches the screen
# on_touch_up() - when we lift the finger/mouse off the screen after it touching it
# on_touch_move() - when we drag our finger/mouse on the screen

class GameWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._on_keyboard_closed, self)
        self._keyboard.bind(on_key_down = self._on_key_down)
        self._keyboard.bind(on_key_up = self._on_key_up)

        with self.canvas:
            # load and draw images unto the canvas
            self.field = Rectangle(source="media/field.jpg", pos=(0, 0), size=(800, 800))
            self.ball = Rectangle(source="media/ball.png", pos=(376, 20), size=(40, 40))
            self.player = Rectangle(source="media/goalkeeper.png", pos=(348, 258))
            # self.goalpost = Rectangle(source="media/goalpost.png", pos=(277, 460), size=(250, 120))

        # play sound
        self.background_music = SoundLoader.load('media/background_music.mp3')
        self.background_music.play() 

        # keyboard events
        self.keysPressed = set()

        Clock.schedule_interval(self.move_step, 0)

    def on_touch_down(self, touch):
        # print(touch.x)
        currentx = self.player.pos[0]
        currenty = self.player.pos[1]
        self.player.pos = (currentx, currenty)

        # if touch.x > 365 and touch.x < 420: 
        if touch.x > 365 and touch.x < 420 and touch.y > 20 and touch.y < 70: 
            print("In")
            self.player.move()

        # print(self.player.pos[0]) #348
        # print(self.player.pos[1]) #258.0
        # what to do when the screen is touched
        # where is the touching allowed

    def on_touch_up(self, touch):
        pass
        # print("Out")

    def _on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down = self._on_key_down)
        self._keyboard.unbind(on_key_up = self._on_key_up)
        self._keyboard = None

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        self.keysPressed.add(text)

    def _on_key_up(self, keyboard, keycode):
        text = keycode[1]

        if text in self.keysPressed:
            self.keysPressed.remove(text)

    def move_step(self, dt):
        currentx = self.player.pos[0]
        currenty = self.player.pos[1]

        step_size = 200 * dt

        if "w" in self.keysPressed:
            currenty += step_size
        if "s" in self.keysPressed:
            currenty -= step_size
        if "a" in self.keysPressed:
            currentx -= step_size
        if "d" in self.keysPressed:
            currentx += step_size

        self.player.pos = (currentx, currenty)

class MobileGameApp(App):
    def build(self):
        return GameWidget()

if __name__ == '__main__':
    MobileGameApp().run()

