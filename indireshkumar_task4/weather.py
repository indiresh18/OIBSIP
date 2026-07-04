import requests

API_KEY = "261808b9d1d9e1a9e998dbb5f1f82344"  


def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url, timeout=10)
        data = response.json()


        if response.status_code == 404:
            print("❌ Error: City not found.")
            return

        if response.status_code != 200:
            print(f"❌ Error: Unable to fetch weather data. Status code: {response.status_code}")
            return

    
        

        temp_c = data["main"]["temp"]
        temp_f = (temp_c * 9 / 5) + 32
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"].title()
        wind_speed = data["wind"]["speed"]

        print("\n------ Weather Report ------")
        print(f"City: {data['name']}")
        print(f"Temperature: {temp_c:.2f} °C")
        print(f"Temperature: {temp_f:.2f} °F")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {description}")
        print(f"Wind Speed: {wind_speed} m/s")

    except requests.exceptions.Timeout:
        print("❌ Error: Request timed out.")

    except requests.exceptions.ConnectionError:
        print("❌ Error: No internet connection.")

    except Exception as e:
        print("❌ Unexpected Error:", e)


def main():
    city = input("Enter city name: ").strip()

    if city == "":
        print("❌ Error: City name cannot be empty.")
        return

    get_weather(city)


if __name__ == "__main__":
    main()