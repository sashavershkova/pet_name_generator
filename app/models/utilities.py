import google.generativeai as genai
import os

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

def generate_pet_name(request_body):
    model = genai.GenerativeModel("gemini-1.5-flash")
    input_message = f"I have a pet animal type {request_body["animal"]}, personality of {request_body["personality"]} and color - {request_body["coloration"]}. i need to come up with a name for it. I need just a name from you, nothing else"
    
    try:
        response = model.generate_content(input_message)
        name = response.text.strip()
    except Exception as err:
        print("Error accessing AI", err)
        return []

    return name
