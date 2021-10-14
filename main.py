import pyperclip as pc
import os
import pygubu
import tkinter as tk
import tkinter.ttk as ttk
encrypted = ""

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_UI = os.path.join(PROJECT_PATH, "newproject")

class Numco:
    def __init__(self, master=None):
        # build ui
        self.frame2 = ttk.Frame(master)
        self.labelframe1 = ttk.Labelframe(self.frame2)
        self.entry1 = ttk.Entry(self.labelframe1)
        _text_ = '''Message Here'''
        self.entry1.delete('0', 'end')
        self.entry1.insert('0', _text_)
        self.entry1.pack(padx='100', pady='10', side='top')
        self.button2 = ttk.Button(self.labelframe1)
        self.button2.configure(text='Encode')
        self.button2.pack(pady='10', side='top')
        self.labelframe1.configure(height='200', text='Numco', width='200')
        self.labelframe1.pack(side='top')
        self.separator1 = ttk.Separator(self.frame2)
        self.separator1.configure(orient='horizontal', style='Toolbutton')
        self.separator1.pack(side='top')
        self.entry2 = ttk.Entry(self.frame2)
        _text_ = '''Encoded Here'''
        self.entry2.delete('0', 'end')
        self.entry2.insert('0', _text_)
        self.entry2.pack(pady='10', side='top')
        self.button3 = ttk.Button(self.frame2)
        self.button3.configure(text='Decode')
        self.button3.pack(pady='10', side='top')
        self.message2 = tk.Message(self.frame2)
        self.encrypted = tk.StringVar(value='')
        self.message2.configure(textvariable = encrypted)
        self.message2.pack(pady='50', side='top')
        self.frame2.configure(height='2000', width='2000')
        self.frame2.pack(side='top')

        # Main widget
        self.mainwindow = self.frame2
    

    def run(self):
        self.mainwindow.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    app = Numco(root)
    app.run()








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

                ]

while True:
    encOrDec = input("Do you want to encode or decode (e/d/exit) ")
    encoded = ''
    decoded = ''
    if encOrDec == "e":
        text = input("what do you want to encode? ")

        for letter in text:
            encoded = encoded + inout[[f_inout[0] for f_inout in inout].index(letter)][1]
        pc.copy(encoded)
        print(encoded)


    elif encOrDec == "d":
        text = input("what do you want to decode? ")

        for letter in text:
            decoded = decoded + inout[[f_inout[1] for f_inout in inout].index(letter)][0]
        print(decoded)
    
    elif encOrDec == "exit":
        exit()

function decode():
    text = input("what do you want to decode? ")

    for letter in text:
        decoded = decoded + inout[[f_inout[1] for f_inout in inout].index(letter)][0]
        print(decoded)