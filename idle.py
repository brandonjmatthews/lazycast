import sys;


import Tk as Tk


from PIL import Image, ImageTk

root = None

def show_pin(current_pin):
    # create Tk canvas
    root = Tk.Tk();

    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    if w == 0 or h == 0:
        w = 1920
        h = 1080
    root.overrideredirect(1)
    root.geometry("%dx%d+0+0" % (w, h))
    root.focus_set()
    root.bind("<Escape>", lambda e: (e.widget.withdraw(), e.widget.quit()))
    canvas = Tk.Canvas(root, width=w, height=h)
    canvas.pack()
    canvas.configure(background='black')

    # load pilImage for background
    pilImage = Image.open("background.jpg")
    imgWidth, imgHeight = pilImage.size

    if imgWidth > w or imgHeight > h:
        ratio = min(w/imgWidth, h/imgHeight)
        imgWidth = int(imgWidth*ratio)
        imgHeight = int(imgHeight*ratio)
        pilImage = pilImage.resize((imgWidth,imgHeight), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(pilImage)
    imagesprite = canvas.create_image(w/2,h/2,image=image)
    
    text = "%s" % (current_pin)
    canvas.create_text(w-20, h-20, anchor=Tk.SE, text=text, fill="#fff", font=('Arial', 100, 'bold'))

    root.update()

def kill():
    if root is not None:
        root.destroy()

if __name__ == '__main__':
    pin = sys.argv[1]
    show_pin(pin)

