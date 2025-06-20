from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib 

app = FastAPI()

model = joblib.load("../models/mental_health_model.pkl")
ordinal_encoder = joblib.load("../models/ordinal_encoder.pkl")

class SurveyData(BaseModel):
    gender: str
    self_employed: str
    family_history: str
    days_indoors: str
    growing_stress: str
    changes_habits: str
    mental_health_history: str
    mood_swings: str
    coping_struggles: str
    work_interest: str

@app.post("/predict")
def predict(data: SurveyData):
    input_data = {
        k: v.lower().replace(" ", "_") for k, v in data.dict().items()
    }

    #  yes=1, no=0
    binary_cols = ['gender', 'self_employed', 'family_history', 'coping_struggles']
    for col in binary_cols:
        input_data[col] = 1 if input_data[col] == 'yes' else 0

    ordinal_input = [
        input_data['days_indoors'],
        input_data['growing_stress'],
        input_data['changes_habits'],
        input_data['mental_health_history'],
        input_data['mood_swings'],
        input_data['work_interest']
    ]
    encoded_ordinal = ordinal_encoder.transform([ordinal_input])
    final_input = [
        input_data['gender'],
        input_data['self_employed'],
        input_data['family_history'],
        *encoded_ordinal[0],
        input_data['coping_struggles']
    ]

    prediction = model.predict(np.array([final_input]))
    return {"prediction": int(prediction[0])}
