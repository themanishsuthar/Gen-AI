import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

from personality_prompt import personality_template,prompt

load_dotenv()
                               
st.title("Advanced Personality Profiler")

with st.sidebar:
    st.header("Parameters")

    work = st.selectbox( "Work Style", ["Deep Focus/Solo", "Collabrative/Team", "Fast-paced/Dynamic"] ) 

    logic = st.select_slider( "Decision Making", options=["Purely Emotional", "Balanced", "Data-Driven"] )

    social = st.radio( "Social Battery", ["Introverted (Recharge Alone)", "Extroverted (Recharge with others)"] )

    stress = st.text_input("How do you react to tight deadline?",placeholder='eg: I got organised / I got anxious')


user_intro = st.text_area("Tell me about your journey so far:",height=150)

if st.button(" Generate Personality Report"):
    if user_intro and stress:
        model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
        
        user_input = prompt.format(
            user_intro=user_intro,
            work_style=work,
            decision_logic=logic,
            social_battery=social,
            stress_response=stress
        )

        with st.spinner("Analyze traits..."):
            response = model.invoke(user_input)
            st.markdown('---')
            st.markdown(response.content)
    else:
        st.warning("Please fill in the intro and stress response fields.")


