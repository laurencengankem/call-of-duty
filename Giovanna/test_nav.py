from kivy.graphics.context_instructions import Color
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.modalview import ModalView

from kivy.uix.popup import Popup
from kivy.uix.videoplayer import VideoPlayer
from kivymd.uix.bottomsheet import MDCustomBottomSheet
from kivymd.uix.card import MDSeparator
from kivymd.uix.list import MDList

Builder.load_string(
    """
#:import Window kivy.core.window.Window
#:import get_hex_from_color kivy.utils.get_hex_from_color

                
<Subscribe>
    size_hint_y: 1
    orientation:'vertical'
    Button:
        background_normal: 'gold.jpg'
        text:'Subscribe to get access to the recipe \\n 0.99€/Month'
        halign:'center'
        color: 0.2,0,0,1
        font_size: self.width/18       
                    
        
<FoodItem>
    mod:1
    orientation:'vertical'
    bg: 'bambini.jpg'
    size_hint_y: .45
    text: "love"
    callback: None
    callback1: None
    canvas:
        Color:
            rgb: 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.width,self.height
            source: root.bg
            
    BoxLayout:
        size_hint:1,.2
               
        BoxLayout:
            size_hint:.65,.2
            pos_hint:{"top":1,}
            Label:
                text: root.text
                halign:'left'
                font_size: self.width/10
                color: 0,0,0,1
        
        BoxLayout:
            size_hint:.35,1
            MDIconButton:
                pos_hint:{"top":1,}
                icon:'star'
            MDIconButton:
                pos_hint:{"top":1,}
                icon:'star'
            MDIconButton:
                pos_hint:{"top":1,}
                icon:'star'
            MDIconButton:
                pos_hint:{"top":1,}
                icon:'star-outline'
            MDIconButton:
                pos_hint:{"top":1,}
                icon:'star-outline'
        
         
        
                
    BoxLayout:
        size_hint_y:.1
        spacing: dp(3)
        Button:
            size_hint_y:.5
            opacity: 0.6
            font_size: self.parent.width/15
            text: 'Ingredients'
            on_release: root.callback()
            
        Button:
            size_hint_y:.5
            opacity: 0.6
            font_size: self.parent.width/15
            text: 'Preparation'
            on_release: root.show_preparation(root.text)
        

    
<Mypopup>
    size_hint: .8,.9
    auto_dismiss: True
    canvas:
        Color:
            rgb: 1,1,1
        Rectangle:
            pos:self.pos
            size: self.size
    
    BoxLayout:
        orientation: 'vertical'
        size_hint: 1,1
        spacing: dp(10)

        
        Label:
            size_hint: 1,.2
            pos_hint:{"top":1}
            halign: 'center'
            text: 'Ingredients'
            font_size: self.width/10
            anchor_y: 'top'
            color: 0,0,0,1
            
        MDSeparator:
        
        BoxLayout:
            id: box
            orientation: 'vertical'
            BoxLayout:
                size_hint: 1,.2
                Label:
                    text: 'Name'
                    font_size: self.width/12
                    bold: True
                    color: 0,0,0,1
                Label:
                    text: 'Quantity'
                    font_size: self.width/12
                    bold: True
                    color: 0,0,0,1
            BoxLayout:
                size_hint: 1,.15        
                Label:
                    text: 'Eggs'
                    color: 0,0,0,1
                Label:
                    text: '2'
                    color: 0,0,0,1
            BoxLayout:
                size_hint: 1,.15    
                Label:
                    text: 'Milk'
                    color: 0,0,0,1
                Label:
                    text: '200ml'
                    color: 0,0,0,1        
            BoxLayout:
                size_hint: 1,.2    
                Label:
                    text: 'apple'
                    color: 0,0,0,1
                Label:
                    text: '200g'
                    color: 0,0,0,1
            MDSeparator:        
            BoxLayout:
                Label:
                    halign: 'center'
                    color: 0,0,0,1
                    text: 'Ingredients for \\n one meal and \\n one baby'
                    font_size: self.width/17
        
<Mypoppreparation>
    size_hint: .8,.9
    auto_dismiss: True
    on_pre_dismiss: self.ids.video.state= 'stop'
    canvas:
        Color:
            rgb: 1,1,1
        Rectangle:
            pos:self.pos
            size: self.size
    
    BoxLayout:
        orientation: 'vertical'
        size_hint: 1,1
        spacing: dp(10)

        
        Label:
            size_hint: 1,.2
            pos_hint:{"top":1}
            halign: 'center'
            text: 'Preparation'
            font_size: self.width/10
            anchor_y: 'top'
            color: 0,0,0,1
            
        MDSeparator:
        
        BoxLayout:
            padding: dp(30)
            VideoPlayer:
                id: video
                source: 'alex.mp4'
                image_overlay_play: 'marmelata.png'
                 
                        
"""
)

recipe=''

class FoodItem(BoxLayout):

    def show_example_custom_bottom_sheet(self, text):
        popup=Mypopup()
        if text !='marmelata':
            popup.remove_widget(popup.children[0])
            popup.padding=dp(10)
            popup.size_hint_y=0.3
            popup.add_widget(Subscribe())
        popup.open()


    def show_preparation(self,text):
        popup1 = Mypoppreparation()
        if text != 'marmelata':
            popup1.remove_widget(popup1.children[0])
            popup1.padding = dp(5)
            popup1.size_hint_y = 0.3
            popup1.add_widget(Subscribe())
        popup1.open()

class Mypopup(ModalView):
    pass

class Mypoppreparation(ModalView):
    pass

class Subscribe(BoxLayout):
    pass












