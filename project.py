import tkinter as tk
from tkinter import Button, Frame, ttk, RIDGE  # Importing RIDGE constant for relief
from PIL import Image, ImageTk  # Correctly import Image and ImageTk
from urllib.request import urlopen  # Correctly import urlopen from urllib.request

class HotelManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")
        
        # Load and place the header image
        header_img_url = 'https://i.pinimg.com/736x/06/ae/a6/06aea60cb15b198a6f1a72e43b994012.jpg'
        with urlopen(header_img_url) as url:  
            header_img = Image.open(url) 
            header_img = header_img.resize((1550, 200), Image.LANCZOS)  
            self.header_photoimg = ImageTk.PhotoImage(header_img)  
        
        lbl_header = tk.Label(self.root, image=self.header_photoimg, bd=5, relief=RIDGE)
        lbl_header.place(x=0, y=0, width=1550, height=200) 

        # Add the title below the header image
        lbl_title = tk.Label(
            self.root,
            text="Coral Hotel",
            font=('Courier New', 40, 'bold'),  # Correct font specification
            bg='#311B92',  # Background color
            fg='#F5DEB3',  # Foreground color (wheat color)
            bd=4,
            relief='ridge'
        )
        lbl_title.place(x=0, y=200, width=1550, height=60)

        # Load and place the logo image below the title
        logo_img_url = 'https://i.pinimg.com/564x/ed/e7/ed/ede7ed3a665a32735decd34cd04d61fe.jpg'
        with urlopen(logo_img_url) as url:  
            logo_img = Image.open(url) 
            logo_img = logo_img.resize((230, 200), Image.LANCZOS)  
            self.logo_photoimg = ImageTk.PhotoImage(logo_img)  
        
        lbl_logo = tk.Label(self.root, image=self.logo_photoimg, bd=5, relief=RIDGE)
        # Placing logo below the title image with some spacing
        lbl_logo.place(x=0, y=0, width=230, height=200) 
        
        
        main_frame=Frame(self.root,bd=4,relief=RIDGE) 
        main_frame.place(x=0,y=260,width=1550,height=620)
        
        lbl_menu=tk.Label(main_frame,
                          text="Menu",
                          font=('Courier New', 20, 'bold'),  # Correct font specification
                          bg='#311B92',  # Background color
                          fg='#F5DEB3',  # Foreground color (wheat color)
                          bd=4,
                          relief='ridge'
                          )
        lbl_menu.place(x=0,y=0,width=230)
        
        
        btn_frame= Frame(main_frame,bd=5,relief=RIDGE)
        btn_frame.place(x=0,y=40,width=228,height=220)
        
        cust_btn=Button(btn_frame,
                           text="Customer",
                           width=22,
                           font=('Courier New', 14 ),  # Correct font specification
                           bg='#311B92',  # Background color
                           fg='#F5DEB3',  # Foreground color (wheat color)
                           bd=0,
                           cursor="hand2"
                        )
        cust_btn.grid(row=0,column=0,pady=1)
        
        room_btn=Button(btn_frame,
                           text="Room",
                           width=22,
                           font=('Courier New', 14 ),  # Correct font specification
                           bg='#311B92',  # Background color
                           fg='#F5DEB3',  # Foreground color (wheat color)
                           bd=0,
                           cursor="hand2"
                        )
        room_btn.grid(row=1,column=0,pady=1)
        
        detail_btn=Button(btn_frame,
                           text="Details",
                           width=22,
                           font=('Courier New', 14 ),  # Correct font specification
                           bg='#311B92',  # Background color
                           fg='#F5DEB3',  # Foreground color (wheat color)
                           bd=0,
                           cursor="hand2"
                        )
        detail_btn.grid(row=2,column=0,pady=1)
        
        report_btn=Button(btn_frame,
                           text="Report",
                           width=22,
                           font=('Courier New', 14 ),  # Correct font specification
                           bg='#311B92',  # Background color
                           fg='#F5DEB3',  # Foreground color (wheat color)
                           bd=0,
                           cursor="hand2"
                        )
        report_btn.grid(row=3,column=0,pady=1)
        
        Feedback_btn=Button(btn_frame,
                           text="FeedBack",
                           width=22,
                           font=('Courier New', 14 ),  # Correct font specification
                           bg='#311B92',  # Background color
                           fg='#F5DEB3',  # Foreground color (wheat color)
                           bd=0,
                           cursor="hand2"
                        )
        Feedback_btn.grid(row=4,column=0,pady=1)
        
        logout_btn=Button(btn_frame,
                           text="logout",
                           width=22,
                           font=('Courier New', 14 ),  # Correct font specification
                           bg='#311B92',  # Background color
                           fg='#F5DEB3',  # Foreground color (wheat color)
                           bd=0,
                           cursor="hand2"
                        )
        logout_btn.grid(row=5,column=0,pady=1)
        
        
        right_img_url = 'https://i.pinimg.com/564x/bc/cd/0c/bccd0cb7a8698496eb9ad06dcd3ebcf8.jpg'
        with urlopen(right_img_url) as url:  
            right_img = Image.open(url) 
            right_img = right_img.resize((1310, 590), Image.LANCZOS)  
            self.right_photoimg = ImageTk.PhotoImage(right_img)  
        
        lbl_right = tk.Label(main_frame, image=self.right_photoimg, bd=5, relief=RIDGE)
        # Placing logo below the title image with some spacing
        lbl_right.place(x=230, y=0, width=1310, height=590) 

if __name__ == "__main__":
    root = tk.Tk()
    app = HotelManagement(root)
    root.mainloop()
