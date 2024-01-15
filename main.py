
import time
from kivy.core.audio import SoundLoader
#from kivy.core.video import Video
from kivy.properties import BooleanProperty, Clock
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

import random

Builder.load_file('design.kv')

global soundenable
soundenable = "True"


class MyScreen(Screen):
    button_disabled = BooleanProperty(False)

    def play(self):

        self.button_disabled = True
        diceface = random.choice(["dice_1.png", "dice_2.png", "dice_3.png", "dice_4.png",
                                 "dice_5.png", "dice_6.png"])
        filename = "assets/" + diceface
        self.ids.dice_state.source = filename
        self.button_disabled = False

    def on_switch_active(self, widget):
        updateglobal(str(widget.active))



class MainApp(MDApp):
    def __init__(self):
        super().__init__()
        self.init_audio()
        self.sound_music1.play()
        Clock.schedule_interval(self.update, 10)

    def build(self):
        return RootWidget()

    def init_audio(self):
        self.sound_music1 = SoundLoader.load("audio/neon.mp3")
        self.sound_music1.volume = 0.05


    def update(self, dt):
        if soundenable == "True":
            self.sound_music1.play()




def updateglobal(b):
    global soundenable
    soundenable = b



class RootWidget(ScreenManager):
    pass

if __name__ == "__main__":
    MainApp().run()



