import pyperclip as pc
encoded = ""
decoded = ""

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
    encOrDec = input("Do you want to encode or decode (e/d) ")
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
