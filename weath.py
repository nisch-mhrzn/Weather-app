import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime, timedelta
import requests
import json




class WeatherApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Weather App")
        self.create_widgets()

    def create_widgets(self):
        # City input field
        self.city_label = ttk.Label(self.master, text="City:")
        self.city_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.city_entry = ttk.Entry(self.master, width=30)
        self.city_entry.grid(row=0, column=1, padx=5, pady=5)

        # Country code input field
        self.country_label = ttk.Label(self.master, text="Country Code:")
        self.country_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.country_entry = ttk.Entry(self.master, width=30)
        self.country_entry.grid(row=1, column=1, padx=5, pady=5)

        # Get Weather button
        self.get_weather_button = ttk.Button(self.master, text="Get Weather", command=self.get_weather)
        self.get_weather_button.grid(row=2, column=0, padx=5, pady=5, columnspan=2)

        # Weather info label
        self.weather_info_label = ttk.Label(self.master, text="", font=("Arial", 12), wraplength=400)
        self.weather_info_label.grid(row=3, column=0, padx=5, pady=5, columnspan=2)

    def get_weather(self):
        # Get user input for city and country code
        city = self.city_entry.get()
        country_code = self.country_entry.get()

        # Check if input fields are empty
        if not city or not country_code:
            messagebox.showerror("Error", "Please enter city and country code.")
            return

        # Call weather API
        api_key = "cb5c253ceb606f06d1b58d6666888dc5" #generate this form the api.openweathermap.org
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&appid={api_key}&units=metric"
        response = requests.get(url)

        # Check if API call was successful
        if response.status_code != 200:
            messagebox.showerror("Error", "Failed to retrieve weather information.")
            return

        # Parse JSON response
        data = json.loads(response.text)

        # Format weather info
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"].capitalize()
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        sunrise_time = datetime.fromtimestamp(data["sys"]["sunrise"]).strftime("%I:%M %p")
        sunset_time = datetime.fromtimestamp(data["sys"]["sunset"]).strftime("%I:%M %p")

        weather_info = f"Temperature: {temperature}°C\nDescription: {description}\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s\nSunrise: {sunrise_time}\nSunset: {sunset_time}"
        self.weather_info_label.configure(text=weather_info)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('800x500')
    app = WeatherApp(master=root)
    app.mainloop()
