from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import random

app = Flask(__name__)

# Apply CORS to the Flask app
CORS(app, resources={r"/recommend": {"origins": "*"}})

rackets = [
    # Offensive Rackets
    {"name": "Yonex Astrox 99 Pro", "playStyle": "offensive", "price": 280},
    {"name": "Yonex Voltric Z-Force II", "playStyle": "offensive", "price": 270},
    {"name": "Victor Thruster K 9900", "playStyle": "offensive", "price": 220},
    {"name": "Li-Ning Aeronaut 9000", "playStyle": "offensive", "price": 250},
    {"name": "Yonex Astrox 88S", "playStyle": "offensive", "price": 260},
    {"name": "Victor Hypernano X 900X", "playStyle": "offensive", "price": 200},
    {"name": "Li-Ning 3D Calibar 900", "playStyle": "offensive", "price": 230},
    {"name": "Yonex Nanoray 900", "playStyle": "offensive", "price": 200},
    {"name": "Victor Jetspeed S10", "playStyle": "offensive", "price": 190},
    {"name": "Yonex Arcsaber 11 Pro", "playStyle": "offensive", "price": 250},
    {"name": "Yonex Astrox 77", "playStyle": "offensive", "price": 240},
    {"name": "Li-Ning Turbo Charging 75C", "playStyle": "offensive", "price": 210},
    {"name": "Victor DriveX 7K", "playStyle": "offensive", "price": 220},
    {"name": "Yonex Astrox 100 ZZ", "playStyle": "offensive", "price": 300},
    {"name": "Li-Ning Turbo X90-II", "playStyle": "offensive", "price": 180},

    # Defensive Rackets
    {"name": "Victor Brave Sword 12", "playStyle": "defensive", "price": 180},
    {"name": "Yonex Duora 10", "playStyle": "defensive", "price": 200},
    {"name": "Li-Ning Windstorm 72", "playStyle": "defensive", "price": 150},
    {"name": "Yonex Nanoray 10F", "playStyle": "defensive", "price": 70},
    {"name": "Victor DriveX 9X", "playStyle": "defensive", "price": 190},
    {"name": "Li-Ning Turbo Charging 75", "playStyle": "defensive", "price": 180},
    {"name": "Yonex Nanoflare 800", "playStyle": "defensive", "price": 240},
    {"name": "Victor Light Fighter 7400", "playStyle": "defensive", "price": 100},
    {"name": "Li-Ning Windstorm 500", "playStyle": "defensive", "price": 90},
    {"name": "Yonex Nanoflare 700", "playStyle": "defensive", "price": 210},
    {"name": "Yonex Nanoflare 555", "playStyle": "defensive", "price": 180},
    {"name": "Victor Arrow Speed 88", "playStyle": "defensive", "price": 140},
    {"name": "Li-Ning Aeronaut 6000D", "playStyle": "defensive", "price": 200},
    {"name": "Yonex Nanoray 20", "playStyle": "defensive", "price": 80},
    {"name": "Victor Auraspeed 50D", "playStyle": "defensive", "price": 170},

    # Balanced Rackets
    {"name": "Yonex Arcsaber 7", "playStyle": "balanced", "price": 200},
    {"name": "Victor Auraspeed 90K", "playStyle": "balanced", "price": 220},
    {"name": "Li-Ning G-Force 3600", "playStyle": "balanced", "price": 110},
    {"name": "Yonex Duora 77", "playStyle": "balanced", "price": 170},
    {"name": "Victor Thruster K330", "playStyle": "balanced", "price": 150},
    {"name": "Yonex Duora 88", "playStyle": "balanced", "price": 180},
    {"name": "Li-Ning 3D Calibar 600", "playStyle": "balanced", "price": 190},
    {"name": "Yonex Arcsaber 10", "playStyle": "balanced", "price": 210},
    {"name": "Victor Auraspeed 30H", "playStyle": "balanced", "price": 120},
    {"name": "Li-Ning Turbo Charging 70", "playStyle": "balanced", "price": 200},
    {"name": "Yonex Arcsaber 5", "playStyle": "balanced", "price": 160},
    {"name": "Victor Auraspeed 70F", "playStyle": "balanced", "price": 130},
    {"name": "Li-Ning Windstorm 78", "playStyle": "balanced", "price": 100},
    {"name": "Yonex Nanoray 60FX", "playStyle": "balanced", "price": 140},
    {"name": "Victor Brave Sword 11", "playStyle": "balanced", "price": 200},

    # Beginner-Friendly Rackets
    {"name": "Yonex GR 303", "playStyle": "balanced", "price": 30},
    {"name": "Li-Ning XP-90-IV", "playStyle": "balanced", "price": 40},
    {"name": "Victor Arrow Power 6000", "playStyle": "offensive", "price": 50},
    {"name": "Yonex Muscle Power 2", "playStyle": "balanced", "price": 35},
    {"name": "Li-Ning XP 60-II", "playStyle": "balanced", "price": 45},
    {"name": "Victor Starter Set 100", "playStyle": "defensive", "price": 60},
    {"name": "Yonex ZR 100", "playStyle": "balanced", "price": 25},
    {"name": "Li-Ning XP 70-II", "playStyle": "offensive", "price": 50},
    {"name": "Victor Power Series 50", "playStyle": "balanced", "price": 55},
    {"name": "Yonex GR 201", "playStyle": "balanced", "price": 40},
    {"name": "Yonex Carbonex 6000", "playStyle": "balanced", "price": 70},
    {"name": "Li-Ning XP 1000", "playStyle": "defensive", "price": 80},
    {"name": "Victor Jetpower 2.0", "playStyle": "offensive", "price": 60},
    {"name": "Yonex Isometric 200", "playStyle": "balanced", "price": 65},
    {"name": "Li-Ning Junior XP", "playStyle": "defensive", "price": 35}
]

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    skill_level = data.get('skillLevel')
    play_style = data.get('playStyle')
    budget = data.get('budget')

    # Filter rackets based on user input
    filtered_rackets = [r for r in rackets if r['playStyle'] == play_style and r['price'] <= budget]

    # Shuffle the filtered rackets to add randomness
    random.shuffle(filtered_rackets)

    # Limit recommendations to 3 random rackets
    recommendations = filtered_rackets[:3] if len(filtered_rackets) > 0 else []

    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
