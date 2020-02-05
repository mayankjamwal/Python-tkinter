from tkinter import *
import requests
sc = Tk()
sc.title("Air Quality Finder")
sc.iconbitmap('E:\D\python-GUI\\ninja.ico')
sc.geometry("500x100")

#token value : get that value by registering in http://aqicn.org/api/

def check():
    
    try:

        global label,label2,label3

        api_link = "https://api.waqi.info/feed/"+ country.get() +"/?token=value" #<----token value must be inserted !!!!!
        link = requests.get(api_link)
        aqi = link.json()
        index = aqi['data']['aqi']
        city = aqi['data']['city']['name']
        loc = aqi['data']['city']['geo']
        pm10 = aqi['data']['iaqi']['pm10']['v']
        co = aqi['data']['iaqi']['co']['v']

        if index > 0 and index <= 50:
            weather_color = "green"
        elif index > 50 and index <= 100:
            weather_color = "yellow"
        elif index > 100 and index <= 150:
            weather_color = "orange" 
        elif index > 150 and index <= 200:
            weather_color = "red"
        elif index > 200 and index <= 250:
            weather_color = "purple"
        elif index > 250 and index <= 300:
            weather_color = "maroon"        

        sc.configure(background=weather_color)
        label = Label(sc,text=city+" Air quality index:"+str(index),font=("helvetica",10),background=weather_color)
        label.grid(row=1,column=0,columnspan=3)
        label2 = Label(sc,text="Location Cordinates : "+str(loc),font=("helvetica",10),background=weather_color)
        label2.grid(row=2,column=0,columnspan=3)
        label3= Label(sc,text="Pm10 : "+ str(pm10)+ " Carbon Monoxide Level : "+ str(co)+"%",font=("helvetica",10),background=weather_color)
        label3.grid(row=3,column=0,columnspan=3)

        
    
            
    except Exception as e:
        aqi = "ERROR..."    
    
def clear_widget():

    label.grid_forget()
    label2.grid_forget()
    label3.grid_forget()

country = Entry(sc,width=35,borderwidth=5,bg='lightgrey')
country.grid(row=0,column=0,pady=2)

button = Button(sc,text="Check the AQI",padx=30,pady=2,bg='lightblue',fg='black',command=check)
button.grid(row=0,column=1)
button = Button(sc,text="Clear",padx=30,pady=2,bg='lightblue',fg='black',command=clear_widget)
button.grid(row=0,column=2)
sc.mainloop()