from kivy.app import App
from kivy.animation import Animation

class MainApp(App):
    title = "Sustainable Development Goals"

    def animate_ball(self, widget, *args):
        anim = Animation(top_hint=.3, duration=2, t='out_elastic') # change here for top_hint=1 and ball duration=0.2 
        anim.bind(on_progress=self.my_progress_callback)
        anim.bind(on_complete=self.animate_way_back)
        anim.start(widget)

    def my_progress_callback(self, *args):
        progress = args[2]
        print(progress)

    def animate_way_back(self, *args):
        progress = args[0]
        print(progress)

if __name__ == '__main__':
    MainApp().run()