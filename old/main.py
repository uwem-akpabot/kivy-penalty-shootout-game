from kivy.app import App
from kivy.graphics import Rectangle
from kivy.animation import Animation

class MainApp(App):
    title = "Sustainable Development Goals"

    def animate_ball(self, widget, *args):
        anim = Animation(top_hint=.3, duration=2, t='out_elastic') # change here for top_hint=1 and ball duration=0.2 
        anim.bind(on_progress=self.my_progress_callback)
        anim.start(widget)

    def my_progress_callback(self, *args):
        progress = args[2]
        print(progress)

    # def animate_the_button(self, *kwargs):
    #     self.rect = Rectangle(pos=(75,10), size=(10,50))
    #     self.canvas.add(self.rect)
    #     anim = Animation(pos=(75,700))
    #     anim.start(self.rect)

if __name__ == '__main__':
    MainApp().run()