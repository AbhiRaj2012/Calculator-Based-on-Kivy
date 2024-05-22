from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang.builder import Builder


Builder.load_file('./cal.kv')
Window.clearcolor = (1,1,1, 1)

class CalWidget(Widget):
    def clear(self):
        self.ids.input_box.text = '0'

    def btnClick(self,num):
        pText=self.ids.input_box.text

        if pText =='0':
            self.ids.input_box.text=""
            self.ids.input_box.text =f"{num}"

        else:
            self.ids.input_box.text = f"{pText}{num}"

    def total(self):
        try:
            self.ids.input_box.text = str(eval( self.ids.input_box.text))
        except:
            self.ids.input_box.text = "Error "


class CalApp(App):
    def build(self):
        return CalWidget(  )

if __name__=="__main__":
    CalApp().run()