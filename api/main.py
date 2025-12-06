from fastapi import FastAPI
from pydantic import BaseModel
from models.nsga2 import run_nsga2

app = FastAPI(title="Transport Smart Agent API")

class UserForm(BaseModel):
    name: str
    age: int
    distance_km: float
    has_car: int
    has_bike: int
    has_license: int
    current_mode: str
    comfort_pref: float
    cost_pref: float
    env_pref: float
    punctuality_pref: float

@app.post("/predict")
def predict(form: UserForm):
    input_data = form.dict()

    # Convertir les checkboxes en bool
    input_data['has_car'] = bool(input_data['has_car'])
    input_data['has_bike'] = bool(input_data['has_bike'])
    input_data['has_license'] = bool(input_data['has_license'])

    # Appeler la fonction NSGA2 pour obtenir la recommandation
    result = run_nsga2(input_data)

    # Retour adapté au Code Node n8n
    return {
        "mode_recommande": result["mode"],
        "confort": result["confort"],
        "cout": result["cout"],
        "impact_env": result["impact_env"],
        "ponctualite": result["ponctualite"]
    }
