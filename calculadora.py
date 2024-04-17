import tkinter as tk
import math

# Definir display como una variable global
display = None

def clear():
    display.delete(0, tk.END)

def button_click(symbol):
    current = display.get()
    if symbol == '^':
        # Si el símbolo es "^", agregamos "**" para indicar la potencia en Python
        display.insert(tk.END, '**')
    else:
        display.insert(tk.END, symbol)

def evaluate():
    try:
        expression = display.get()
        expression = expression.replace('π', 'math.pi')
        # Evaluar expresiones con potencias usando "**"
        expression = expression.replace('^', '**')
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

def add():
    button_click('+')

def subtract():
    button_click('-')

def multiply():
    button_click('*')

def divide():
    button_click('/')

def sin():
    try:
        expression = display.get()
        expression = expression.replace('π', 'math.pi')
        result = math.sin(eval(expression))
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

def cos():
    try:
        expression = display.get()
        expression = expression.replace('π', 'math.pi')
        result = math.cos(eval(expression))
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

def tan():
    try:
        expression = display.get()
        expression = expression.replace('π', 'math.pi')
        result = math.tan(eval(expression))
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

def log():
    try:
        expression = display.get()
        expression = expression.replace('π', 'math.pi')
        result_expression = eval(expression)
        result = math.log10(result_expression)
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

def sqrt():
    try:
        expression = display.get()
        expression = expression.replace('π', 'math.pi')
        result = math.sqrt(eval(expression))
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

def arcsin():
    try:
        expression = display.get()
        expression = expression.replace('π', 'math.pi')
        result = math.asin(eval(expression))
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

def arccos():
    try:
        expression = display.get()
        expression = expression.replace('π', 'math.pi')
        result = math.acos(eval(expression))
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

def arctan():
    try:
        expression = display.get()
        expression = expression.replace('π', 'math.pi')
        result = math.atan(eval(expression))
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

def open_calculator():
    global display  # Asegurar que se está utilizando la variable global
    root = tk.Tk()
    root.title("Calculadora Científica")

    display = tk.Entry(root, width=40, borderwidth=5)
    display.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('C', 1, 4),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('(', 2, 4),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), (')', 3, 4),
        ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('π', 4, 3), ('=', 4, 4),
        ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('log', 5, 3), ('√', 5, 4),
        ('^', 6, 0), ('arcsin', 6, 1), ('arccos', 6, 2), ('arctan', 6, 3)
    ]

    # Funciones para las operaciones matemáticas
    operations = {'+': add, '-': subtract, '*': multiply, '/': divide, 'sin': sin, 'cos': cos, 'tan': tan, 'log': log, '√': sqrt, 'arcsin': arcsin, 'arccos': arccos, 'arctan': arctan}

    for (text, row, col) in buttons:
        if text == '=':
            button = tk.Button(root, text=text, padx=20, pady=20, command=evaluate)
        elif text in operations:
            button = tk.Button(root, text=text, padx=20, pady=20, command=operations[text])
        elif text == 'C':
            button = tk.Button(root, text=text, padx=20, pady=20, command=clear)
        else:
            button = tk.Button(root, text=text, padx=20, pady=20, command=lambda symbol=text: button_click(symbol))
        button.grid(row=row, column=col)

    root.mainloop()

