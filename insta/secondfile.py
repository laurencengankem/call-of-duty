import certifi
from kivy.network.urlrequest import UrlRequest
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivymd.toast import toast
from kivymd.uix.button import MDRoundFlatButton, MDRoundFlatIconButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.progressloader import MDProgressLoader
import os
import endpoint

os.environ['SSL_CERT_FILE']= certifi.where()
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
        req1=UrlRequest(info1['source'],file_path=info1['profile']+".jpg",ca_file=certifi.where(),verify=False)
        req2=UrlRequest(info2['source'],file_path=info2['profile']+".jpg",ca_file=certifi.where(),verify=False)
        req1.wait()
        req2.wait()
        self.ids.imp1.pop= info1['profile']+".jpg"
        self.ids.imp2.pop = info2['profile']+".jpg"
        self.ids.b1.ids.nome.text= info1['profile']
        self.ids.b2.ids.nome.text = info2['profile']
        self.ids.b1.ids.followers.text="[b]Followers[/b] \n"+info1['Followers']
        self.ids.b1.ids.followings.text = "[b]Followings[/b] \n" + info1['Followings']
        self.ids.b1.ids.posts.text = "[b]Posts[/b] \n" + info1['Posts']
        self.ids.b2.ids.followers.text = "[b]Followers[/b] \n" + info2['Followers']
        self.ids.b2.ids.followings.text = "[b]Followings[/b] \n" + info2['Followings']
        self.ids.b2.ids.posts.text = "[b]Posts[/b] \n" + info2['Posts']




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
    return {"profile":input,"source":source,"Followers":Followers,"Followings":Followings,"Posts":Posts}
