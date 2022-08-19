from kivy.uix.label import Label
from cProfile import label
from cgitb import text
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class AulaKivy01_2(App):
    def build(self):
        self.box = BoxLayout(orientation = 'vertical')
        self.button1 = Button(text = "Incremento", font_size = 30, on_release = self.incrementar)
        self.texto = Label (text = "1", font_size = 50)
        self.texto.bold = True
        self.texto.color = [0, 5, 1, 1]
        self.box.add_widget(self.button1)
        self.box.add_widget(self.texto)
        

        return self.box

    def incrementar(self, button):
        if int(self.texto.text) <= 9:
            self.texto.text = str(int(self.texto.text)+1)
        else:
            self.texto.text = str(int(self.texto.text)-9)





if __name__ == '__main__':
    AulaKivy01_2().run()