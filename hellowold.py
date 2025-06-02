from tkinter import *

class cqalculating:
    def __init__(self, root):
        self.root = root
        self.root.title("CATculator")
        self.root.resizable(0, 0)

        self.output_var = StringVar()

        self.create_widgets()

    def create_widgets(self):
        # enetry 
        self.entry1 = Entry(self.root, justify=CENTER)
        self.entry1.pack(fill=X, ipady=10)

        # middle
        label_plus = Label(self.root, font="Arial 15 bold", text="AND...?")
        label_plus.pack()

        # Entry for second number
        self.entry2 = Entry(self.root, justify=CENTER)
        self.entry2.pack(fill=X, ipady=10)

        # sepreation
        label_line = Label(self.root, font="Arial 15 bold", text="-----------------------------")
        label_line.pack()

        # outputting
        output_label = Label(self.root, font="Arial 20 bold", textvariable=self.output_var)
        output_label.pack()

        # Buttons
        button_add = Button(self.root, text="Add", width=10, command=self.add_numbers)
        button_add.pack(side=LEFT, ipady=10, padx=10, pady=10)

        button_multiply = Button(self.root, text="mlitply", width=10, command=self.multioply_numbers)
        button_multiply.pack(side=LEFT, ipady=10, padx=10, pady=10)

        button_print = Button(self.root, text="Print", width=10, command=self.print_text)
        button_print.pack(side=LEFT, ipady=10, padx=10, pady=10)

        button_reset = Button(self.root, text="Reset", width=10, command=self.reset_fields)
        button_reset.pack(side=LEFT, ipady=10, padx=10, pady=10)

        button_quit = Button(self.root, text="Quit", width=10, command=self.quit_app)
        button_quit.pack(side=LEFT, ipady=10, padx=10, pady=10)

    def quit_app(self):
        self.root.destroy()

    def print_text(self):
        self.output_var.set("Hello, world!")

    def add_numbers(self):
        try:
            num1 = float(self.entry1.get())
            num2 = float(self.entry2.get())
            result = num1 + num2
            self.output_var.set(f"Result: {result}")
        except ValueError:
            self.output_var.set("Invalid input!")

    def multioply_numbers(self):
        try:
            num1 = float(self.entry1.get())
            num2 = float(self.entry2.get())
            result = num1 * num2
            self.output_var.set(f"Result: {result}")
        except ValueError:
            self.output_var.set("Invalid input!")

    def reset_fields(self):
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.output_var.set("")


if __name__ == "__main__":
    root = Tk()
    app = cqalculating(root)
    root.mainloop()