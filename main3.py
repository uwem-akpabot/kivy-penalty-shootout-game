from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector

class GameBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    # latest position of ball = curr velocity + curr position
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

class GameWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas:
            # load and draw images unto the canvas
            self.field = Rectangle(source="media/field.jpg", pos=(0, 0), size=(800, 800))
            self.ball = Rectangle(source="media/ball.png", pos=(376, 20), size=(40, 40))
            self.player = Rectangle(source="media/goalkeeper.png", pos=(348, 258))
            # self.goalpost = Rectangle(source="media/goalpost.png", pos=(277, 460), size=(250, 120))

        # play sound
        self.background_music = SoundLoader.load('media/background_music.mp3')
        self.background_music.play() 

        # Clock.schedule_interval(self.move_step, 0)

    def on_touch_down(self, touch):
        currentx = self.player.pos[0]
        currenty = self.player.pos[1]
        self.player.pos = (currentx, currenty)
        
        if touch.x > 365 and touch.x < 420 and touch.y > 20 and touch.y < 70: 
            print("In")

    def on_touch_up(self, touch):
        pass
        # print("Out")

    ball = ObjectProperty(None)
    player = ObjectProperty(None)

    def serve_ball(self):
        self.ball.velocity = Vector(4, 0).rotate(int(0, 360))
    # moving the ball by calling the move function
    def update(self, dt):
        # self.ball.move()

        self.ball.velocity += -1

class GameApp(App):
    def build(self):
        game = GameWidget()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return GameWidget()

if __name__ == '__main__':
    GameApp().run()


# on_touch_down() - when a finger/mouse touches the screen
# on_touch_up() - when we lift the finger/mouse off the screen after it touching it
# on_touch_move() - when we drag our finger/mouse on the screen

# def move_step(self, dt):
    # currentx = self.player.pos[0]
    # currenty = self.player.pos[1]

    # step_size = 200 * dt

    # if "w" in self.keysPressed:
    #     currenty += step_size
    # if "s" in self.keysPressed:
    #     currenty -= step_size
    # if "a" in self.keysPressed:
    #     currentx -= step_size
    # if "d" in self.keysPressed:
    #     currentx += step_size

    # self.player.pos = (currentx, currenty)