import math
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scatter import Scatter
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

btnlist = [['7', '8', '9', '+','√'],
           ['4','5','6','-','π'],
           ['1','2','3','*','('],
           ['C','0','=','/',')'],
           ['log','.','BACK','AC','CE']]
count = 0
def onClick(textinput, btn):
    global count
    print("Click Button:", btn.text)

    if(btn.text == 'C'):
        textinput.text = ''
    elif(btn.text == '='):
        textinput.text = str(eval(textinput.text))
    elif(btn.text == '√'):
        textinput.text = textinput.text + '**0.5'
    elif(btn.text == 'π'):
        textinput.text += '*3.14'
    elif(btn.text == '('):
        textinput.text = textinput.text + btn.text
        count+=1 
    elif(btn.text == ')'):
        if(count > 0):
            count-=1
            textinput.text += btn.text
        else:
            pass
    elif(btn.text == 'log'):
        for i, c in enumerate(textinput.text[::-1]):
            if(c in ['+','-','*','/']):
                textinput.text = textinput.text[:-1] + 'log(' + textinput.text[-i:]+')'
                break
        n1 = textinput.text.find('+')
        n2 = textinput.text.find('-')
        n3 = textinput.text.find('*')
        n4 = textinput.text.find('/')
        if (n1 == n2 == n3 == n4 == -1):
            textinput.text = 'log(' + textinput.text +')'
    elif(btn.text == 'BACK'):
        textinput.text = textinput.text[:-1]
    elif(btn.text == '.'):
        textinput.text += '.'
    elif(btn.text == 'AC'):
        pass
    elif(btn.text == 'CE'):
        pass
    else:
        textinput.text += btn.text
    

class MyApp(App):
    def build(self):
        self.title = "계산기"
        B = BoxLayout(orientation="vertical")
        T = TextInput(font_size=50)
        B.add_widget(T)

        G = GridLayout(cols=5)
        for i, btnl in enumerate(btnlist):
            for j, key in enumerate(btnl):
                btn = Button(text=key, font_size=30)
                
                def cmd(btn = btn):
                    onClick(T, btn)

                btn.bind(on_press=cmd)
                G.add_widget(btn)
        B.add_widget(G)
        return B
    
MyApp().run()

