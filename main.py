from kivy.app import App
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.clock import Clock
from datetime import datetime
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout

class ClockLayout(BoxLayout):
    time_prop = ObjectProperty(None)

class ClockApp(App):
    sw_second = 0
    sw_started = False

    def on_start(self):
        Clock.schedule_interval(self.update_time, 0)

    def update_time(self, nap):
        now = datetime.now()
        self.root.time_prop.text = now.strftime('[b]%I[/b]:%M:%S')
        if self.sw_started:
            self.sw_second += nap
        minutes, seconds = divmod(self.sw_second, 60)
        self.root.ids.stopwatch.text = (
                                        '%02d:%02d.[size=40]%02d[/size]'%
                                            (int(minutes), int(seconds), int(seconds*100 % 100)))

    def start_stop(self):
        self.root.ids.start_stop.text = ('Start' if self.sw_started else 'Stop')
        self.sw_started = not self.sw_started

    def reset(self):
        self.root.ids.start_stop.text = 'Start'
        self.sw_started = False
        self.sw_second = 0

if __name__ == "__main__":
    LabelBase.register(name = 'Roboto',
                        fn_regular = 'Roboto-Thin.ttf',
                        fn_bold= 'Roboto-Medium.ttf')
    
    #setting window Color
    Window.clearcolor = get_color_from_hex('#101216')
    ClockApp().run()
