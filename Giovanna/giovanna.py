
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.expansionpanel import MDExpansionPanel
from kivymd.uix.list import OneLineIconListItem, MDList
import time
from kivy.animation import Animation
from test_nav import FoodItem


class ContentNavigationDrawer(BoxLayout):
    pass


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color



class GiovannaApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)




if __name__ == "__main__":
    GiovannaApp().run()
