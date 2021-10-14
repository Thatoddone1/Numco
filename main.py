import pyperclip as pc
import os
import pygubu
import tkinter as tk
import tkinter.ttk as ttk
encoded = ""
decoded = ""
def decode(text):
    decoded = ""
    for letter in text:
        decoded = decoded + inout[[f_inout[1] for f_inout in inout].index(letter)][0]
        return decoded

def encode(text):
    encoded = ""
    for letter in text:
        encoded = encoded + inout[[f_inout[0] for f_inout in inout].index(letter)][1]
    pc.copy(encoded)
    return encoded


inout = [
        [" ", "/"],
        ["q", "e"],
        ["w", "r"],
        ["e", "t"],
        ["r", "y"],
        ["t", "u"],
        ["y", "i"],
        ["u", "o"],
        ["i", "p"],
        ["o", "["],
        ["p", "]"],
        ["a", "d"],
        ["s", "f"],
        ["d", "g"],
        ["f", "h"],
        ["g", "j"],
        ["h", "k"],
        ["j", "l"],
        ["k", ";"],
        ["l", "'"],
        ["z", "c"],
        ["x", "v"],
        ["c", "b"],
        ["v", "n"],
        ["b", "m"],
        ["n", ","],
        ["m", "."],
        [".", "+"],
        [",", "1"],
        ["!", "|"],
        ["?", "*"],
        ["1", "3"],
        ["2", "4"],
        ["3", "5"],
        ["4", "6"],
        ["5", "7"],
        ["6", "8"],
        ["7", "9"],
        ["8", "0"],
        ["9", "-"],
        ["0", "="],
        ["#", "%"],
        ["Q", "E"],
        ["W", "R"],
        ["E", "T"],
        ["R", "Y"],
        ["T", "U"],
        ["Y", "I"],
        ["U", "O"],
        ["I", "P"],
        ["O", "{"],
        ["P", "}"],
        ["A", "D"],
        ["S", "F"],
        ["D", "G"],
        ["F", "H"],
        ["G", "J"],
        ["H", "K"],
        ["J", "L"],
        ["K", ":"],
        ["L", "?"],
        ["Z", "C"],
        ["X", "V"],
        ["C", "B"],
        ["V", "N"],
        ["B", "M"],
        ["N", "<"],
        ["M", ">"],
        ["_", "~"],

                ]


PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_UI = os.path.join(PROJECT_PATH, "newproject")


conorgui = input("Would you like the console UI or the GUI UI(gui/con) ")
if conorgui == "gui":



    class NumcoGuiApp:
        def __init__(self, master=None):
            # build ui
            self.frame1 = ttk.Frame(master)
            self.labelframe1 = ttk.Labelframe(self.frame1)
            self.Encode = ttk.Label(self.labelframe1)
            self.Encode.configure(text='Encode')
            self.Encode.pack(side='top')
            self.entry1 = ttk.Entry(self.labelframe1)
            self.encodetext = tk.StringVar(value='Text here')
            self.encodetext = tk.StringVar(value= "Text here")
            self.entry1.configure(textvariable=self.encodetext)
            _text_ = '''Text here'''
            self.entry1.delete('0', 'end')
            self.entry1.insert('0', _text_)
            self.entry1.pack(pady='10', side='top')
            self.button4 = ttk.Button(self.labelframe1)
            self.button4.configure(text='Encode')
            self.button4.pack(padx='100', pady='10', side='top')
            self.button4.configure(command=self.encodebut)
            self.separator2 = ttk.Separator(self.labelframe1)
            self.separator2.configure(orient='horizontal')
            self.separator2.pack(ipadx='150', pady='10', side='top')
            self.label3 = ttk.Label(self.labelframe1)
            self.label3.configure(text='Decode')
            self.label3.pack(side='top')
            self.entry3 = ttk.Entry(self.labelframe1)
            self.decodetext = tk.StringVar(value='Encoded text here')
            self.decodetext = tk.StringVar(value= "Encoded text here")
            self.entry3.configure(textvariable=self.decodetext)
            _text_ = '''Encoded text here'''
            self.entry3.delete('0', 'end')
            self.entry3.insert('0', _text_)
            self.entry3.pack(pady='10', side='top')
            self.button5 = ttk.Button(self.labelframe1)
            self.button5.configure(text='Decode')
            self.button5.pack(pady='10', side='top')
            self.button5.configure(command=self.decodebut)
            self.message1 = tk.Message(self.labelframe1)
            self.output = tk.StringVar(value='')
            self.message1.configure(textvariable=self.output)
            self.message1.pack(pady='100', side='top')
            self.labelframe1.configure(height='200', text='Numco', width='200')
            self.labelframe1.pack(side='top')
            self.labelframe1.bind('<1>', self.callback, add='')
            self.frame1.configure(height='200', width='200')
            self.frame1.pack(side='top')

            # Main widget
            self.mainwindow = self.frame1
    
        def encodebut(self):
            output = str(self.entry1.get())
            encoded = encode(output)
            self.message1.configure(text=encoded)
            self.message1.pack(pady='100', side='top')
            print(encoded)

        def decodebut(self):
            output = str(self.decodetext)
            decoded = decode(output)
            self.message1.configure(text=decoded)
            self.message1.pack(pady='100', side='top')
            print(decoded)

        def callback(self, event=None):
            pass

        def run(self):
            self.mainwindow.mainloop()


    if __name__ == '__main__':
        root = tk.Tk()
        app = NumcoGuiApp(root)
        app.run()










elif conorgui == "con":
    while True:
        encOrDec = input("Do you want to encode or decode (e/d/exit) ")
        encoded = ''
        decoded = ''
        if encOrDec == "e":
            text = input("What do you want to encode? ")
            encoutput = encode(text)
            print(encoutput)


        elif encOrDec == "d":
            text = input("What do you want to decode? ")
            decoutput = decode(text)
            print(decoutput)
        elif encOrDec == "exit":
            exit()
