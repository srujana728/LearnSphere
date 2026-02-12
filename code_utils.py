import google.generativeai as genai
import time

# ✅ Ensure your key is valid
API_KEY = "AIzaSyAlrPBnRsGFtLAPgqZ3XZIXkwmD5ZIdfx4"
genai.configure(api_key=API_KEY)

def get_code(topic, level):
    # 2026 Failover strategy: Lite has the highest daily limit (1,000 RPD)
    models_to_try = [
        'gemini-2.5-flash-lite', 
        'gemini-3-flash-preview', 
        'gemini-1.5-flash'
    ]
    
    prompt = (f"Provide high-quality Python code for {topic} suitable for a {level} learner. "
              "Include helpful comments and use standard libraries like scikit-learn. "
              "Wrap the code in markdown blocks (```python).")

    for model_name in models_to_try:
        try:
            print(f"📡 Requesting Code from: {model_name}...")
            model = genai.GenerativeModel(model_name)
            response = model.generate_content(prompt)
            
            if response and response.text:
                return response.text
                
        except Exception as e:
            # If we hit a 429 quota error, we move to the next model in the list
            print(f"⚠️ {model_name} quota hit or error: {str(e)[:50]}...")
            continue
            
    return "❌ All coding models have reached their daily free limit. Please try again in 24 hours."