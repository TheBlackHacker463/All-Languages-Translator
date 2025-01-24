from tkinter import *
from tkinter import ttk, messagebox
from googletrans import LANGUAGES, Translator
from PIL import Image, ImageTk  # Import Pillow for better image support

# Create the main window
window = Tk()
window.title("All Languages Translator")
window.geometry("1080x400")
window.resizable(False, False)
window.configure(background="white")

# Function to update language labels
def label_change():
    c = combo1.get()
    c1 = combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    window.after(1000, label_change)

# Function to perform translation
def translate_now():
    try:
        text_ = text1.get(1.0, END).strip()
        if not text_:
            messagebox.showwarning("Warning", "Please enter text to translate!")
            return

        t1 = Translator()
        trans_text = t1.translate(text_, src=combo1.get(), dest=combo2.get())
        trans_text = trans_text.text

        text2.delete(1.0, END)
        text2.insert(END, trans_text)
    except Exception as e:
        messagebox.showerror("Error", f"Translation failed: {e}")

# Load images using Pillow
try:
    image_icon = ImageTk.PhotoImage(Image.open("C:/Users/SHC/Desktop/Translate/Abbas.png"))
    window.iconphoto(False, image_icon)

    arrow_icon = ImageTk.PhotoImage(Image.open("C:/Users/SHC/Desktop/Translate/arrow.png"))
    image_label = Label(window, image=arrow_icon, width=150)
    image_label.place(x=460, y=50)
except FileNotFoundError as e:
    messagebox.showerror("Error", f"Image file not found: {e}")

# Language options
languageV = list(LANGUAGES.values())

# Source language combobox
combo1 = ttk.Combobox(window, values=languageV, font="roboto 14", state="r")
combo1.place(x=110, y=20)
combo1.set("SELECT LANGUAGE")

label1 = Label(window, text="English", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label1.place(x=10, y=50)

# Destination language combobox
combo2 = ttk.Combobox(window, values=languageV, font="roboto 14", state="r")
combo2.place(x=730, y=20)
combo2.set("SELECT LANGUAGE")

label2 = Label(window, text="English", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label2.place(x=620, y=50)

# Input text frame
f = Frame(window, bg="black", bd=5)
f.place(x=10, y=118, width=440, height=210)

text1 = Text(f, font="roboto 20", bg="white", bd=5, relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=430, height=200)

scrollbar1 = Scrollbar(f)
scrollbar1.pack(side="right", fill='y')
scrollbar1.config(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# Output text frame
f1 = Frame(window, bg="black", bd=5)
f1.place(x=620, y=118, width=440, height=210)

text2 = Text(f1, font="roboto 20", bg="white", bd=5, relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=430, height=200)

scrollbar2 = Scrollbar(f1)
scrollbar2.pack(side="right", fill='y')
scrollbar2.config(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

# Translate button
translate = Button(window, text="TRANSLATE", font=("Roboto", 15), activebackground="white",
                   cursor="hand2", bd=1, width=10, height=2, bg="black", fg="white", command=translate_now)
translate.place(x=476, y=250)

# Start label update and main event loop
label_change()
window.mainloop()
