from langchain_core.prompts import PromptTemplate


personality_template ="""
     You are a senior psychological consultant. Analyze the following user profile 
    to provide a detailed personality assessment.

USER DATA:
- Introduction: {user_intro}
- Preferred Work Environment: {work_style}
- Decision Making Style: {decision_logic}
- Social Energy: {social_battery}
- Handling Pressure: {stress_response}

ANALYSIS INSTRUCTIONS:
1. Evaluate the user across the Big Five personality traits.
2. Identify their top 3 strengths and 2 potential blind spots.
3. Suggest a communication style that works best for this person.
4. Conclude with a "Personality Archetype" name (e.g., 'The Relentless Architect').

Final Assessment:

"""


prompt = PromptTemplate(
    input_variables=["user_intro", "work_style", "decision_logic", "social_battery", "stress_response"],
    template=personality_template
)

# personality_template.save('personality_temp.json')



