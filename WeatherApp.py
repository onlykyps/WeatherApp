from tkinter import *
import tkinter as tk

from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk

root = Tk()
root.title("Weather App")
root.geometry("890x470+300+300")
root.configure(bg="#57adff")
root.resizable(False, False)

# Icon
image_icon = PhotoImage(file="Images/logo.png")
root.iconphoto(False, image_icon)

# Labels
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

# search box
Search_image = PhotoImage(file="Images/RoundRect_3.png")
my_image = Label(image=Search_image, bg="#57adff")
my_image.place(x=270, y=120)

weat_image = PhotoImage(file="Images/cloud.png")
weather_image = Label(root, image=weat_image, bg="#203243")
weather_image.place(x=290, y=127)

text_field = Entry(root, justify="center",
                   width=15, font=("poppins", 25, "bold"),
                   bg="#203243", border=0, fg="white")
text_field.place(x=370, y=130)
text_field.focus()

Search_icon = PhotoImage(file="Images/looking_glass.png")


def getWeather():
    city = text_field.get()
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(city)

    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
    timezone.config(text=result)

    long_lat.config(text=f"{round(location.latitude, 4)}°N, "
                         f"{round(location.longitude, 1)}°E")
    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    clock.config(text=current_time)

    # api_one_call = ("https://api.openweathermap.org/data/2.5/onecall!lat=" +
    #         str(location.latitude) +
    #        "&lon=" + str(location.longitude) +
    #       "&units=metric&exclude=hourly" +
    #       "&appid={AIzaSyDaGmWKa4JsXZ-HjGw7ISLn_3namBGewQe}")  # NOT ACTUAL API KEY

    api = ("https://api.openweathermap.org/data/2.5/weather!lat=" +
           str(location.latitude) +
           "&lon=" + str(location.longitude) +
           "&appid={AIzaSyDaGmWKa4JsXZ-HjGw7ISLn_3namBGewQe}")  # NOT ACTUAL API KEY

    json_data = requests.get(api).json()
    # json_data_one_call = requests.get(api_one_call).json()

    # current

    temp = json_data['main']['temp']
    humidity = json_data['main']['humidity']
    pressure = json_data['main']['pressure']
    wind = json_data['main']['speed']
    description = json_data['main']['weather'][0]['description']

    # one call for Celsius

    # temp_one_call = json_data_one_call['current']['temp']
    # humidity_one_call = json_data_one_call['current']['humidity']
    # pressure_one_call = json_data_one_call['current']['pressure']
    # wind_one_call = json_data_one_call['current']['wind_speed']
    # description_one_call = json_data_one_call['current']['weather'][0]['description']

    t.config(text=(temp, "K"))
    h.config(text=(temp, "%"))
    p.config(text=(temp, "hPa"))
    w.config(text=(temp, "m/s"))
    d.config(text=description)

    # one call for Celsius

    # t_one_call.config(text=(temp, "C"))
    # h_one_call.config(text=(temp, "%"))
    # p_one_call.config(text=(temp, "hPa"))
    # w_one_call.config(text=(temp, "m/s"))
    # d_one_call.config(text=description)

    # first cell

    first_day_image = json_data['daily'][0]['weather'][0]['icon']
    print(first_day_image)
    photo_one = ImageTk.PhotoImage(file=f"icon/{first_day_image}")
    first_day_image.config(image=photo_one)
    first_image.image = photo_one

    temp_day_one = json_data['daily'][0]['temp']['day']
    temp_night_one = json_data['daily'][0]['temp']['night']

    day_one_temp.config(text=f"Day:{temp_day_one}\n Night:{temp_night_one}")

    # second cell

    second_day_image = json_data['daily'][1]['weather'][1]['icon']
    print(second_day_image)
    img = (Image.open(f"icon/{second_day_image}@2x.png"))
    resized_image = img.resize((50, 50))
    photo_two = ImageTk.PhotoImage(resized_image)
    second_day_image.config(image=photo_two)
    second_image.image = photo_two

    temp_day_two = json_data['daily'][1]['temp']['day']
    temp_night_two = json_data['daily'][1]['temp']['night']

    day_two_temp.config(text=f"Day:{temp_day_two}\n Night:{temp_night_two}")

    # third cell

    third_day_image = json_data['daily'][2]['weather'][2]['icon']
    print(third_day_image)

    img = (Image.open(f"icon/{second_day_image}@2x.png"))
    resized_image = img.resize((50, 50))

    photo_three = ImageTk.PhotoImage(resized_image)
    third_day_image.config(image=photo_three)
    third_image.image = photo_three

    temp_day_three = json_data['daily'][2]['temp']['day']
    temp_night_three = json_data['daily'][2]['temp']['night']

    day_two_temp.config(text=f"Day:{temp_day_three}\n Night:{temp_night_three}")

    # fourth cell

    fourth_day_image = json_data['daily'][3]['weather'][3]['icon']
    print(fourth_day_image)

    img = (Image.open(f"icon/{second_day_image}@2x.png"))
    resized_image = img.resize((50, 50))

    photo_fourth = ImageTk.PhotoImage(resized_image)

    fourth_day_image.config(image=photo_fourth)
    fourth_image.image = photo_fourth

    temp_day_four = json_data['daily'][3]['temp']['day']
    temp_night_four = json_data['daily'][3]['temp']['night']

    day_two_temp.config(text=f"Day:{temp_day_four}\n Night:{temp_night_four}")

    # fifth cell

    fifth_day_image = json_data['daily'][4]['weather'][4]['icon']
    print(fifth_day_image)

    img = (Image.open(f"icon/{second_day_image}@2x.png"))
    resized_image = img.resize((50, 50))

    photo_fifth = ImageTk.PhotoImage(resized_image)
    fifth_day_image.config(image=photo_fifth)
    fifth_image.image = photo_fifth

    temp_day_five = json_data['daily'][4]['temp']['day']
    temp_night_five = json_data['daily'][4]['temp']['night']

    day_two_temp.config(text=f"Day:{temp_day_five}\n Night:{temp_night_five}")

    # sixth cell

    sixth_day_image = json_data['daily'][5]['weather'][5]['icon']
    print(sixth_day_image)

    img = (Image.open(f"icon/{second_day_image}@2x.png"))
    resized_image = img.resize((50, 50))

    photo_sixth = ImageTk.PhotoImage(resized_image)
    sixth_day_image.config(image=photo_sixth)
    sixth_image.image = photo_sixth

    temp_day_six = json_data['daily'][5]['temp']['day']
    temp_night_six = json_data['daily'][5]['temp']['night']

    day_two_temp.config(text=f"Day:{temp_day_six}\n Night:{temp_night_six}")

    # seventh cell

    seventh_day_image = json_data['daily'][6]['weather'][6]['icon']
    print(seventh_day_image)

    img = (Image.open(f"icon/{second_day_image}@2x.png"))
    resized_image = img.resize((50, 50))

    photo_seventh = ImageTk.PhotoImage(resized_image)
    seventh_day_image.config(image=photo_seventh)
    seventh_image.image = photo_seventh

    temp_day_seven = json_data['daily'][6]['temp']['day']
    temp_night_seven = json_data['daily'][6]['temp']['night']

    day_two_temp.config(text=f"Day:{temp_day_seven}\n Night:{temp_night_seven}")

    # days

    first = datetime.now()
    day_1.config(text=first.strftime("%A"))

    second = first + timedelta(days=1)
    day_2.config(text=second.strftime("%A"))

    third = first + timedelta(days=2)
    day_3.config(text=third.strftime("%A"))

    forth = first + timedelta(days=3)
    day_4.config(text=forth.strftime("%A"))

    fifth = first + timedelta(days=4)
    day_5.config(text=fifth.strftime("%A"))

    sixth = first + timedelta(days=5)
    day_6.config(text=sixth.strftime("%A"))

    seventh = first + timedelta(days=6)
    day_7.config(text=seventh.strftime("%A"))


