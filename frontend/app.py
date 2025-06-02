import streamlit as st
import requests
st.subheader("MentalHealth Treatment Prediction")
st.caption("This app predicts whether a person needs mental health treatment based on their responses to a series of questions.")
col1, col2 = st.columns(2)


with col1:
    genre = st.selectbox("Enter Your Genre:", ['Male','Female'])
    self_employed = st.selectbox("Are you self-employed?", ['Yes', 'No'])
    family_history = st.selectbox("Do you have a family history of mental illness?", ['Yes', 'No'])
    days_indoors = st.selectbox("How many days have you spent indoors?", ['1-14 days', 'Go out Every day', 'More than 2 months', '15-30 days', '31-60 days'])
    growing_stress = st.selectbox("Are you experiencing growing stress?", ['Yes', 'No', 'Maybe'])
with col2:
    changes_habits = st.selectbox("Have you noticed changes in your habits?",['Yes', 'No', 'Maybe'])
    mental_health_history = st.selectbox("Do you have a history of mental health issues?", ['No', 'Maybe', 'Yes'])
    mood_swings = st.selectbox("How would you describe your mood swings?", ['Medium', 'Low', 'High'])
    work_interest = st.selectbox("Are you interested in work?", ['Yes', 'No', 'Maybe'])
    coping_struggles = st.selectbox("Are you struggling to cope?", ['Yes', 'Mo', 'Maybe'])

if st.button("Predict"):
    input_data = {
        "gender": genre,
        "self_employed": self_employed,
        "family_history": family_history,
        "days_indoors": days_indoors,
        "growing_stress": growing_stress,
        "changes_habits": changes_habits,
        "mental_health_history": mental_health_history,
        "mood_swings": mood_swings,
        "work_interest": work_interest,
        "coping_struggles": coping_struggles
}

    response = requests.post("http://localhost:8000/predict", json=input_data)
    result = response.json()
    
    st.subheader("🩺 Prediction Result:")
    st.write(f"**Prediction:** {'Needs Treatment' if result['prediction'] == 1 else 'No Treatment Needed'}")
   
st.caption("This app is for informational purposes only and should not be used as a substitute for professional medical advice.Thank you for using the Mental Health Treatment Prediction app! If you have any concerns, please consult a healthcare professional.")
footer = """
<div style=" bottom: 10px; width: 100%; text-align: center; font-size: 16px;">
    <a href="https://www.kaggle.com/datasets/bhavikjikadara/mental-health-dataset/data" target="_blank">DataSet</a> |
    <a href="https://github.com/EgonLh/Mental-Health-Pred" target="_blank">Source Code</a> |
    <a href="https://egon-12k2.vercel.app/" target="_blank">Contact</a>
</div>
"""

st.markdown(footer, unsafe_allow_html=True)
