from cProfile import label
from cgitb import text
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Test(App):
    def build(self):
        box = BoxLayout(orientation = 'horizontal')
        button = Button(text = "Botão1")
        button2 = Button(text = "Botão2")
        texto = Label(text = "Bem Vindo")
        texto.bold = True
        texto.color = [0, 5, 1, 1]
        box.add_widget(button)
        box.add_widget(texto)
        box.add_widget(button2)
        return box

if __name__ == '__main__':
    Test().run()