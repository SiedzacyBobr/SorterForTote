import tkinter as tk
from tkinter import E, W, CENTER, ttk
from Route_dict import route_dict
from Colour_dict import colour_dict
from Time_dict import time_dict
from Route_direct import route_direct
from Booking import booking, keysbooking
from Route_mix import route_mix
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

        frame5 = ThereIsNoSuchNumber(container_label, self, padding=(7, 7))
        frame5.grid(column=0, row=2, sticky="S")

        frame4 = TransferToDirectDepartment(container_label, self, padding=(7, 7), )
        frame4.grid(column=0, row=2, sticky="S")

        frame3 = LabelOnConteiner(container_label, self, padding=(7, 7), )
        frame3.grid(column=0, row=2, sticky="EW")

        self.frames[TransferToDirectDepartment] = frame4
        self.frames[ThereIsNoSuchNumber] = frame5
        self.frames[LabelOnConteiner] = frame3

        self.bind("<Return>", frame3.start_input)
        self.bind("<KP_Enter>", frame3.start_input)

    def show_frames(self, container_label):
        container_frame = self.frames[container_label]
        container_frame.tkraise()


class HelloUsers(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.helo_user = ttk.Frame(self)
        self.helo_user.pack()

        self.text_in_hello = "To aplikacja rozszyfrowująca nr skrzynki transportowej w centrum dystrybucji." \
                             "\n każda skrzynka to zakupy dokonane przez klienta. " \
                             "\n program podaje przewoźnika i czas odjazdu"

        self.label_hello = tk.Label(self.helo_user, text=self.text_in_hello, font=('Non Sans', 14, 'normal'),)
        self.label_hello.pack()


class LabelOnConteiner(ttk.Frame):
    def __init__(self, container_label, controller, *args, **kwargs):
        super().__init__(container_label, *args, **kwargs)

        self.first_cell = ttk.Frame(self)
        self.first_cell.pack(side="top")


        self.title_input = ttk.Label(self.first_cell, text="7 cyfrowy numer skrzynki: ")
        self.title_input.pack(pady=7, padx=7, side="left")

        self.in_the_window = tk.StringVar()
        self.window_input = ttk.Entry(self.first_cell, width=7, textvariable=self.in_the_window, font=("Segoe UI", 10))
        self.window_input.pack(pady=7, padx=7, side="left")

        self.one_cell = ttk.Frame(self)
        self.one_cell.pack(ipady=16, ipadx=50,fill="both", expand=True)

        self.colour = tk.StringVar()

        self.carrier = tk.StringVar(value="Przewoźnik")
        self.prepared_on_time = tk.StringVar(value="Przesyłka gotowa na: ")
        self.purchase_invoice = tk.StringVar(value="Czy wystawić fakturę?")
        self.number_booking = tk.StringVar(value="booking")
        self.destination_country = tk.StringVar(value="Do jakiego kraju?")

        self.show_carrier = ttk.Label(self.one_cell, borderwidth=1, relief='solid', background="gray", anchor=CENTER, textvariable=self.carrier,)
        self.show_carrier.pack(side="left",)

        self.show_time = ttk.Label(self.one_cell, borderwidth=1, relief='solid', background="gray", anchor=CENTER, textvariable=self.prepared_on_time, )
        self.show_time.pack(side="left",)

        self.show_invoice = ttk.Label(self.one_cell, borderwidth=1, relief='solid', background="gray", anchor=CENTER, textvariable=self.purchase_invoice, )
        self.show_invoice.pack(side="top", )

        self.show_booking = ttk.Label(self.one_cell, borderwidth=1, relief='solid', background="gray", anchor=CENTER, textvariable=self.number_booking, )
        self.show_booking.pack(side="left",)

        self.show_country = ttk.Label(self.one_cell, borderwidth=1, relief='solid', background="gray", anchor=CENTER, textvariable=self.destination_country, )
        self.show_country.pack(side="left", )

        for child in self.one_cell.winfo_children():
            child.pack_configure(ipadx=20, ipady=20, fill='both', expand=True,)


    def start_input(self, *args, **kwargs):

        self.number_tote = self.in_the_window.get()
        if (len(self.number_tote)) == 7:

            self.index_route_mix = int(self.number_tote[2:4])
            self.routkey = route_mix[self.index_route_mix]

            self.index_booking = int(self.number_tote[3])
            self.key_booking = keysbooking[self.index_booking]

            if self.routkey in route_direct:
                print(f"Ta Rootka na directy {self.routkey}")

                root.show_frames(TransferToDirectDepartment)

            elif self.routkey[:3] in route_dict.keys():
                print(f'To jest normalna rootka {self.routkey}')

                self.carrier.set(route_dict[self.routkey[:3]])
                self.colour.set(colour_dict[self.carrier.get()])
                self.prepared_on_time.set(time_dict[self.carrier.get()])
                self.purchase_invoice.set("TAK wystawiamy Fakturę!" if self.routkey[-1:] == "1" else "BEZ Faktury!")
                self.number_booking.set(self.key_booking)
                self.destination_country.set(booking[self.key_booking])

                print(f'To jest color po zmianie {self.colour.get()}')

                self.show_carrier.config(background=self.colour.get(), foreground="White" if self.colour.get() == "Blue" else "Black")
                self.show_time.config(background=self.colour.get(), foreground="White" if self.colour.get() == "Blue" else "Black")
                self.show_invoice.config(background=self.colour.get(), foreground="White" if self.colour.get() == "Blue" else "Black")
                self.show_booking.config(background=self.colour.get(), foreground="White" if self.colour.get() == "Blue" else "Black")
                self.show_country.config(background=self.colour.get(), foreground="White" if self.colour.get() == "Blue" else "Black")

                root.show_frames(LabelOnConteiner)

            else:
                print(f"to jest żadna rootka")

                root.show_frames(ThereIsNoSuchNumber)


class TransferToDirectDepartment(ttk.Frame):
    def __init__(self, container_label, controller, *args, **kwargs):
        super().__init__(container_label, *args, **kwargs)

        self.move_to = ttk.Frame(self)
        self.move_to.pack()

        self.label_move_to_direct = tk.Label(self.move_to, text=f"Materiał przenieść \n do działu klineta VIP \n <==")
        self.label_move_to_direct.config(borderwidth=1, relief='solid',height=4, width=40,  background="green", font=("arial", 25, 'bold'), fg='white')
        self.label_move_to_direct.pack(fill='both', expand=True)


class ThereIsNoSuchNumber(ttk.Frame):
    def __init__(self, container_label, controller, *args, **kwargs):
        super().__init__(container_label, *args, **kwargs)

        self.no_number = ttk.Frame(self)
        self.no_number.pack()

        self.no_label_of_number = tk.Label(self.no_number, text=f"Brak takiej rootki w bazie danych")
        self.no_label_of_number.config(borderwidth=1, relief='solid', height=4, width=40,  background="Grey", font=("arial", 25, 'bold'), fg='Black',)
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
    style = ttk.Style(root)
    root.mainloop()
