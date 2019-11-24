import json
import urllib


from kivy.animation import Animation
from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.screenmanager import ScreenManager, Screen
from progress import NewProgressBar
import endpoint

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
        Clock.schedule_once(self.switch_back,7)

    def switch_back(self, *args):
        self.manager.current = "first"

    def anim(self):
        an= Animation(opacity=1, duration=3)
        an.start(self.ids.fond)

class ThirdWindow(Screen):
    def on_enter(self):
        self.ids.tt.text= "Results for "+ nome +' :'
        self.ids.pp.source = source
        self.ids.followers.text= Followers
        self.ids.followings.text= Followings
        self.ids.posts.text= Posts




class WindowManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pb = NewProgressBar()
        pb.min = 0
        pb.max = 100
        pb.bar_value = 0
        pb.background_color = "#FFFFFF"
        pb.border_color = "#293149"
        pb.color("#293149")
        pb.opacity = 0
        self.grid = SecondWindow()
        self.grid.ids.box.add_widget(pb)
        self.t = ThirdWindow()
        self.m = MainWindow()
        anim = Animation(bar_value=100, duration=3)
        anim &= Animation(opacity=1, duration=3)
        anim.start(pb)
        self.add_widget(self.grid)
        self.add_widget(self.m)
        self.add_widget(self.t)


    def search(self,input):
        profile=input
        if input != '':
            profile.replace(" ", "")
            urli = endpoint.request_account_info(profile)
            data = {}
            with urllib.request.urlopen(urli) as url:
                data = json.loads(url.read().decode())
            global nome
            global Followers
            global Followings
            global Posts
            global source
            nome = input
            Followers = str(data['graphql']['user']['edge_followed_by']['count'])
            Followings = str(data['graphql']['user']['edge_follow']['count'])
            Posts = str(data['graphql']['user']['edge_owner_to_timeline_media']['count'])
            source = data['graphql']['user']['profile_pic_url']
            self.current = "third"





class SmoothButton(Button):
    pass
