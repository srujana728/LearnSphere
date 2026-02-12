import google.generativeai as genai

API_KEY = "AIzaSyAlrPBnRsGFtLAPgqZ3XZIXkwmD5ZIdfx4"
genai.configure(api_key=API_KEY)

def get_visual_desc(topic, level):
    # Stable 2026 models
    models_to_try = ['gemini-2.5-flash-lite', 'gemini-1.5-flash']
    
    prompt = (f"Act as a professional technical illustrator. Describe a visual diagram "
              f"that explains {topic} for a {level} level student. "
              "Focus on layout, arrows, and key labels to create a clear mental image.")

    for model_name in models_to_try:
        try:
            model = genai.GenerativeModel(model_name)
            response = model.generate_content(prompt)
            if response and response.text:
                return response.text
        except Exception as e:
            print(f"⚠️ Image-AI error: {str(e)[:50]}")
            continue
            
    return "❌ Artist AI is unavailable. Please try again later."