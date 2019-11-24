from kivy.animation import Animation
from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.widget import Widget
from kivymd.theming import ThemeManager
from kivymd.uix.navigationdrawer import NavigationLayout
from windowmanager import WindowManager



class NavLayout(NavigationLayout):
    pass




class Application(App):
    theme_cls = ThemeManager()


if __name__== "__main__":
    Application.run((Application()))