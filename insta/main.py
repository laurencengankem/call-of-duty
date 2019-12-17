import certifi
import os
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import AsyncImage
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivy.network.urlrequest import UrlRequest
from kivymd.uix.dialog import  MDDialog
import statis
from secondfile import Hashplot, Hashbar, Enbox

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

class Barplot(BoxLayout):
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

        self.ids.ppp.clear_widgets()
        st= statis.comp('comments',Post)
        n1=st[1]
        b=Barplot(min_height=st[0],max_height=st[2],avg_height=st[1],norm=st[3])
        self.ids.ppp.add_widget(b)
        st = statis.comp('likes', Post)
        n2=st[2]
        b=Barplot(min_height=st[0],max_height=st[2],avg_height=st[1],norm=st[3],tit='likes')
        self.ids.ppp.add_widget(b)
        b = BoxLayout(orientation='vertical')
        er=((n1+n2)/int(Followers))*100
        e=Enbox()
        er=round(er,2)
        e.tt= str(er)+"%"


        (h1, h2) = statis.hash(Post)
        norm=1
        if(len(h2)>0):
            norm = max(h2)+0.5
        h = Hashplot()
        for i in range(len(h1)):
            h.ids.lab.add_widget(Label(text=str(h2[i]), halign='right'))
            h3 = Hashbar()
            h3.t= h1[i]
            h3.size_hint_x= 0.4+ (0.6*(h2[i]/norm))
            h.ids.labval.add_widget(h3)
        self.ids.ppp.add_widget(h)
        self.ids.ppp.add_widget(e)

        b.add_widget(
            Label(text='The Statistics are Based on \nthe Posts Below', font_size='20sp', underline=True,
                  valign="bottom",
                  halign="center"))
        self.ids.ppp.add_widget(b)

        for i in range(len(Post)):
            box =BoxLayout(orientation='vertical')
            box.add_widget(AsyncImage(source=Post[i]['url'],allow_stretch=True,size_hint=(1,1),pos_hint={"left":1}))
            box.add_widget(Label(text="comments: "+str(Post[i]['comments'])+' | '+"likes: "+str(Post[i]['likes'])+"\n"+Post[i]['type']+"\n"+Post[i]['date'],size_hint=(1,.2),halign='center',valign="top"))
            self.ids.ppp.add_widget(box)









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
                    if((len(txt)>0 and txt[0]!='#') or txt==''):
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
