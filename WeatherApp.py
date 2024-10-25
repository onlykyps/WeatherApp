from tkinter import *
import tkinter as tk
from geopy.geocoders import nominatim
from timezonefinder import timezonefinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk

root = Tk()
root.title("Weather App")
root.geometry("890x470+300+300")
root.configure(bg="#57adff")
root.resizable(False, False)

#Icon
image_icon = PhotoImage(file="Images/logo.png")
root.iconphoto(False, image_icon)

#Labels
label1 = Label(root, text="Temperature",
               font=("Helvetica", 11),
               fg="white",
               bg="#203243")
label1.place(x=50, y=120)

label2 = Label(root, text="Humidity",
               font=("Helvetica", 11),
               fg="white",
               bg="#203243")
label2.place(x=50, y=140)

label3 = Label(root, text="Pressure",
               font=("Helvetica", 11),
               fg="white",
               bg="#203243")
label3.place(x=50, y=160)

label4 = Label(root, text="Wind Speed",
               font=("Helvetica", 11),
               fg="white",
               bg="#203243")
label4.place(x=50, y=180)

label5 = Label(root, text="Description",
               font=("Helvetica", 11),
               fg="white",
               bg="#203243")
label5.place(x=50, y=200)

Round_box = PhotoImage(file="Images/RoundRect_1.png")

#search box
Search_image = PhotoImage(file="Images/RoundRect_3.png")
my_image = Label(image=Search_image, bg="#57adff")
my_image.place(x=270,y=120)

weat_image = PhotoImage(file="Images/cloud.png")
weather_image = Label(root, image=weat_image, bg="#203243")
weather_image.place(x=290, y=127)

text_field = Entry(root, justify="center",
                   width=15, font=("poppins", 25, "bold"),
                   bg="#203243", border=0, fg="white")
text_field.place(x=370, y=130)
text_field.focus()

Search_icon = PhotoImage(file="Images/looking_glass.png")
my_image_icon = Button(image=Search_icon, borderwidth=0, cursor='hand2', bg="#203243")
my_image_icon.place(x=645, y=125)

mainloop()

