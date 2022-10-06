import tkinter as tk
from tkinter import E, W, CENTER, ttk
from Route_dict import route_dict
from Colour_dict import colour_dict
from Time_dict import time_dict
from Route_direct import route_direct
from Booking import booking
import random
import tkinter.font as font

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

class WindowSortingInFPK(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Sortownik Toto in Final Packing")
        self.columnconfigure(0, weight=1)

        self.frames = dict()

        container_label = ttk.Frame(self)
        container_label.grid(column=0, row=2, sticky="EW")

        font.nametofont("TkDefaultFont").config(size=12)

        frame = HelloUsers(self, padding=(10,10))
        frame.grid(column=0, row=0, sticky="N")

        frame1 = SignatureMadeBy(self, padding=(2, 2))
        frame1.grid(column=0, row=6, sticky="ES")

        frame2 = InputToSorting(self, padding=(10, 10))
        frame2.grid(column=0, row=1, sticky="EW")

        frame5 = ThereIsNoSuchNumber(container_label, self, padding=(7, 7))
        frame5.grid(column=0, row=2, sticky="EW")

        frame4 = TransferToDirectDepartment(container_label, self, padding=(7, 7), )
        frame4.grid(column=0, row=2, sticky="EW")

        frame3 = LabelOnConteiner(container_label, self, padding=(7, 7), )
        frame3.grid(column=0, row=2, sticky="EW")

        self.frames[TransferToDirectDepartment] = frame4
        self.frames[ThereIsNoSuchNumber] = frame5
        self.frames[LabelOnConteiner] = frame3

        self.bind("<Return>", frame2.start_input)
        self.bind("<KP_Enter>", frame2.start_input)

    def show_frames(self, container_label):
        container_frame = self.frames[container_label]
        container_frame.tkraise()



class HelloUsers(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.helo_user = ttk.Frame(self)
        self.helo_user.pack()

        self.text_in_hello = "To jest prosty program \n pomocny w sortowaniu skrzynek "

        self.label_hello = tk.Label(self.helo_user, text=self.text_in_hello, font=('Bradley Hand ITC', 15, 'bold'),)
        self.label_hello.pack()


class LabelOnConteiner(ttk.Frame):
    def __init__(self, container_label, controller, *args, **kwargs):
        super().__init__(container_label, *args, **kwargs)

        self.one_cell = ttk.Frame(self)
        self.one_cell.pack(ipady=30, ipadx=50,fill="both", expand=True)

        self.carrier = tk.StringVar(name="Przewoźnik")
        self.colour = tk.StringVar(name="grey")
        self.prepared_on_time = tk.StringVar(name="Gotowe na godzinę")
        self.purchase_invoice = tk.StringVar(name="Czy fakturowane?")
        self.number_booking = tk.StringVar(name="Booking")
        self.destination_country = tk.StringVar(name="Do jakiego Kraju?")

        show_carrier = ttk.Label(self.one_cell, borderwidth=1, relief='solid',background=self.colour, anchor=CENTER, textvariable=self.carrier, )
        show_carrier.pack(side="left",)

        show_time = ttk.Label(self.one_cell, borderwidth=1, relief='solid',background=self.colour, anchor=CENTER, textvariable=self.prepared_on_time, )
        show_time.pack(side="left",)

        show_invoice = ttk.Label(self.one_cell, borderwidth=1, relief='solid', background=self.colour, anchor=CENTER, textvariable=self.purchase_invoice, )
        show_invoice.pack(side="top", )

        show_booking = ttk.Label(self.one_cell, borderwidth=1, relief='solid', background=self.colour, anchor=CENTER, textvariable=self.number_booking, )
        show_booking.pack(side="left",)

        show_country = ttk.Label(self.one_cell, borderwidth=1, relief='solid', background=self.colour, anchor=CENTER, textvariable=self.destination_country, )
        show_country.pack(side="left", )

        show_color = ttk.Label(self.one_cell, borderwidth=1, relief='solid', background=self.colour, anchor=CENTER, textvariable=self.colour, )
        show_color.pack(side="top",)


        def Zmiana_koloru_tla():
            show_color.config(background="green")
            print(self.colour)


        for child in self.one_cell.winfo_children():
            child.pack_configure(ipadx=20, ipady=20, fill='both', expand=True)

        zmiana_coloru = ttk.Button(self.one_cell, text="Zmiana_koloru",command=Zmiana_koloru_tla)
        zmiana_coloru.pack()

class InputToSorting(ttk.Frame,):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.first_cell = ttk.Frame(self)
        self.first_cell.pack(side="top")

        self.in_the_window = tk.StringVar()
        self.title_input = ttk.Label(self.first_cell, text="numer roonki: ")
        self.title_input.pack(side="left")

        self.window_input = ttk.Entry(self.first_cell, textvariable=self.in_the_window, font=("Segoe UI", 10))
        self.window_input.pack(side="left")

        self.carrier = tk.StringVar(name="Przewoźnik")
        self.colour = tk.StringVar(name="gray")
        self.prepared_on_time = tk.StringVar(name="Gotowe na godzinę")
        self.purchase_invoice = tk.StringVar(name="Czy fakturowane?")
        self.number_booking = tk.StringVar(name="Booking")
        self.destination_country = tk.StringVar(name="Do jakiego Kraju?")


    def start_input(self, *args):

        self.routkey = str(self.in_the_window.get())

        if self.routkey in route_direct:
            print(f"Ta Rootka na directy {self.routkey}")

            root.show_frames(TransferToDirectDepartment)

        elif self.routkey[:3] in route_dict.keys():
            print(f'To jest normalna rootka {self.routkey}')

            self.carrier.set(route_dict[self.routkey[:3]])
            self.colour.set(colour_dict[self.carrier.get()])
            self.prepared_on_time.set(time_dict[self.carrier.get()])
            self.purchase_invoice.set("TAK wystawiamy Fakturę!" if self.routkey[-1:] == "1" else "BEZ Faktury!")
            self.number_booking.set(random.choice(list(booking.keys())))
            self.destination_country.set(booking[self.number_booking.get()])

            # if self.colour != "grey":
            #     LabelOnConteiner.Zmiana_koloru_tła()

            root.show_frames(LabelOnConteiner)
        else:
            print(f"to jest żadna rootka")

            root.show_frames(ThereIsNoSuchNumber)


class TransferToDirectDepartment(ttk.Frame):
    def __init__(self, container_label, controller, *args, **kwargs):
        super().__init__(container_label, *args, **kwargs)

        self.move_to = ttk.Frame(self)
        self.move_to.pack()

        self.label_move_to_direct = tk.Label(self.move_to, text=f"Materiał przenieść \n do działu Direct \n <==")
        self.label_move_to_direct.config(borderwidth=1, relief='solid',height=5, width=50,  background="red", font=("arial", 25, 'bold'), fg='yellow')
        self.label_move_to_direct.pack(fill='both', expand=True)


class ThereIsNoSuchNumber(ttk.Frame):
    def __init__(self, container_label, controller, *args, **kwargs):
        super().__init__(container_label, *args, **kwargs)

        self.no_number = ttk.Frame(self)
        self.no_number.pack()

        self.no_label_of_number = tk.Label(self.no_number, text=f"Brak takiej rootki w bazie danych")
        self.no_label_of_number.config(borderwidth=1, relief='solid', height=5, width=50,  background="Grey", font=("arial", 25, 'bold'), fg='Black',)
        self.no_label_of_number.pack(fill='both', expand=True, )


class SignatureMadeBy(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.signature = ttk.Frame(self)
        self.signature.pack(side="bottom", fill="both",)

        self.label_signature = tk.Label(self.signature, text="made by KRWB ", font=('Bradley Hand ITC', 10, 'bold'))
        self.label_signature.pack(anchor=E)


if __name__ == "__main__":

    root = WindowSortingInFPK()
    root.mainloop()
