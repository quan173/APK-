from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label


class HelloWorldApp(App):
    def build(self):
        button = Button(text='Click !', on_press=self.say_hello)
        return button

    def say_hello(self, instance):
        popup = Popup(title='Hello!', content=Label(text='Hello World!'), size_hint=(None, None), size=(400, 200))
        popup.open()


if __name__ == '__main__':
    HelloWorldApp().run()
