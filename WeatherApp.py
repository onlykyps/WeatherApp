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

mainloop()

