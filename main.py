import tkinter as tk
import math
from operation import Operation

window = tk.Tk()
window.title('Test')
window.geometry('450x450')

entry = tk.Entry()
entry.place(x=0, y=0, width=360, height=90)

operation = Operation(0, 0, "")


def click_btn(event):
    caller = event.widget
    dict_btns = {
        ".!button": 1,
        ".!button2": 2,
        ".!button3": 3,
        ".!button4": 4,
        ".!button5": 5,
        ".!button6": 6,
        ".!button7": 7,
        ".!button8": 8,
        ".!button9": 9,
        ".!button12": 00,
        ".!button10": 0,
    }
    if str(caller) != ".!button12":
        num = dict_btns[str(caller)]
        entry.insert("end", num)
    else:
        entry.insert("end", 0)
        entry.insert("end", 0)

def delete(event):
    entry.delete(0, "end")


def first(event):
    caller = event.widget
    dict_btns = {
        ".!button13": "+",
        ".!button14": "log",
        ".!button15": "-",
        ".!button16": "deg",
        ".!button17": "*",
        ".!button18": "sin",
        ".!button19": "/",
        ".!button20": "cos",

    }
    operation.operation = dict_btns[str(caller)]
    operation.num1 = int(entry.get().strip())
    delete(event)


def second(event):
    operation.num2 = int(entry.get().strip())
    delete(event)

    if operation.operation == "+":
        entry.insert(0, str(operation.num1 + operation.num2))

    if operation.operation == "-":
        entry.insert(0, str(operation.num1 - operation.num2))

    if operation.operation == "*":
        entry.insert(0, str(operation.num1 * operation.num2))

    if operation.operation == "/":
        entry.insert(0, str(operation.num1 / operation.num2))

    if operation.operation == "deg":
        entry.insert(0, str(operation.num1 ** operation.num2))

    if operation.operation == "cos":
        entry.insert(0, str(math.cos(operation.num1)))

    if operation.operation == "sin":
        entry.insert(0, str(math.sin(operation.num1)))

    if operation.operation == "log":
        entry.insert(0, str(math.log(operation.num1, operation.num2)))

    operation.operation = ""


btns = []
x, y = 0, 90
for i in range(9):
    btn = tk.Button(window, text=str(i + 1))
    btn.place(x=x, y=y, width=90, height=90)
    btn.bind("<Button-1>", click_btn)
    btns.append(btn)
    x += 90
    if x == 270:
        x = 0
        y += 90

operations1 = ["0", "CLR", "00"]
btns_oper = []
x, y = 0, 360
for i in range(3):
    btn = tk.Button(window, text=operations1[i])
    btn.place(x=x, y=y, width=90, height=90)
    btn.bind("<Button-1>", click_btn)
    btns_oper.append(btn)
    x += 90

operations2 = ["+", "log", "-", "deg", "*", "sin", "/", "cos"]
x, y = 270, 90
for i in range(8):
    btn = tk.Button(window, text=operations2[i])
    btn.place(x=x, y=y, width=90, height=90)
    btns_oper.append(btn)
    x += 90
    if x == 450:
        x = 270
        y += 90

btn = tk.Button(window, text="=")
btn.place(x=360, y=0, width=90, height=90)
btns_oper.append(btn)

btns_oper[0].bind("<Button-1>", click_btn)
btns_oper[1].bind("<Button-1>", delete)
btns_oper[2].bind("<Button-1>", click_btn)
for i in range(3, 12):
    btns_oper[i].bind("<Button-1>", first)
btns_oper[11].bind("<Button-1>", second)

if __name__ == '__main__':
    window.mainloop()