from pytube import YouTube
#import rsa
#import base64
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
#import images
import re
from PIL import Image, ImageTk
from tkinter.filedialog import askdirectory
import os

def downloadvideo(uuid,out_dir):
    k=uuid.get()
    d=out_dir.get()
    
    print(k)
    print(d)
    
    yt = YouTube(k)


    # To print title
    print("Title :", yt.title)
    
    d=d+"/"+"yourvideo"
    # To get number of views
    print("Views :", yt.views)
    # To get the length of video
    print("Duration :", yt.length)
    # To get description
    print("Description :", yt.description)
    # To get ratings
    print("Ratings :", yt.rating)

    stream = yt.streams.get_highest_resolution()
    stream.download(d)
    print("Download completed!!")
    messagebox.showinfo("Download","File downloaded Sucessfully")

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
        root.quit()


def ask_dir(entr):
    folder = askdirectory()
    print(folder)
    entr.delete(0,END)
    entr.insert(END,folder)
    #print(entr.insert(END,folder))




#current_machine_id = "4C4C4544-0056-5210-8047-C2C04F583330"
def gen_img(base64_img,file):
    img_data = base64.b64decode(base64_img)
    with open(file,"wb") as img:
        img.write(img_data)
        img.close()
    return file

ey_icon = "ey_icon.ico"
ey_logo = "ey_logo.png"

root = Tk()
root.wm_title("Youtube Donwloader")
root.iconbitmap(ey_icon)
root.minsize(300,100)


uuid_lbl = Label(root,text = "Youtube Link")
uuid =Entry(root,font = "Consolas 12",width = 40)

uuid_lbl.grid(row = 1, padx = 10 , pady = 10, column = 0, columnspan = 200,sticky = N+S+E+W)
uuid.grid(row = 1, padx = 10 , pady = 10, column = 3, columnspan = 8,sticky = N+S+E+W)
#print(uuid)
kpath= uuid.get()
print(kpath+"first")

out_dir_lbl = Label(root,text = "Save file to")
out_dir_lbl.grid(row = 3, padx = 10 , pady = 10, column = 0, columnspan = 2,sticky = N+S+E+W)
out_dir = Entry(root,font = "Consolas 12",width = "50")

out_dir.grid(row = 3, column = 3,padx = 10, pady = 10,columnspan = 150,sticky = N+S+E+W)
dir_browse = Button(root,text = "Browse",command = lambda:ask_dir(out_dir))
dir_browse.grid(row = 3, padx = 10, pady = 10, column = 20, columnspan = 3,sticky = N+S+E+W)

dpath=out_dir.get()
print(dpath+"second")

gen = Button(root,text = "Download",command = lambda:downloadvideo(uuid,out_dir))
gen.grid(row = 7, padx = 10, pady = 10, column = 3, columnspan = 15,sticky = N+S+E+W)

vSmallIco = (60, 60)
op = Image.open(ey_logo)
resized = op.resize(vSmallIco, Image.ANTIALIAS)
img = ImageTk.PhotoImage(resized)

panel = Label(root,image = img)
panel.grid(row = 16, padx = 20 , pady = 10, column = 0, columnspan = 3,sticky = N+S+E+W,rowspan =2)

copyright = "© Ankit"
cp_lbl = Label(root,text = copyright,)
cp_lbl.grid(row = 17, padx = 10 , pady = 10, column = 6, columnspan = 10,sticky = N+S+E+W)


root.protocol("WM_DELETE_WINDOW", on_closing)
root.resizable(False,False)

root.mainloop()
