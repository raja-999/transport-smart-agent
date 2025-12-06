import pandas as pd
import numpy as np
import random
from datetime import datetime

random.seed(42)
np.random.seed(42)

n = 200

first_names = ["Raja","Ali","Mouna","Sami","Leila","Omar","Nora","Youssef","Ines","Salah","Maya","Karim","Safa","Hatem"]
last_names = ["BenBey","Trabelsi","Haddad","Kallel","Bouaziz","Zidi","Mansour","Mezghani","Fakhfakh","Said","Kchouk","Jabari"]

names = [f"{random.choice(first_names)} {random.choice(last_names)}" for _ in range(n)]
ages = np.random.randint(18, 31, size=n)
genders = np.random.choice(["F","M"], size=n, p=[0.55,0.45])

distance_km = np.round(np.random.uniform(0.5, 30, n), 2)
duration_min = (distance_km * np.random.uniform(2.5, 4.0, size=n)).astype(int)

has_car = np.random.choice([0,1], size=n, p=[0.7,0.3])
has_bike = np.random.choice([0,1], size=n, p=[0.6,0.4])
has_license = np.where(has_car==1, 1, np.random.choice([0,1], size=n, p=[0.5,0.5]))

modes = ["Walk", "Bike", "Bus", "Train", "Car", "Scooter"]
current_mode = np.random.choice(modes, size=n)

comfort_pref = np.round(np.random.uniform(0,1,n),2)
cost_pref = np.round(np.random.uniform(0,1,n),2)
env_pref = np.round(np.random.uniform(0,1,n),2)
punctuality_pref = np.round(np.random.uniform(0,1,n),2)

df = pd.DataFrame({
    "id": range(1, n+1),
    "name": names,
    "gender": genders,
    "age": ages,
    "distance_km": distance_km,
    "duration_min": duration_min,
    "current_mode": current_mode,
    "has_car": has_car,
    "has_bike": has_bike,
    "has_license": has_license,
    "comfort_pref": comfort_pref,
    "cost_pref": cost_pref,
    "env_pref": env_pref,
    "punctuality_pref": punctuality_pref,
    "created_at": datetime.utcnow().strftime("%Y-%m-%d"),
})

df.to_csv("students_synthetic.csv", index=False)
print("Dataset created: students_synthetic.csv")
