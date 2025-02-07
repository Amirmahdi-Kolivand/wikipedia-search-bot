from tkinter import *
from tkinter import *
from tkinter import ttk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from deep_translator import GoogleTranslator
A=Tk()
A.geometry('1000x700')
A.title('wikinerd')
A.config(bg='sky blue')


lableH=Label(A,text='output:',bg='#E5FDFC',font=('bookman old style',20,'bold'),fg='#000033')
lableH.place(x=500,y=0)
textb=Text(height=10,width=60)
textb.place(x=500,y=40)


En=Entry(A,bg='black',fg='white',font=('bookman old style',18,'bold'))
En.place(x=350,y=300)
def search():
    enter=En.get()
    

        
    bro=webdriver.Chrome()
    
    bro.get('https://www.wikipedia.org/')

    c=bro.find_element('xpath','//*[@id="searchInput"]')
    c.click()
    c.send_keys(enter)
    c.send_keys(Keys.ENTER)
    h=bro.find_element('xpath','//*[@id="mw-content-text"]/div[1]/p[2]')
    t=h.text

    textb.delete('1.0', END)
    textb.insert(INSERT,t)
        
        
but1=Button(A,text='submit',font=('bookman old style',15,'bold'),width=35,command=lambda:search())
but1.place(x=300,y=400)
A.mainloop()