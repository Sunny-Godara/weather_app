Localized Weather Application 🌤️💨

A lightweight, clean Python command-line utility that fetches real-time meteorological data. The application utilizes a multi-stage API integration process to resolve geographical coordinates before mapping current weather conditions.

🚀 Features

Dual-API Workflow: Integrates the Open-Meteo Geocoding API to dynamically translate text-based city names into exact latitude/longitude coordinates, passing them seamlessly to the Forecast API.

Real-Time Parameters: Parses and extracts real-time temperatures, wind speeds, and relative humidity.

Modular Architecture: Isolates API routing and base service endpoints into a dedicated local config.py module to preserve code cleanliness and separation of concerns.

🛠️ Tech Stack & Dependencies

Language: Python 3

Libraries: urllib.request, urllib.parse, json (All standard built-in Python modules—no external pip installations required!)

💻 How To Run

Clone the repository.

Run the application:

python3 weather_app.py


Enter any city name when prompted to pull instant atmospheric diagnostics.
