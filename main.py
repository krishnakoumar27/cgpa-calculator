from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        sub1_var = float(sub1.get())
        sub2_var = float(sub2.get())
        sub3_var = float(sub3.get())
        sub4_var = float(sub4.get())
        sub5_var = float(sub5.get())
        sub6_var = float(sub6.get())
        sub7_var = float(sub7.get())

        credit1_var = float(credit1.get())
        credit2_var = float(credit2.get())
        credit3_var = float(credit3.get())
        credit4_var = float(credit4.get())
        credit5_var = float(credit5.get())
        credit6_var = float(credit6.get())
        credit7_var = float(credit7.get())

        total_credits = int(credit1_var + credit2_var + credit3_var + credit4_var + credit5_var + credit6_var + credit7_var)
        
        gpa.set(int((sub1_var * credit1_var) + (sub2_var * credit2_var) + (sub3_var * credit3_var) + (sub4_var * credit4_var) + (sub5_var * credit5_var) + (sub6_var * credit6_var) + (sub7_var * credit7_var))/total_credits)
    except ValueError:
        pass

root = Tk()
root.title("GPA Calculator")

mainframe = ttk.Frame(root, padding="160 160 160 160")
mainframe.grid(column=3, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

sub1 = StringVar()
sub1_entry = ttk.Entry(mainframe, width=7, textvariable=sub1)
sub1_entry.grid(column=1, row=1, sticky=(W, E))

sub2 = StringVar()
sub2_entry = ttk.Entry(mainframe, width=7, textvariable=sub2)
sub2_entry.grid(column=1, row=2, sticky=(W, E))

sub3 = StringVar()
sub3_entry = ttk.Entry(mainframe, width=7, textvariable=sub3)
sub3_entry.grid(column=1, row=3, sticky=(W, E))

sub4 = StringVar()
sub4_entry = ttk.Entry(mainframe, width=7, textvariable=sub4)
sub4_entry.grid(column=1, row=4, sticky=(W, E))

sub5 = StringVar()
sub5_entry = ttk.Entry(mainframe, width=7, textvariable=sub5)
sub5_entry.grid(column=1, row=5, sticky=(W, E))

sub6 = StringVar()
sub6_entry = ttk.Entry(mainframe, width=7, textvariable=sub6)
sub6_entry.grid(column=1, row=6, sticky=(W, E))

sub7 = StringVar()
sub7_entry = ttk.Entry(mainframe, width=7, textvariable=sub7)
sub7_entry.grid(column=1, row=7, sticky=(W, E))

credit1 = StringVar()
credit1_entry = ttk.Entry(mainframe, width=7, textvariable=credit1)
credit1_entry.grid(column=3, row=1, sticky=(W, E))

credit2 = StringVar()
credit2_entry = ttk.Entry(mainframe, width=7, textvariable=credit2)
credit2_entry.grid(column=3, row=2, sticky=(W, E))

credit3 = StringVar()
credit3_entry = ttk.Entry(mainframe, width=7, textvariable=credit3)
credit3_entry.grid(column=3, row=3, sticky=(W, E))

credit4 = StringVar()
credit4_entry = ttk.Entry(mainframe, width=7, textvariable=credit4)
credit4_entry.grid(column=3, row=4, sticky=(W, E))

credit5 = StringVar()
credit5_entry = ttk.Entry(mainframe, width=7, textvariable=credit5)
credit5_entry.grid(column=3, row=5, sticky=(W, E))

credit6 = StringVar()
credit6_entry = ttk.Entry(mainframe, width=7, textvariable=credit6)
credit6_entry.grid(column=3, row=6, sticky=(W, E))

credit7 = StringVar()
credit7_entry = ttk.Entry(mainframe, width=7, textvariable=credit7)
credit7_entry.grid(column=3, row=7, sticky=(W, E))


gpa = StringVar()
ttk.Label(mainframe, textvariable=gpa).grid(column=2, row=10, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=1, row=10, sticky=S)

ttk.Label(mainframe, text="Subject 1 Grade").grid(column=0, row=1, sticky=W)
ttk.Label(mainframe, text="Subject 2 Grade").grid(column=0, row=2, sticky=W)
ttk.Label(mainframe, text="Subject 3 Grade").grid(column=0, row=3, sticky=W)
ttk.Label(mainframe, text="Subject 4 Grade").grid(column=0, row=4, sticky=W)
ttk.Label(mainframe, text="Subject 5 Grade").grid(column=0, row=5, sticky=W)
ttk.Label(mainframe, text="Subject 6 Grade").grid(column=0, row=6, sticky=W)
ttk.Label(mainframe, text="Subject 7 Grade").grid(column=0, row=7, sticky=W)

ttk.Label(mainframe, text="credits ").grid(column=2, row=1, sticky=W)
ttk.Label(mainframe, text="credits ").grid(column=2, row=2, sticky=W)
ttk.Label(mainframe, text="credits ").grid(column=2, row=3, sticky=W)
ttk.Label(mainframe, text="credits ").grid(column=2, row=4, sticky=W)
ttk.Label(mainframe, text="credits ").grid(column=2, row=5, sticky=W)
ttk.Label(mainframe, text="credits ").grid(column=2, row=6, sticky=W)
ttk.Label(mainframe, text="credits ").grid(column=2, row=7, sticky=W)

#ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
#ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
#ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

sub1_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()