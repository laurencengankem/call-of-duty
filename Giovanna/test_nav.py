
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.videoplayer import VideoPlayer
from kivymd.uix.bottomsheet import MDCustomBottomSheet
from kivymd.uix.card import MDSeparator
from kivymd.uix.list import MDList

Builder.load_string(
    """
#:import Window kivy.core.window.Window
#:import get_hex_from_color kivy.utils.get_hex_from_color


<BoxContentForBottomSheetCustomScreenList>
    orientation: "vertical"
    padding: dp(10)
    spacing: dp(10)
    size_hint_y: None
    height: self.minimum_height
    pos_hint: {"top": 1}

    ScrollView:

        GridLayout:
            size_hint_y: None
            height: self.minimum_height
            cols: 1
            orientation: 'vertical'
            row_default_height: self.parent.height*2
            padding: dp(20)
            
            
            BoxLayout:
                orientation:'vertical'
                id: box
                spacing: dp(20)
                Label:
                    size_hint_y: .01
                    id: ricetta
                    color: 70/255,130/255,180/255,1
                    font_size: self.width/12
                    
                MDSeparator:
                
<Subscribe>
    size_hint_y: .1
    orientation:'vertical'
    Button:
        background_normal: 'gold.jpg'
        text:'Subscribe to get access to the recipe \\n 0.99€/Month'
        halign:'center'
        color: 0.2,0,0,1
        font_size: self.width/18    
 
    
                    
            
<Ingredient>
    name:''
    quantity:''
    spacing: dp(20)
    size_hint_y: 0.01
    
    canvas:
        Color:
            rgb: 1,1,1
        Rectangle:
            pos:self.pos
            size: self.size  
        
    Label:      
        color: 0,0,0,1
        font_size: self.width/6
        text: root.name
    
    Label:
        color: 0,0,0,1
        font_size: self.width/6
        text: root.quantity
        
<VideoBox>
    size_hint_y: 0.05
    canvas:
        Color:
            rgb: 1,1,1
        Rectangle:
            pos:self.pos
            size: self.size  
    
    padding: dp(20)
    VideoPlayer:
        source: 'alex.mp4'
        image_overlay_play: 'marmelata.png'
       
        
    
        
<FoodItem>
    bg: 'bambini.jpg'
    size_hint_y: .2
    text: "love"
    callback: None
    canvas:
        Color:
            rgb: 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.width,self.height
            source: root.bg
    
    Button:
        size_hint_y:.2
        opacity: 0.6
        font_size: self.width/15
        text: root.text
        on_release: root.callback()
        
        

                
"""
)

recipe=''

class FoodItem(BoxLayout):

    def show_example_custom_bottom_sheet(
            self, text, corner=None, animation=True
    ):
        """Show menu from the screen BottomSheet."""
        global recipe
        recipe=text
        custom_screen_for_bottom_sheet = BoxContentForBottomSheetCustomScreenList()
        MDCustomBottomSheet(
            screen=custom_screen_for_bottom_sheet,
            bg_color=[1,1,1, .75],
            animation=animation,
            radius_from=corner,
        ).open()



class Subscribe(BoxLayout):
    pass

class Ingredient(BoxLayout):
    pass

class VideoBox(BoxLayout):
    pass


class BoxContentForBottomSheetCustomScreenList(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.ricetta.text=recipe


        if (recipe == 'marmelata'):
            self.ids.box.add_widget(Label(text='Ingredients', color=[0, 0, 0, 1], font_size=self.width / 4, size_hint_y=0.01))
            lista={'Eggs':'2','Milk':'200ml','Apple':'200g'}
            self.list(lista)
            self.ids.box.add_widget(MDSeparator())
            self.ids.box.add_widget(Label(text='Preparation', color=[0, 0, 0, 1], font_size=self.width / 4, size_hint_y=0.01))
            self.ids.box.add_widget(VideoBox())

        if(recipe=='pudino'):
            self.ids.box.add_widget(Subscribe())
            self.ids.box.add_widget(Label(text='0.99/Month',valign='top'))

    def list(self,lista):
        for c in lista:
            ing= Ingredient(orientation='horizontal')
            ing.name=c
            ing.quantity= lista[c]
            self.ids.box.add_widget(ing)












