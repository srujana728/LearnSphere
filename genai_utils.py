import google.generativeai as genai
import time

# ✅ Updated with your new working API Key
API_KEY = "AIzaSyAlrPBnRsGFtLAPgqZ3XZIXkwmD5ZIdfx4"
genai.configure(api_key=API_KEY)

def get_explanation(topic, level):
    # LEAD WITH FLASH-LITE for the highest free-tier quota in 2026
    models_to_try = [
        'gemini-2.5-flash-lite', 
        'gemini-3-flash-preview', 
        'gemini-1.5-flash'
    ]
    
    prompt = (
        f"Explain the Machine Learning concept of '{topic}' for a {level} level student. "
        "IMPORTANT: Every 2-3 paragraphs, insert a visual marker like this: "
        "[VISUAL: description of a diagram or image]. "
        "This marker should describe what the student should see at that point."
    )

    for model_name in models_to_try:
        try:
            print(f"📡 Requesting Explanation from: {model_name}...")
            model = genai.GenerativeModel(model_name)
            response = model.generate_content(prompt)
            
            if response and response.text:
                return response.text
                
        except Exception as e:
            print(f"⚠️ {model_name} failed: {str(e)[:100]}")
            continue
            
    return "❌ Connection Failed: Daily quota reached on all models. Please try again tomorrow."