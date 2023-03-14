from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint
from kivy.core.audio import SoundLoader

class SdgGoalpost(Widget):
    score = NumericProperty(0)

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1, * vx, vy)
            vel = bounced * 1.1
            ball.velocity = vel.x, vel.y + offset
    
class SdgBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos # moves the ball

class SdgKeeper(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos # moves the keeper

class SdgField(Widget):
    pass

class SdgGame(Widget):
    # play sound
    background_music = SoundLoader.load('media/_music.mp3')
    background_music.play() 

    ball = ObjectProperty(None)
    keeper = ObjectProperty(None)

    def serve_ball(self):
        self.ball.center = self.center
        self.ball.velocity = Vector(8, 5)

    def serve_keeper(self):
        self.keeper.center = self.center
        # self.keeper.velocity = Vector(4, 0).rotate(randint(0, 360))
        self.keeper.velocity = Vector(5, 0) # Vector(speed, angle)

    def update(self, dt):
        self.ball.move()
        self.keeper.move()

        # bounce ball off top and bottom
        if (self.ball.y < 0) or (self.ball.top > self.height):
            self.ball.velocity_y *= -1
        
        # bounce ball off left and right
        if (self.ball.x < 0) or (self.ball.right > self.width):
            self.ball.velocity_x *= -1
    
        # bounce keeper off left and right
        if (self.keeper.x < 100) or (self.keeper.right > self.width - 100):
            self.keeper.velocity_x *= -1

    def on_touch_down(self, touch):
        if touch.x == self.width / 2:
            # self.ball.center_y = touch.y
            self.serve_ball()
    #     # if touch.x > self.width - self.width / 3:
    #     #     self.player2.center_y = touch.y

class SdgApp(App):
    def build(self):
        self.title = 'SDG Game'
        game = SdgGame()
        # game.serve_ball()
        game.serve_keeper()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game
    
if __name__ == '__main__':
    SdgApp().run()


# python sdg.py --size=360x740 --dpi=529
# python sdg.py --size=740x360 --dpi=529