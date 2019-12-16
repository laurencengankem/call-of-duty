import certifi
import os
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import AsyncImage
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivy.network.urlrequest import UrlRequest
from kivymd.uix.dialog import  MDDialog
import matlab

import endpoint
from datetime import datetime

os.environ['SSL_CERT_FILE']= certifi.where()

account=""
source=""
profile: str=""
Followers=""
Followings=""
Posts=""
ID=""
real=""
private= False

Post=[]

class First(Screen):
    pass


class Login(Screen):
    pass

class Register(Screen):
    pass

class Result(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_enter(self, *args):
        req = UrlRequest(source,file_path=profile,ca_file=certifi.where(),verify=False)
        req.wait()
        self.ids.posts.text='Posts: '+Posts
        self.ids.followers.text = 'Followers: ' + Followers
        self.ids.followings.text = 'Followings: ' + Followings
        self.ids.idp.text = 'Profile ID: '+ ID
        self.ids.prof.text = 'Profile Name: ' + account
        self.ids.real.text = 'Real Name: ' + real
        if(private== True):
            self.ids.type.text = 'Account Type: Private'
        else:
            self.ids.type.text = 'Account Type: Public'
        self.ids.imp.pop= profile
        i=0
        self.ids.ppp.clear_widgets()
        for i in range(len(Post)):
            box =BoxLayout(orientation='vertical')
            box.add_widget(AsyncImage(source=Post[i]['url'],allow_stretch=True,size_hint=(1,1),pos_hint={"left":1}))
            box.add_widget(Label(text="comments: "+str(Post[i]['comments'])+' | '+"likes: "+str(Post[i]['likes'])+"\n"+Post[i]['type']+"\n"+Post[i]['date'],size_hint=(1,.2),halign='center'))
            self.ids.ppp.add_widget(box)

        b = BoxLayout(orientation='vertical')
        b.add_widget(Label(text='These are the '+str(len(Post))+' Latest Posts \nof ' + str(real) , font_size='15sp',
                           halign="center"))
        self.ids.ppp.add_widget(b)
        self.ids.f3.clear_widgets()
        boxes=matlab.figure(Post)
        matlab.hash(Post)
        self.ids.f3.add_widget(boxes[0])
        self.ids.f3.add_widget(boxes[1])
        self.ids.f3.add_widget(boxes[2])
        self.ids.f3.add_widget(Label(text="The Computation of these statistics\n is based on the \n 12 most recent Posts",halign='center'))




class MainApp(MDApp):
    def __init__(self, **kwargs):
        self.theme_cls.primary_palette = "Blue"
        self.profile=''
        super().__init__(**kwargs)

    def search(self,input):

        if input != '':
            input.replace(" ", "")
            urli = endpoint.request_account_info(input)
            req=UrlRequest(urli,ca_file=certifi.where(),verify=False)
            req.wait()
            data = req.result
            global source
            global profile
            global Followers
            global Followings
            global Posts
            global ID
            global account
            global real
            global Post
            global private
            account=input
            profile = input + '.jpg'
            source= self.profile
            self.profile=input+'.jpg'
            source = data['graphql']['user']['profile_pic_url']
            Followers = str(data['graphql']['user']['edge_followed_by']['count'])
            Followings = str(data['graphql']['user']['edge_follow']['count'])
            Posts = str(data['graphql']['user']['edge_owner_to_timeline_media']['count'])
            ID= str(data['graphql']['user']['id'])
            real= str(data['graphql']['user']['full_name'])
            private = data['graphql']['user']['is_private']
            p=len(data['graphql']['user']['edge_owner_to_timeline_media']['edges'])
            i=0
            Post.clear()
            for i in range(p):
                url=data['graphql']['user']['edge_owner_to_timeline_media']['edges'][i]['node']['thumbnail_resources'][2]['src']
                comments= data['graphql']['user']['edge_owner_to_timeline_media']['edges'][i]['node']['edge_media_to_comment']['count']
                likes= data['graphql']['user']['edge_owner_to_timeline_media']['edges'][i]['node']['edge_liked_by']['count']
                t=data['graphql']['user']['edge_owner_to_timeline_media']['edges'][i]['node']['is_video']
                time= data['graphql']['user']['edge_owner_to_timeline_media']['edges'][i]['node']['taken_at_timestamp']
                date=datetime.fromtimestamp(time)
                #print(data['graphql']['user']['edge_owner_to_timeline_media']['edges'][i]['node']['edge_media_to_caption']['edges'])
                h=data['graphql']['user']['edge_owner_to_timeline_media']['edges'][i]['node']['edge_media_to_caption']['edges']
                hashtags=[]
                if(len(h)>0):
                    txt=data['graphql']['user']['edge_owner_to_timeline_media']['edges'][i]['node']['edge_media_to_caption']['edges'][0]['node']['text']
                    hashtags=txt.split('#')
                    if(txt[0]!='#'):
                        hashtags.pop(0)
                type='Photo'
                if(t):
                    type='Video'

                Post.append({"url":url,"comments":comments,"likes":likes,"type":type,"date":str(date),"hashtags": hashtags})
            self.root.ids.manager.current= 'result'
        else:
            dialog = MDDialog(
                title="Alert",
                size_hint=(0.8, 0.3),
                text_button_ok="Ok",
                text="Insert an account name"
            )
            dialog.open()

    def show_example_input_dialog(self,input1,input2,input3):

        if(input1!=input2):
            dialog = MDDialog(
                title="Error message",
                size_hint=(0.8, 0.3),
                text_button_ok="Ok",
                text = "The 2 Passwords you entered are differents"
            )
            dialog.open()
        elif(input1=='' or input2=='' or input3==''):
            dialog = MDDialog(
                title="Alert",
                size_hint=(0.8, 0.3),
                text_button_ok="Ok",
                text="Fill all the fields"
            )
            dialog.open()

    def show_example_dialog(self,input1,input2):
        if(input1=='' or input2==''):
            dialog = MDDialog(
                title="Alert",
                size_hint=(0.8, 0.3),
                text_button_ok="Ok",
                text = "Fill all the fields"
            )
            dialog.open()

if __name__ == "__main__":
    MainApp().run()