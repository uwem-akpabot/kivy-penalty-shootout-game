from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint

class CoreBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos # moves the ball

class CoreKeeper(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        pass
        # self.pos = Vector(*self.velocity) + self.pos # moves the keeper

class CoreField(Widget):
    pass

class CoreGame(Widget):
    ball = ObjectProperty(None)
    keeper = ObjectProperty(None)

    def serve_ball(self):
        self.ball.center = self.center
        self.ball.velocity = Vector(4, 0).rotate(randint(0, 360))

    def serve_keeper(self):
        self.keeper.center = self.center
        self.keeper.velocity = Vector(4, 0).rotate(randint(0, 360))

    def update(self, dt):
        self.ball.move()
        self.keeper.move()

        # bounce ball off top and bottom
        if (self.ball.y < 0) or (self.ball.top > self.height):
            self.ball.velocity_y *= -1
        
        # bounce ball off left and right
        if (self.ball.x < 0) or (self.ball.right > self.width):
            self.ball.velocity_x *= -1

        # bounce keeper off top and bottom
        if (self.keeper.y < 0) or (self.keeper.top > self.height):
            # self.keeper.velocity_y *= -1
            pass
        
        # bounce keeper off left and right
        if (self.keeper.x < 0) or (self.keeper.right > self.width):
            self.keeper.velocity_x *= -1

class CoreApp(App):
    def build(self):
        game = CoreGame()
        game.serve_ball()
        game.serve_keeper()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game
    
if __name__ == '__main__':
    CoreApp().run()