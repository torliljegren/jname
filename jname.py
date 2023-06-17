TRANSLATE = {
    "a":"ka",
    "b":"tu",
    "c":"mi",
    "d":"te",
    "e":"ku",
    "f":"ru",
    "g":"ji",
    "h":"re",
    "i":"ki",
    "j":"zu",
    "k":"me",
    "l":"ta",
    "m":"rin",
    "n":"to",
    "o":"mo",
    "p":"no",
    "q":"ke",
    "r":"shi",
    "s":"su",
    "t":"chi",
    "u":"do",
    "v":"ru",
    "w":"mei",
    "x":"na",
    "y":"fu",
    "z":"ze"
}

def translate(name: str) -> str:
    jname = list()
    for char in name.lower():
        if char == "å":
            char = "o"
        elif char == "ä":
            char = "e"
        elif char == "ö":
            char = "u"
        else:
            jname.append(TRANSLATE[char])
    return "".join(jname).capitalize()

if __name__ == "__main__":
    from tkinter import Tk, StringVar, END
    from tkinter.ttk import Frame, Button, Label, Entry
    from tkinter.messagebox import showerror


    def gui_translate(svar_in: StringVar, svar_out: StringVar, focus_on_wiget: Entry):
        name = svar_in.get()
        if not name.isalpha():
            showerror("Error", "Use letters only.")
            return
        svar_out.set(translate(name))
        focus_on_wiget.select_range(0, END)
        focus_on_wiget.focus_set()


    root = Tk()
    root.title("Japanese name")
    frame = Frame(root)

    namelabel = Label(frame, text="Name:")
    nameentryvar = StringVar(frame)
    nameentry = Entry(frame, textvariable=nameentryvar)

    jnamelabel = Label(frame, text="Translation:")
    jnameentryvar = StringVar(frame)
    jnameentry = Entry(frame, textvariable=jnameentryvar)

    okbutton = Button(frame, text="Translate", command=lambda: gui_translate(nameentryvar, jnameentryvar, nameentry))
    root.bind("<Return>", lambda x:okbutton.invoke())

    namelabel.grid(row=0, column=0, sticky='E', pady=(10,5), padx=(10,0))
    nameentry.grid(row=0, column=1, pady=(10,5), padx=(1,10))
    jnamelabel.grid(row=1, column=0, sticky='E', padx=(10,1))
    jnameentry.grid(row=1, column=1, pady=5, padx=(1,10))
    okbutton.grid(row=2, column=0, columnspan=2, pady=10)

    frame.pack()

    root.resizable(False, False)
    jnameentry.config(state="readonly")
    nameentry.focus_set()

    root.mainloop()






