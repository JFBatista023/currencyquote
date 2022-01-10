from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import requests


def request_quotes():
    global quotes
    brl_usd = requests.get("https://economia.awesomeapi.com.br/last/BRL-USD").json()
    brl_eur = requests.get("https://economia.awesomeapi.com.br/last/BRL-EUR").json()
    usd_brl = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL").json()
    usd_eur = requests.get("https://economia.awesomeapi.com.br/last/USD-EUR").json()
    eur_brl = requests.get("https://economia.awesomeapi.com.br/last/EUR-BRL").json()
    eur_usd = requests.get("https://economia.awesomeapi.com.br/last/EUR-USD").json()
    quotes = [float(brl_usd["BRLUSD"]["bid"]), float(brl_eur["BRLEUR"]["bid"]),
              float(usd_brl["USDBRL"]["bid"]), float(usd_eur["USDEUR"]["bid"]),
              float(eur_brl["EURBRL"]["bid"]), float(eur_usd["EURUSD"]["bid"])]


def quote():
    try:
        if combo_first.get() == "Real" and combo_second.get() == "Dolar":
            label_second["text"] = "$ " + str(round(quotes[0] * float(entry.get()), 2))
        elif combo_first.get() == "Real" and combo_second.get() == "Euro":
            label_second["text"] = "€ " + str(round(quotes[1] * float(entry.get()), 2))
        elif combo_first.get() == "Dolar" and combo_second.get() == "Real":
            label_second["text"] = "R$ " + str(round(quotes[2] * float(entry.get()), 2))
        elif combo_first.get() == "Dolar" and combo_second.get() == "Euro":
            label_second["text"] = "€ " + str(round(quotes[3] * float(entry.get()), 2))
        elif combo_first.get() == "Euro" and combo_second.get() == "Real":
            label_second["text"] = "R$ " + str(round(quotes[4] * float(entry.get()), 2))
        elif combo_first.get() == "Euro" and combo_second.get() == "Dolar":
            label_second["text"] = "$ " + str(round(quotes[5] * float(entry.get()), 2))
        else:
            messagebox.showerror(title="Error", message="Invalid Currency")
    except ValueError:
        messagebox.showerror(title="Error", message="Invalid Value")


window = Tk()
window.title("Currency Quote")
window.geometry("500x300")
window.resizable(width=False, height=False)
window.config(bg="#73c706")

combo_first = Combobox(window, values=["Real", "Dolar", "Euro"], width=15,
                       justify=CENTER, font=("Arial 10 bold"))
combo_first.place(x=50, y=100, height=40)
combo_first.current(0)

combo_second = Combobox(window, values=["Real", "Dolar", "Euro"], width=15,
                        justify=CENTER, font=("Arial 10 bold"))
combo_second.place(x=320, y=100, height=40)
combo_second.current(1)

entry = Entry(window, width=15, justify=CENTER, font=("Arial 12 bold"), bg="#1d2e69", fg="#06cf6e")
entry.place(x=180, y=170, height=27)

label_first = Label(window, width=5, height=2, text="TO", bg=window["bg"],
                    justify=CENTER, font=("Arial 18 bold"), fg="#1c1fd4")
label_first.place(x=208, y=90)

label_second = Label(window, text="No quotes", width=11,
                     justify=CENTER, font=("Arial 15 bold"), bg="#6f8783", fg="#06cf6e")
label_second.place(x=180, y=210, height=30)

label_third = Label(window, text="Enter a value:", width=14,
                    justify=CENTER, font=("Arial 12 bold"), bg="#1d2e69", fg="#06cf6e")
label_third.place(x=20, y=170, height=25)

label_fourth = Label(window, text="CURRENCY QUOTE", width=20,
                     justify=CENTER, font=("Arial 20 bold"), bg=window["bg"], fg="#1d2e69")
label_fourth.place(x=80, y=15, height=40)

button = Button(window, command=quote, width=14, text="Quote", font=("Arial 11 bold"),
                justify=CENTER, bg="#1d2e69", fg="#06cf6e", relief=RAISED, bd=3)
button.place(x=177, y=250, height=40)


if __name__ == "__main__":
    request_quotes()
    window.mainloop()
