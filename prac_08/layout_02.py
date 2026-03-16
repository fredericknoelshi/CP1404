from kivy.app import App
from kivy.lang import Builder


class Layout2(App):
    def build(self):
        self.title = "Layout2"
        self.root = Builder.load_file("layout_02.kv")
        return self.root


Layout2().run()