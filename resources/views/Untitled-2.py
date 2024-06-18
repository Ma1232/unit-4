import tkinter
import tkinter.ttk

root= tkinter.Tk()

tkinter.Button(root).pack()
tkinter.Label(root).pack()
m= tkinter.ttk.Frame(root).pack()

root.title('m')
root.geometry('1900x50')
root.resizable(False,False)

root.mainloop()
