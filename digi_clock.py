import random
import tkinter as tk
from datetime import datetime

window = tk.Tk()
current_time = datetime.now()
formattted = current_time.strftime("%I:%M %p")
a = 0.2
f = True


wd = window.winfo_screenwidth()
ht = window.winfo_screenheight()

print(wd, ht)

x = random.randint(0, wd - 500)
y = random.randint(0, ht - 500)

window.title("Digital Clock")
window.geometry("800x400")
window.attributes("-fullscreen", True)
window.attributes("-alpha", 1.0)
window.configure(bg="black")

as_labe = tk.Label(
    window,
    text=r"""

  __________
 / ___  ___ \
/ / @ \/ @ \ \
\ \___/\___/ /\
 \____\/____/||
 /     /\\\\\//
|     |\\\\\\
 \      \\\\\\
   \______/\\\\
    _||_||_

""",
    font=("Consolas", 25),
    fg="lime",
    bg="black",
)

as_labe.pack(expand=True)


label = tk.Label(
    window, text=formattted, font=("OCR A Extended", 150), fg="lime", bg="black"
)
label.place(x=x, y=y)


def esc_button(event):
    window.destroy()


window.bind("<Escape>", esc_button)


def animate():
    global f
    global a

    if f:
        a += 0.05
        if a > 1.0:
            f = False
    else:
        a -= 0.05
        if a <= 0.2:
            x = random.randint(0, wd - 1000)
            y = random.randint(0, ht - 500)
            label.place(x=x, y=y)
            f = True

    window.attributes("-alpha", a)

    window.after(100, animate)


def update_clock():
    current_time = datetime.now()
    formattted = current_time.strftime("%I:%M %p")

    label.config(text=formattted)
    window.after(1000, update_clock)


update_clock()
animate()
window.mainloop()
