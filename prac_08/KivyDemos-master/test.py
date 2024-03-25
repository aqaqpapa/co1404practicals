from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
Builder.load_file('app.kv')

class MyBoxLayout(BoxLayout):
    def change_label_text(self):
        self.ids.my_label.text = "Button Clicked!"


class MyApp(App):
    def build(self):
        return MyBoxLayout()


if __name__ == '__main__':
    MyApp().run()