my_image_icon = Button(image=Search_icon, borderwidth=0, cursor='hand2', bg="#203243", command=getWeather())
my_image_icon.place(x=645, y=125)

# bottom boxes

frame = Frame(root, width=900, height=180, bg="#212120")
frame.pack(side=BOTTOM)

firstbox = PhotoImage(file="Images/RoundSq.png")
secondbox = PhotoImage(file="Images/RoundRect_2.png")

Label(frame, image=firstbox, bg="#212120").place(x=30, y=20)
Label(frame, image=secondbox, bg="#212120").place(x=300, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=400, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=500, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=600, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=700, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=800, y=30)

# clock

clock = Label(root, text="2:30pm", font=("Helvetica", 30, 'bold'), fg='white', bg='#57adff')
clock.place(x=30, y=20)

# timezone

timezone = Label(root, font=("Helvetica", 20), fg="white", bg="#57adff")
timezone.place(x=30, y=20)

long_lat = Label(root, font=("Helvetica", 20), fg="white", bg="#57adff")
long_lat.place(x=700, y=50)

t = Label(root, font=("Helvetica", 20), fg="white", bg="#203243")
t.place(x=150, y=120)

h = Label(root, font=("Helvetica", 20), fg="white", bg="#203243")
h.place(x=150, y=140)

