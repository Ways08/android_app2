# import Kivy
import kivy
import random
from math import sqrt
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.config import Config
from kivy.core.window import Window

'''
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '640')
Config.set('graphics', 'height', '520')
'''
Window.fullscreen = True

class MyApp(App):
# layout

    def build(self):
        layout = BoxLayout(padding=10, orientation='vertical')
        self.txt1 = TextInput(text='', multiline=False)
        self.lbl1 = Label(text="Введите числа: a b c")
        layout.add_widget(self.lbl1)
        layout.add_widget(self.txt1)
        btn1 = Button(text="OK")
        btn1.bind(on_press=self.buttonClicked)
        layout.add_widget(btn1)


        return layout

# button click function
    def buttonClicked(self,btn):
        try:
            unsplittedstr = self.txt1.text
            z, v, n = unsplittedstr.split(' ')
            a = int(z)
            b = int(v)
            c = int(n)
            disc = (b*b + (-4 * a * c))
            if disc > 0:
                x1 = ((-b + sqrt(disc)) / (a*2))
                x2 = ((-b - sqrt(disc)) / (a*2))
                self.lbl1.text = ("D = " + str(disc) + "\nx1 = {0}, x2 = {1}".format(str(x1), str(x2)) + "\nРазложенное: " + str(a) + "(x - (" + str(x1) + ")(x - (" + str(x2) + (")"))
                
            elif disc == 0:
                x = ((b * (-1)) / (2*a))
                self.lbl1.text = ("D = " + str(disc) + "\nx = " + str(x) + "\nРазложенное: " + str(a) + "(x - " + str(x) + ") \nP.S. Скобка в квадрате")
            else:
                self.lbl1.text = ("D = " + str(disc) + "\nНет корней")
        except:
            self.lbl1.text = "Ошибка!"

    
        #   self.txt1.text

# run app
if __name__ == "__main__":
    MyApp().run()


'''
def eqls(a, b, c):


'''
