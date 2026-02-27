from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    outfit = []

    if request.method == "POST":
        city = request.form["city"]

        # Geocoding API
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
        geo_response = requests.get(geo_url).json()

        if "results" in geo_response:
            latitude = geo_response["results"][0]["latitude"]
            longitude = geo_response["results"][0]["longitude"]

            # Weather API
            weather_url = (
                f"https://api.open-meteo.com/v1/forecast?"
                f"latitude={latitude}&longitude={longitude}&current_weather=true"
            )
            weather_response = requests.get(weather_url).json()
            current = weather_response["current_weather"]

            temperature = current["temperature"]
            windspeed = current["windspeed"]

            # Outfit logic
            if temperature >= 30:
                outfit.append("Wear light cotton clothes")
            elif 20 <= temperature < 30:
                outfit.append("Wear comfortable casual clothes")
            elif 10 <= temperature < 20:
                outfit.append("Wear a light jacket or sweater")
            else:
                outfit.append("Wear heavy winter clothing")

            if windspeed > 20:
                outfit.append("Wear wind-resistant clothing")

            weather_data = {
                "city": city,
                "temperature": temperature,
                "windspeed": windspeed
            }
        else:
            outfit.append("City not found. Please try again.")

    return render_template("index.html", weather=weather_data, outfit=outfit)

if __name__ == "__main__":
    app.run(debug=True)
