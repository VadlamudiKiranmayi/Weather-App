import tkinter as tk
import requests
import time

def getWeather():
    city_input = city_entry.get()
    weather_api = "https://api.openweathermap.org/data/2.5/weather?q=" + city_input + "&appid=c1d4d7239011f2a0ce0ea3a7be452031"
    json_data = requests.get(weather_api).json()
    
    if 'main' in json_data and 'wind' in json_data and 'sys' in json_data and 'visibility' in json_data:
        latitude = json_data['coord']['lat']
        longitude = json_data['coord']['lon']
        temperature = int(json_data['main']['temp'] - 273.15)
        daily_high = int(json_data['main']['temp_max'] - 273.15)
        daily_low = int(json_data['main']['temp_min'] - 273.15)
        wind_speed = json_data['wind']['speed']
        wind_direction = json_data['wind']['deg']
        pressure = json_data['main']['pressure']
        visibility = json_data['visibility']
        sunrise = time.strftime("%I:%M:%S %p", time.gmtime(json_data['sys']['sunrise'] - 21600))
        sunset = time.strftime("%I:%M:%S %p", time.gmtime(json_data['sys']['sunset'] - 21600))
        
        weather_info = f"Coordinates: {latitude}, {longitude}\nCurrent Temperature: {temperature}°C\nDaily High: {daily_high}°C\nDaily Low: {daily_low}°C\nWind Speed: {wind_speed} m/s\nWind Direction: {wind_direction}°\nBarometric Pressure: {pressure} hPa\nVisibility: {visibility} meters\nSunrise: {sunrise}\nSunset: {sunset}"
        weather_label.config(text=weather_info)
    else:
        weather_label.config(text="City not found or data unavailable!")


root = tk.Tk()
root.geometry("400x500")
root.title("Weather App")


font_style = ("Arial", 12)
bg_color = "#f0f0f0"
text_color = "#000000"  
button_color = "#FFA500"  
button_text_color = "white"
heading_color = "#007bff"  


root.config(bg=bg_color)


city_label = tk.Label(root, text="Enter City:", font=font_style, bg=bg_color, fg=text_color)
city_label.pack(pady=10)

city_entry = tk.Entry(root, font=font_style)
city_entry.pack(pady=5)

get_weather_button = tk.Button(root, text="Get Weather", command=getWeather, font=font_style, bg=button_color, fg=button_text_color)
get_weather_button.pack(pady=10)

weather_label = tk.Label(root, font=font_style, wraplength=380, justify="left", bg=bg_color, fg=text_color)
weather_label.pack(pady=10)


weather_label.config(font=(font_style[0], font_style[1], 'bold'), fg=heading_color)
weather_label.config(justify="left")

root.mainloop()
