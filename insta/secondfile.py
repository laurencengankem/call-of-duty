import certifi
from kivy.metrics import sp
from kivy.network.urlrequest import UrlRequest
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivymd.toast import toast
from kivymd.uix.button import MDRoundFlatButton, MDRoundFlatIconButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.progressloader import MDProgressLoader
import statis

import endpoint

kv = Builder.load_file("second.kv")

info1={}
info2={}


class Hashplot(BoxLayout):
    pass

class Hashbar(BoxLayout):
    pass

class Enbox(BoxLayout):
    pass

class ImBox(BoxLayout):
    pass

class Box(BoxLayout):
    pass

class DownloadButton(MDRoundFlatIconButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.link=''
        self.path=''

    def download(self):
        try:
            progress=MDProgressLoader(url_on_image=self.link,
                                      path_to_file=self.path,
                                      download_complete=self.complete,
                                      download_hide=self.hide)
            progress.start(self)
        except:
            dialog = MDDialog(
                title="Alert",
                size_hint=(0.8, 0.3),
                text_button_ok="Ok",
                text="check the storage permission"
            )
            dialog.open()

    def complete(self):
        toast('Download Completed')

    def hide(self, instance_progress):
        x=0


class MostBox(BoxLayout):
    pass


class CompResult(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_enter(self, *args):
        req1=UrlRequest(info1['source'],file_path=info1['profile']+".jpg")
        req2=UrlRequest(info2['source'],file_path=info2['profile']+".jpg")
        req1.wait()
        req2.wait()
        self.ids.imp1.pop= info1['profile']+".jpg"
        self.ids.imp2.pop = info2['profile']+".jpg"
        self.ids.b1.ids.nome.text= "[b]"+info1['profile']+"[/b]"
        self.ids.b2.ids.nome.text = "[b]"+info2['profile']+"[/b]"
        self.ids.b1.ids.followers.text="[b]Followers[/b] \n"+info1['Followers']
        self.ids.b1.ids.followings.text = "[b]Followings[/b] \n" + info1['Followings']
        self.ids.b1.ids.posts.text = "[b]Posts[/b] \n" + info1['Posts']
        self.ids.b1.ids.avg_c.text = "[b]comments/post[/b] \n" + str(info1['avg_com'])
        self.ids.b1.ids.avg_l.text = "[b]likes/post[/b] \n" + str(info1['avg_likes'])
        er1 = (info1['avg_com'] + info1['avg_likes']) / int(info1['Followers'])*100
        self.ids.b1.ids.er.text = "[b]E.R[/b] \n" + str(round(er1,2))+"%"

        (h1, h2) = statis.hash(info1['Post'])
        norm = 1
        if (len(h2) > 0):
            norm = max(h2) + 0.5
        h = Hashplot()
        for i in range(len(h1)):
            h.ids.lab.add_widget(Label(text=str(h2[i]), halign='right',color=(0,0,0.7,1)))
            h3 = Hashbar()
            h3.siz=sp(10)
            h3.t = h1[i]
            h3.size_hint_x = 0.4 + (0.6 * (h2[i] / norm))
            h.ids.labval.add_widget(h3)
        self.ids.box1.add_widget(h)

        self.ids.b2.ids.followers.text = "[b]Followers[/b] \n" + info2['Followers']
        self.ids.b2.ids.followings.text = "[b]Followings[/b] \n" + info2['Followings']
        self.ids.b2.ids.posts.text = "[b]Posts[/b] \n" + info2['Posts']
        self.ids.b2.ids.avg_c.text = "[b]comments/post[/b] \n" + str(info2['avg_com'])
        self.ids.b2.ids.avg_l.text = "[b]likes/post[/b] \n" + str(info2['avg_likes'])
        er2=(info2['avg_com'] + info2['avg_likes']) / int(info2['Followers'])*100
        self.ids.b2.ids.er.text = "[b]E.R[/b] \n" + str(round(er2,2))+"%"

        (h1, h2) = statis.hash(info2['Post'])
        norm = 1
        if (len(h2) > 0):
            norm = max(h2) + 0.5
        h = Hashplot()
        for i in range(len(h1)):
            h.ids.lab.add_widget(Label(text=str(h2[i]), halign='right',color=(0,0.6,0,1)))
            h3 = Hashbar()
            h3.siz=sp(10)
            h3.t = h1[i]
            h3.size_hint_x = 0.4 + (0.6 * (h2[i] / norm))
            h.ids.labval.add_widget(h3)
        self.ids.box2.add_widget(h)



class Comparaison(Screen):
    def compare(self,input1,input2):
        if (input1 == '' or input2 == '' or input1==input2):
            dialog = MDDialog(
                title="Alert",
                size_hint=(0.8, 0.3),
                text_button_ok="Ok",
                text="enter 2 differents profile name"
            )
            dialog.open()

        else:
            input1.replace(" ", "")
            input2.replace(" ", "")
            url1 = endpoint.request_account_info(input1)
            url2= endpoint.request_account_info(input2)
            req1 =UrlRequest(url1, ca_file=certifi.where(), verify=False)
            req2= UrlRequest(url2, ca_file=certifi.where(), verify=False)
            req1.wait()
            req2.wait()
            data1=req1.result
            data2=req2.result
            type1=data1['graphql']['user']['is_private']
            type2=data2['graphql']['user']['is_private']
            if type1:
                dialog = MDDialog(
                    title="Alert",
                    size_hint=(0.8, 0.3),
                    text_button_ok="Ok",
                    text=input1+" is a private profile"
                )
                dialog.open()
            elif type2:
                dialog = MDDialog(
                    title="Alert",
                    size_hint=(0.8, 0.3),
                    text_button_ok="Ok",
                    text=input2+" is a private profile"
                )
                dialog.open()
            else:
                global info1
                global info2
                info1= extract(data1,input1)
                info2= extract(data2,input2)
                self.parent.current='compresult'



def extract(data,input):
    source = data['graphql']['user']['profile_pic_url']
    Followers = str(data['graphql']['user']['edge_followed_by']['count'])
    Followings = str(data['graphql']['user']['edge_follow']['count'])
    Posts = str(data['graphql']['user']['edge_owner_to_timeline_media']['count'])
    p = len(data['graphql']['user']['edge_owner_to_timeline_media']['edges'])
    post=[]
    for i in range(p):
        comments = data['graphql']['user']['edge_owner_to_timeline_media']['edges'][i]['node']['edge_media_to_comment']['count']
        likes = data['graphql']['user']['edge_owner_to_timeline_media']['edges'][i]['node']['edge_liked_by']['count']
        h = data['graphql']['user']['edge_owner_to_timeline_media']['edges'][i]['node']['edge_media_to_caption']['edges']
        hashtags = []
        if (len(h) > 0):
            txt = data['graphql']['user']['edge_owner_to_timeline_media']['edges'][i]['node']['edge_media_to_caption']['edges'][0]['node']['text']
            hashtags = txt.split('#')
            if ((len(txt) > 0 and txt[0] != '#') or txt == ''):
                hashtags.pop(0)
        post.append({"comments": comments, "likes": likes,"hashtags":hashtags})

    mc=statis.comp('comments',post)
    ml=statis.comp('likes',post)

    return {"profile":input,"source":source,"Followers":Followers,"Followings":Followings,"Posts":Posts,"avg_com":mc[1],"avg_likes":ml[1],"Post":post}

