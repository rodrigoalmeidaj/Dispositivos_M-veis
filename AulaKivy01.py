from kivy.uix.label import Label
from cProfile import label
from cgitb import text
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class AulaKivy01(App):
    def build(self):
        box = BoxLayout(orientation = 'vertical')
        box2 = BoxLayout(orientation = 'horizontal')
        button1 = Button(text = "Botão1", font_size = 30, on_release = self.incrementar)
        texto = Label(text = "Bem Vindo")
        texto.bold = True
        texto.color = [0, 5, 1, 1]
        box.add_widget(button1)
        box.add_widget(texto)
        
        

        button2 = Button(text = "Botão2")
        texto2 = Label(text = "Bem Vindo")
        box2.add_widget(button2)
        box2.add_widget(texto2)

        box.add_widget(box2)
        return box


    def incrementar(self, button):
        if button.text == "Botão 1":
            button.text == "Mudou"
        else:
            button.text == "Botão 1"

if __name__ == '__main__':
    AulaKivy01().run()