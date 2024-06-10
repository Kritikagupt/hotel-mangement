import tkinter as tk
from tkinter import Button, Frame, ttk, RIDGE

class cust_win:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+250")
        
         




if __name__ == "__main__":
    root = tk.Tk()
    app = cust_win(root)
    root.mainloop()     