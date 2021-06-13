from tkinter import *
from tkinter import scrolledtext
import wikipedia
import pyperclip
from tkinter.filedialog import asksaveasfilename
import threading
import tkinter.messagebox as msg
import io

root= Tk()

def thread_2():
    t= threading.Thread(target=get_link)
    t.start()

def thread():
    t=threading.Thread(target=search)
    t.start()

def search():
    copy_button.config(text= "COPY TEXT")
    search_button.config(text= "SEARCHING....")
    result= wikipedia.page(topic.get())
    text_area.delete(0.0, END)
    ask= msg.askyesno(title="Show Wikipedia Article", message="DO YOU WANT TO SEE THE WHOLE WIKIPEDIA PAGE? OTHERWISE WE WILL"
                                                         "SHOW YOU ONLY THE SUMMARY")

    if ask:
        text_area.insert(END, f"********************{result.title}********************" + "\n")
        def content():
            text_area.insert(2.0, result.content)
        text_area.after(1000, content)
    else:
        text_area.insert(END, f"********************{result.title}********************" + "\n")
        text_area.insert(END, result.summary)
    search_button.config(text= "SEARCH")
def copy():
    copied_text=pyperclip.copy(text= text_area.get(1.0, END))
    copy_button.config(text= "COPIED")

def save():
    save_button.config(text= "SAVING...")
    save_file= asksaveasfilename(title= "Save file", filetypes= (("text file", "*.txt"),("all files",'*.*')))
    if save_file:
        with io.open(save_file, "w", encoding="utf-8") as f:
            content= text_area.get(1.0, END)
            f.write(content)
    save_button.config(text= "SAVE")

def get_link():
    result= wikipedia.page(topic.get())
    msg.showinfo(title="Page URL", message=f"PAGE URL: {result.url}")

root.geometry("500x500")
root.title("WIKIPEDIA SEARCH TOOL")

frame1= Frame(root).grid(row= 0)


topic= Entry(root, width= 45, font= ("Arial", 11, "bold"))
topic.grid(sticky= "w",ipady= 8, pady= 15, row= 1, padx= 10)

search_button=Button(root, text= "SEARCH",  bd= 1,bg= "deep sky blue", fg= "white",command= thread)
search_button.grid(sticky= "e",padx= 20,row= 1, ipady= 4, ipadx= 23)

text_area= scrolledtext.ScrolledText(root,width= 68, height= 23, font= ("Corbel", 10, "bold italic"))
text_area.grid(pady= 12, padx= 7)

copy_button = Button(root,  text= "COPY TEXT",  bd= 1,bg= "pale green", command= copy)
copy_button.grid(row= 33,sticky = "w", ipady= 5, padx= 10, ipadx= 20)

save_button = Button(root,  text= "SAVE", bd= 1,bg= "pale green", command= save)
save_button.grid(row= 33,sticky= "w", padx= 190, ipady= 5, ipadx= 20)

link_button = Button(root,  text= "GET ABSOLUTE LINK", bd= 1, bg= "pale green",command= thread_2)
link_button.grid(row= 33,sticky= "e", ipady= 5, ipadx= 20, padx= 20)

root.mainloop()