p = Label(root, font=("Helvetica", 20), fg="white", bg="#203243")
p.place(x=150, y=160)

w = Label(root, font=("Helvetica", 20), fg="white", bg="#203243")
w.place(x=150, y=180)

d = Label(root, font=("Helvetica", 20), fg="white", bg="#203243")
d.place(x=150, y=200)

# one call for Celsius

# t_one_call = Label(root, font=("Helvetica", 20), fg="white", bg="#203243")
# t_one_call.place(x=150, y=120)
#
# h_one_call = Label(root, font=("Helvetica", 20), fg="white", bg="#203243")
# h_one_call.place(x=150, y=140)
#
# p_one_call = Label(root, font=("Helvetica", 20), fg="white", bg="#203243")
# p_one_call.place(x=150, y=160)
#
# w_one_call = Label(root, font=("Helvetica", 20), fg="white", bg="#203243")
# w_one_call.place(x=150, y=180)
#
# d_one_call = Label(root, font=("Helvetica", 20), fg="white", bg="#203243")
# d_one_call.place(x=150, y=200)

# first cell

first_frame = Frame(root, width=230, height=132, bg="#282829")
first_frame.place(x=35, y=315)

first_image = Label(first_frame, bg="282829")
first_image.place(x=1, y=15)

day_1 = Label(first_frame, font="arial 20", bg="#282829", fg="#fff")
day_1.place(x=100, y=5)

day_one_temp = Label(first_frame, bg="#282829", fg="#57adff", font="arial 15 bold")
day_one_temp.place(x=100, y=50)

# second cell

second_frame = Frame(root, width=70, height=15, bg="#282829")
second_frame.place(x=305, y=325)

second_image = Label(first_frame, bg="3282829")
second_image.place(x=7, y=20)

day_2 = Label(second_frame, font="arial 20", bg="#282829", fg="#fff")
day_2.place(x=100, y=5)

day_two_temp = Label(first_frame, bg="#282829", fg="#57adff", font="arial 15 bold")
day_two_temp.place(x=2, y=70)

# third cell

third_frame = Frame(root, width=70, height=15, bg="#282829")
third_frame.place(x=405, y=325)

day_3 = Label(third_frame, font="arial 20", bg="#282829", fg="#fff")
day_3.place(x=100, y=5)

third_image = Label(first_frame, bg="282829")
third_image.place(x=7, y=20)

day_three_temp = Label(first_frame, bg="#282829", fg="#57adff", font="arial 15 bold")
day_three_temp.place(x=2, y=70)

# fourth cell

fourth_frame = Frame(root, width=70, height=15, bg="#282829")
fourth_frame.place(x=505, y=325)

day_4 = Label(fourth_frame, font="arial 20", bg="#282829", fg="#fff")
day_4.place(x=100, y=5)

fourth_image = Label(first_frame, bg="282829")
fourth_image.place(x=7, y=20)

day_four_temp = Label(first_frame, bg="#282829", fg="#57adff", font="arial 15 bold")
day_four_temp.place(x=2, y=70)

# fifth cell

fifth_frame = Frame(root, width=70, height=15, bg="#282829")
fifth_frame.place(x=605, y=325)

day_5 = Label(fifth_frame, font="arial 20", bg="#282829", fg="#fff")
day_5.place(x=100, y=5)

fifth_image = Label(first_frame, bg="282829")
fifth_image.place(x=7, y=20)

day_five_temp = Label(first_frame, bg="#282829", fg="#57adff", font="arial 15 bold")
day_five_temp.place(x=2, y=70)

# sixth cell

sixth_frame = Frame(root, width=70, height=15, bg="#282829")
sixth_frame.place(x=705, y=325)

day_6 = Label(sixth_frame, font="arial 20", bg="#282829", fg="#fff")
day_6.place(x=100, y=5)

sixth_image = Label(first_frame, bg="282829")
sixth_image.place(x=7, y=20)

day_six_temp = Label(first_frame, bg="#282829", fg="#57adff", font="arial 15 bold")
day_six_temp.place(x=2, y=70)

# seventh cell

seventh_frame = Frame(root, width=70, height=15, bg="282829")
seventh_frame.place(x=805, y=325)

day_7 = Label(seventh_frame, font="arial 20", bg="#282829", fg="#fff")
day_7.place(x=100, y=5)

seventh_image = Label(first_frame, bg="282829")
seventh_image.place(x=7, y=20)

day_seven_temp = Label(first_frame, bg="#282829", fg="#57adff", font="arial 15 bold")
day_seven_temp.place(x=2, y=70)

mainloop()
