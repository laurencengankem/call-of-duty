import certifi
import os

from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import AsyncImage
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivy.network.urlrequest import UrlRequest
from kivymd.uix.button import MDRoundFlatButton
from kivymd.uix.dialog import  MDDialog
import statis
from secondfile import Hashplot, Hashbar, Enbox, ImBox, DownloadButton, MostBox

import endpoint
from datetime import datetime

os.environ['SSL_CERT_FILE']= certifi.where()

bio=""
account=""
user=""
source=""
profile: str=""
Followers=""
Followings=""
Posts=""
ID=""
real=""
private= False
ver= False

Post=[]

class WindowManager(ScreenManager):
    def change(self):
        sc=self.current_screen.name
        if( sc=='result'):
            self.current='first'
            return True
        else:
            return False

class First(Screen):
    pass

class Barplot(BoxLayout):
    pass


class Result(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_enter(self, *args):
        req = UrlRequest(source,file_path=profile,ca_file=certifi.where(),verify=False)
        req.wait()
        self.ids.user.text= account
        self.ids.posts.text='[b]Posts[/b] \n'+Posts
        self.ids.followers.text = '[b]Followers[/b] \n' + Followers
        self.ids.followings.text = '[b]Followings[/b] \n' + Followings
        self.ids.idp.text = '[b]Profile ID[/b] \n'+ ID
        self.ids.real.text = '[b]Name[/b] \n' + real
        self.ids.ver.text = '[b]Verified[/b] \n' + str(ver)
        if(private== True):
            self.ids.type.text = '[b]Account Type[/b] \n Private'
        else:
            self.ids.type.text = '[b]Account Type[/b] \n Public'
        self.ids.imp.pop= profile

        self.ids.ppp.clear_widgets()
        st= statis.comp('comments',Post)
        n1=st[1]
        maxim2=st[2]
        b=Barplot(min_height=st[0],max_height=st[2],avg_height=st[1],norm=st[3])
        self.ids.ppp.add_widget(b)
        st = statis.comp('likes', Post)
        n2=st[1]
        maxim1=st[2]
        b=Barplot(min_height=st[0],max_height=st[2],avg_height=st[1],norm=st[3],tit='likes')
        self.ids.ppp.add_widget(b)
        b = BoxLayout(orientation='vertical')
        er=((n1+n2)/int(Followers))*100
        e=Enbox()
        er=round(er,2)
        e.tt= str(er)+"%"
        ind=statis.mostliked(Post,maxim1)


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
        if (len(Post) > 0):
            m = MostBox()
            m.ss = Post[ind]['url']
            m.likes=Post[ind]['likes']
            for i in range(len(Post[ind]['hashtags'])):
                m.ids.list.text= m.ids.list.text+'\n #'+Post[ind]['hashtags'][i]
            self.ids.ppp.add_widget(m)


        self.ids.ppp.add_widget(e)

        b.add_widget(
            Label(text='The Statistics are Based on \nthe Posts Below', font_size='20sp', underline=True,
                  valign="bottom",
                  halign="center"))
        self.ids.ppp.add_widget(b)

        for i in range(len(Post)):
            box = BoxLayout(orientation='vertical')
            box.add_widget(
                AsyncImage(source=Post[i]['url'], allow_stretch=True, size_hint=(1, 1), pos_hint={"left": 1}))
            if Post[i]['type']== 'Video':
                box.add_widget(Label(
                    text="comments: " + str(Post[i]['comments']) + ' | ' + "likes: " + str(Post[i]['likes']) + "\n" +
                         Post[i]['type']+" | Views : "+str(Post[i]['view']) + "\n location: "+str(Post[i]['location'])+"\n"+ Post[i]['date'], size_hint=(1, .25), halign='center', valign="top"))
            else:
                box.add_widget(Label(
                    text="comments: " + str(Post[i]['comments']) + ' | ' + "likes: " + str(Post[i]['likes']) + "\n" +
                         Post[i]['type'] + "\n location: " + str(
                        Post[i]['location']) + "\n" + Post[i]['date'], size_hint=(1, .25), halign='center',
                    valign="top"))
            b=DownloadButton()
            b.link=Post[i]['url']
            b.path= '/sdcard/download/'+str(Post[i]['shortcode'])+'.jpg'
            box.add_widget(b)
            self.ids.ppp.add_widget(box)





class MainApp(MDApp):
    def __init__(self, **kwargs):
        self.theme_cls.primary_palette = "Blue"
        self.profile=''
        super().__init__(**kwargs)

    def on_start(self):
        Window.bind(on_keyboard=self.android_back_click)

    def android_back_click(self, window, key, *largs):
        if key == 27:
            if(self.root.change()):
                return True


    def search(self,input):
        try:
            if input !='':
                input.replace(" ", "")
                urli = endpoint.request_account_info(input)
                req=UrlRequest(urli,ca_file=certifi.where(),verify=False)
                req.wait()
                #req2=UrlRequest('http://localhost:5000/s/'+input)
                #req2.wait()
                #print(req2.result)
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
                global bio
                global ver

                account=input
                profile = input + '.jpg'
                source= self.profile
                self.profile=input+'.jpg'
                source = data['graphql']['user']['profile_pic_url']
                Followers = str(data['graphql']['user']['edge_followed_by']['count'])
                Followings = str(data['graphql']['user']['edge_follow']['count'])
                Posts = str(data['graphql']['user']['edge_owner_to_timeline_media']['count'])
                bio=data['graphql']['user']['biography']
                ID= str(data['graphql']['user']['id'])
                real= str(data['graphql']['user']['full_name'])
                ver=data['graphql']['user']['is_verified']
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
                    shortcode=data['graphql']['user']['edge_owner_to_timeline_media']['edges'][i]['node']['shortcode']
                    location=data['graphql']['user']['edge_owner_to_timeline_media']['edges'][i]['node']['location']
                    if(location != None):
                        location=location['name']
                    h=data['graphql']['user']['edge_owner_to_timeline_media']['edges'][i]['node']['edge_media_to_caption']['edges']
                    hashtags=[]
                    if(len(h)>0):
                        txt=data['graphql']['user']['edge_owner_to_timeline_media']['edges'][i]['node']['edge_media_to_caption']['edges'][0]['node']['text']
                        hashtags=txt.split('#')
                        if((len(txt)>0 and txt[0]!='#') or txt==''):
                            hashtags.pop(0)
                    type='Photo'
                    count=0

                    if(t):
                        type='Video'
                        count=data['graphql']['user']['edge_owner_to_timeline_media']['edges'][i]['node']['video_view_count']

                    Post.append({"url":url,"comments":comments,"likes":likes,"type":type,"date":str(date),"hashtags": hashtags,"shortcode":shortcode,"location":location,"view":count})
                self.root.current= 'result'
            elif(input== ''):
                dialog = MDDialog(
                    title="Alert",
                    size_hint=(0.8, 0.3),
                    text_button_ok="Ok",
                    text='insert a profile name'
                )
                dialog.open()
        except:
            dialog = MDDialog(
                title="Error",
                size_hint=(0.8, 0.3),
                text_button_ok="Ok",
                text="There's no profile corresponding to this name "
            )
            dialog.open()




if __name__ == "__main__":
    MainApp().run()
