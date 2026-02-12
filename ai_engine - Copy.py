import google.generativeai as genai
import os

# Updated with your new API Key
API_KEY = "AIzaSyAlrPBnRsGFtLAPgqZ3XZIXkwmD5ZIdfx4"
genai.configure(api_key=API_KEY)

def generate_ml_explanation(topic, style):
    # Use Flash-Lite to ensure high daily quota availability
    model = genai.GenerativeModel('gemini-2.5-flash-lite')
    
    prompts = {
        "coder": f"Explain {topic} in Machine Learning. Provide a clear conceptual overview and a high-quality Python code implementation using Scikit-Learn or TensorFlow. Insert [VISUAL: description] markers every 2 paragraphs.",
        "beginner": f"Explain {topic} in Machine Learning using simple analogies and no jargon. Focus on why it matters. Insert [VISUAL: description] markers every 2 paragraphs.",
        "visual": f"Explain {topic} and describe what a diagram of this concept would look like (layers, nodes, or flowcharts). Use [VISUAL: description] markers frequently."
    }

    selected_prompt = prompts.get(style, prompts["beginner"])
    
    try:
        response = model.generate_content(selected_prompt)
        return {
            "status": "success",
            "topic": topic,
            "explanation": response.text,
            "style_applied": style
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}