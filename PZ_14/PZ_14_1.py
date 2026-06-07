
# Вариант 33  https://i.stack.imgur.com/px0jW.png

from tkinter import *
from tkinter import ttk

def submit_form():
    print("--- Отправленные данные ---")
    print("Requester:", requester.get())
    print("Short Name:", short.get())
    print("Email:", email.get())
    print("Organization:", org.get())
    print("Country:", country.get())
    print("IPv4 Address:", ip.get())
    print("Hostname:", host.get())
    print("FQDN:", fqdn.get())
    print("Description:", desc.get("1.0", END).strip())


root = Tk()
root.title("Certificate Self Service Portal")
root.geometry("680x700")
root.resizable(False, False)
root.configure(bg="#f4f4f4")

style = ttk.Style()
style.theme_use("clam")
style.configure("Custom.TCombobox", padding=3)
style.configure("Custom.TButton", font=("Arial", 10, "bold"), background="#337ab7", foreground="white")
style.map("Custom.TButton", background=[("active", "#286090")])


FONT_LABEL = "Arial 10 bold"
FONT_ENTRY = "Arial 10"
COLOR_BG = "#f4f4f4"
COLOR_FG = "#333333"


title_lbl = Label(root, text="Certificate Self Service Portal", font="Arial 24", bg=COLOR_BG, fg=COLOR_FG)
title_lbl.grid(row=0, column=0, columnspan=2, sticky=W, padx=30, pady=(20, 2))


subtitle_lbl = Label(root, text="Fill out the form to get a certificate.", font="Arial 10", bg=COLOR_BG, fg="#555555")
subtitle_lbl.grid(row=1, column=0, columnspan=2, sticky=W, padx=30, pady=(0, 20))


Label(root, text="Requester", font=FONT_LABEL, bg=COLOR_BG, fg=COLOR_FG).grid(row=2, column=0, sticky=E, padx=(30, 15), pady=6)
requester = Entry(root, font=FONT_ENTRY, width=45, bd=1, relief="solid")
requester.insert(0, "firstname lastname")
requester.grid(row=2, column=1, sticky=W, ipady=3)


Label(root, text="Short Name", font=FONT_LABEL, bg=COLOR_BG, fg=COLOR_FG).grid(row=3, column=0, sticky=E, padx=(30, 15), pady=6)
short = Entry(root, font=FONT_ENTRY, width=45, bd=1, relief="solid")
short.insert(0, "asdf")
short.grid(row=3, column=1, sticky=W, ipady=3)


Label(root, text="Email", font=FONT_LABEL, bg=COLOR_BG, fg=COLOR_FG).grid(row=4, column=0, sticky=E, padx=(30, 15), pady=6)
email = Entry(root, font=FONT_ENTRY, width=45, bd=1, relief="solid")
email.insert(0, "mail@mail.com")
email.grid(row=4, column=1, sticky=W, ipady=3)


Label(root, text="Organization", font=FONT_LABEL, bg=COLOR_BG, fg=COLOR_FG).grid(row=5, column=0, sticky=E, padx=(30, 15), pady=6)
org = Entry(root, font=FONT_ENTRY, width=45, bd=1, relief="solid")
org.insert(0, "Organization")
org.grid(row=5, column=1, sticky=W, ipady=3)


Label(root, text="Country", font=FONT_LABEL, bg=COLOR_BG, fg=COLOR_FG).grid(row=6, column=0, sticky=E, padx=(30, 15), pady=6)
country = ttk.Combobox(root, values=["Austria", "Россия", "Россия", "Russia"], style="Custom.TCombobox", width=42)
country.set("Austria")
country.grid(row=6, column=1, sticky=W)


Label(root, text="IPv4 Address", font=FONT_LABEL, bg=COLOR_BG, fg=COLOR_FG).grid(row=7, column=0, sticky=E, padx=(30, 15), pady=6)
ip = Entry(root, font=FONT_ENTRY, width=45, bd=1, relief="solid")
ip.insert(0, "127.0.0.1")
ip.grid(row=7, column=1, sticky=W, ipady=3)


Label(root, text="Hostname", font=FONT_LABEL, bg=COLOR_BG, fg=COLOR_FG).grid(row=8, column=0, sticky=E, padx=(30, 15), pady=6)
host = Entry(root, font=FONT_ENTRY, width=45, bd=1, relief="solid")
host.insert(0, "host")
host.grid(row=8, column=1, sticky=W, ipady=3)


Label(root, text="FQDN", font=FONT_LABEL, bg=COLOR_BG, fg=COLOR_FG).grid(row=9, column=0, sticky=E, padx=(30, 15), pady=6)
fqdn = Entry(root, font=FONT_ENTRY, width=45, bd=1, relief="solid")
fqdn.insert(0, "host.domain.tld")
fqdn.grid(row=9, column=1, sticky=W, ipady=3)


Label(root, text="Description", font=FONT_LABEL, bg=COLOR_BG, fg=COLOR_FG).grid(row=10, column=0, sticky=NE, padx=(30, 15), pady=6)
desc = Text(root, font=FONT_ENTRY, width=45, height=5, bd=1, relief="solid", wrap=WORD)
desc.insert(1.0, "desc")
desc.grid(row=10, column=1, sticky=W, pady=4)


submit_btn = ttk.Button(root, text="Submit Form", style="Custom.TButton", command=submit_form)
submit_btn.grid(row=11, column=1, sticky=W, pady=(15, 0), ipady=3)


root.mainloop()


