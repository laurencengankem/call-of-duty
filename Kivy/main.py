import time

import kivy
from client import Client
from kivy.animation import Animation
from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.screenmanager import ScreenManager, Screen
import json
import socket
from scraper import Scrap


from progress import NewProgressBar

nome: str = ''
source: str= ''
Followers: str= ''
Followings: str= ''
Posts: str= ''




class MainWindow(Screen):
    pass

class SecondWindow(Screen):

    def on_enter(self):
        self.anim()
        Clock.schedule_once(self.switch_back,5)

    def switch_back(self, *args):
        self.manager.current = "first"

    def anim(self):
        an= Animation(opacity=1, duration=4)
        an.start(self.ids.fond)

class ThirdWindow(Screen):
    def on_enter(self):
        dropdown= DropDown()
        width=self.ids.box.width/5
        self.ids.tt.text= "Results for "+ nome +' :'
        self.ids.pp.source = source
        self.ids.followers.text= Followers
        self.ids.followings.text= Followings
        self.ids.posts.text= Posts
        btn1= SmoothButton(back_color="#D3D3D3",border_radius=[0],for_color="#000000",color=(0,0,0,1),
                           text='Posts',size_hint=(None, None),height=50,width=width)
        btn1.bind(on_release=lambda btn1: dropdown.select(btn1.text))
        dropdown.add_widget(btn1)
        btn2= SmoothButton(back_color="#D3D3D3", border_radius=[0],for_color="#000000",color=(0,0,0,1),
                            text='Hashtags', size_hint=(None, None),height=50,width=width)
        btn2.bind(on_release=lambda btn2: dropdown.select(btn2.text))
        dropdown.add_widget(btn2)
        btn3= SmoothButton(back_color="#D3D3D3", border_radius=[0], for_color="#000000", color=(0, 0, 0, 1),
                            text='Time statistics', size_hint=(None, None),height=50,width=width)
        btn3.bind(on_release=lambda btn3: dropdown.select(btn3.text))
        dropdown.add_widget(btn3)
        btn4 = SmoothButton(back_color="#D3D3D3", border_radius=[0], for_color="#000000", color=(0, 0, 0, 1),
                            text='Locations', size_hint=(None, None),height=50,width=width)
        btn4.bind(on_release=lambda btn4: dropdown.select(btn4.text))
        dropdown.add_widget(btn4)
        self.ids.menu.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(self.ids.menu, 'text', x))



class WindowManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def search(self,input):
        c= Client()
        info=c.req(input).split(",")
        global nome
        global Followers
        global Followings
        global Posts
        global source
        nome = input
        Followers = info[0]
        Followings = info[1]
        Posts = info[2]
        source = info[3]





class SmoothButton(Button):
    pass

kv=Builder.load_file("mymain.kv")



class MyMainApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pb = NewProgressBar()
        pb.min = 0
        pb.max = 100
        pb.bar_value = 0
        pb.background_color = "#FFFFFF"
        pb.border_color = "#8E1600"
        pb.color("#8E1600")
        k = WindowManager()
        self.grid = SecondWindow()
        self.grid.ids.box.add_widget(pb)
        self.t = ThirdWindow()
        self.m= MainWindow()
        anim = Animation(bar_value=100, duration=4)
        anim.start(pb)
        k.add_widget(self.grid)
        k.add_widget(self.m)
        k.add_widget(self.t)
        self.manager= k


    def build(self):
        return  self.manager




if __name__== "__main__":
    MyMainApp.run((MyMainApp()))