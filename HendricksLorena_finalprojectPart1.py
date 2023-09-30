import tkinter as tk
from tkinter import *
from tkinter import ttk

class MainWindow(tk.Tk):
    def __init__(self, tumblerColors=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(width=400, height=300)
        self.title("Tumblers Customization Express")

        # Create a label to display instructions
        tumblerColors_label = tk.Label(self, text="Tumbler Colors:")
        tumblerColors.pack()

        # Create an entry widget for the user to enter the Chosen Color
        self.tumblerColors_entry = tk.Entry(self)
        self.tumblerColors_entry.pack()

        # Create a label to display instructions
        tumblerSize_label = tk.Label(self, text="Tumbler Size:")
        tumblerSize_label.pack()

        # Create an entry widget for the user to enter the Tumbler Size
        self.tumblerSize_entry = tk.Entry(self)
        self.tumblerSize_entry.pack()

        # Create a label to display instructions
        minPrice_label = tk.Label(self, text="Minimum Price:")
        minPrice_label.pack()

        # Create an entry widget for the user to enter the Minimum Price Wanted
        self.minPrice_entry = tk.Entry(self)
        self.minPrice_entry.pack()

        # Create a label to display instructions
        maxPrice_label = tk.Label(self, text="Maximum Price:")
        maxPrice_label.pack()

        # Create an entry widget for the user to enter the Maximum Price Wanted
        self.maxPrice_entry = tk.Entry(self)
        self.maxPrice_entry.pack()

        # Create a label to display instructions
        tumblerStyle_label = tk.Label(self, text="Tumbler Style:")
        tumblerStyle_label.pack()

        # Create an entry widget for the user to enter the Tumbler Style Wanted
        self.tumblerStyle_entry = tk.Entry(self)
        self.tumblerStyle_entry.pack()

        # Create a label to display instructions
        tumblerLid_label = tk.Label(self, text="Tumbler Style Lids:")
        tumblerLid_label.pack()

        # Create an entry widget for the user to enter the Tumbler Lid Style Wanted
        self.tumblerLid_entry = tk.Entry(self)
        self.tumblerLid_entry.pack()

        # Create a label to display instructions
        tumblerWriting_label = tk.Label(self, text="Tumbler Writing Customization:")
        tumblerWriting_label.pack()

        # Create an entry widget for the user to enter the Writing Wanted on the Tumbler
        self.tumblerWriting_entry = tk.Entry(self)
        self.tumblerWriting_entry.pack()

        # Create a label to display instructions
        tumblerPhoto_label = tk.Label(self, text="Tumbler Photo Customization:")
        tumblerPhoto_label.pack()

        # Create an entry widget for the user to enter the Tumbler Photo Customization Tool
        self.tumblerPhoto_entry = tk.Entry(self)
        self.tumblerPhoto.pack()

        # Create a button to trigger the second window to open
        self.convert_button = tk.Button(self, text="Next", command=self.open_secondary_window)
        self.convert_button.pack()

    def open_secondary_window(self):
        # Create secondary (or popup) window.
        newWindow = tk.Toplevel()
        newWindow.title("Secondary Window")
        newWindow.config(width=300, height=200)

        # Create a label to display instructions
        name_label = tk.Label(newWindow, text="Name:")
        name_label.pack()

        # Create an entry widget for the user to enter name
        self.name_entry = tk.Entry(newWindow)
        self.name_entry.pack()

        # Create a label to display instructions
        email_label = tk.Label(newWindow, text="Email:")
        email_label.pack()

        # Create an entry widget for the user to enter email
        self.email_entry = tk.Entry(newWindow)
        self

        # Create a label to display instructions
        address_label = tk.Label(newWindow, text="Address:")
        address_label.pack()

        # Create an entry widget for the user to enter Address
        self.address_entry = tk.Entry(newWindow)
        self.address_entry.pack()

        # Create a label to display instructions
        paymentInfo_label = tk.Label(newWindow, text="Payment Info:")
        paymentInfo_label.pack()

        # Create an entry widget for the user to enter Payment Info for Purchase
        self.paymentInfo_entry = tk.Entry(newWindow)
        self.paymentInfo_entry.pack()

        # Run the main loop
        mainloop()
