# Weather_Based Outfit Advisor (Flask Web App)

- A simple Flask web application that fetches real-time weather data using the Open-Meteo API and provides clothing recommendations based on temperature and wind conditions.

🚀 Features

- 🌍 Search weather by city name

- 🌡️ Fetch live temperature data

- 💨 Detect wind speed

- 👕 Smart outfit recommendations

- 🔌 Uses free Open-Meteo API (No API key required)

- 🌐 Simple and responsive web interface

🛠️ Tech Stack

- Python 3.x

- Flask

- Requests

- HTML (Jinja Templates)

- Open-Meteo API

⚙️ Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/your-username/weather-outfit-advisor.git
cd weather-outfit-advisor

2️⃣ Create Virtual Environment (Recommended)

python -m venv venv
venv\Scripts\activate   # On Windows

3️⃣ Install Dependencies

- pip install flask requests

Or if using requirements.txt:

- pip install -r requirements.txt

▶️ Run the Application

- python app.py

- Open your browser and go to:

http://127.0.0.1:5000/

🌦️ How It Works

- User enters a city name

- App uses Open-Meteo Geocoding API to get latitude & longitude

- Weather API fetches real-time temperature and wind speed

- Rule-based logic generates outfit recommendations

- Results displayed dynamically using Jinja templates

🧠 Outfit Logic

- ≥ 30°C → Light cotton clothes

- 20–29°C → Casual wear

- 10–19°C → Light jacket

- < 10°C → Heavy winter clothing

- Wind speed > 20 km/h → Wind-resistant clothing
