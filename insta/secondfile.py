from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.label import Label
from kivymd.toast import toast
from kivymd.uix.button import MDRoundFlatButton, MDRoundFlatIconButton
from kivymd.uix.progressloader import MDProgressLoader

kv = Builder.load_file("second.kv")

class Hashplot(BoxLayout):
    pass

class Hashbar(BoxLayout):
    pass

class Enbox(BoxLayout):
    pass

class ImBox(BoxLayout):
    pass

class DownloadButton(MDRoundFlatIconButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.link=''
        self.path=''

    def download(self):
        progress=MDProgressLoader(url_on_image=self.link,
                                  path_to_file=self.path,
                                  download_complete=self.complete,
                                  download_hide=self.hide)
        progress.start(self)

    def complete(self):
        toast('Download Completed')

    def hide(self, instance_progress):
        x=0


class MostBox(BoxLayout):
    pass