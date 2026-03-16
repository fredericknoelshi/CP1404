from kivy.app import App
from kivy.lang import Builder


class Layout1(App):
    def build(self):
        self.title = "Layout1"
        self.root = Builder.load_file("layout_01.kv")
        return self.root


Layout1().run()