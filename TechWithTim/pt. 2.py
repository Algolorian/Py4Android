from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 2  # Set columns for main layout

        # ALL OF THESE ARE APART OF THE (INTERIOR)NEW LAYOUT
        self.add_widget(Label(text="First Name: "))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        self.add_widget(Label(text="Last Name: "))
        self.lastName = TextInput(multiline=False)
        self.add_widget(self.lastName)

        self.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False)
        self.add_widget(self.email)


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()
