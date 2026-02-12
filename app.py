import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS 
from utils.genai_utils import get_explanation
from utils.code_utils import get_code
from utils.image_utils import get_visual_desc
from utils.audio_utils import generate_audio

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/generate', methods=['POST'])
def generate():
    try:
        data = request.json
        topic = data.get('topic')
        level = data.get('level')
        mode = data.get('mode')

        if mode == 'explanation':
            result = get_explanation(topic, level)
            return jsonify({"output": result})
        
        elif mode == 'visual':
            result = get_visual_desc(topic, level)
            return jsonify({"output": result})
        
        elif mode == 'code':
            result = get_code(topic, level)
            return jsonify({"output": result})
        
        elif mode == 'audio':
            explanation_text = get_explanation(topic, level)
            audio_filename = generate_audio(topic, level, explanation_text)
            
            if audio_filename:
                return jsonify({
                    "output": "Audio Ready",
                    "audio_url": f"/static/{audio_filename}"
                })
            else:
                return jsonify({"error": "Audio generation failed"}), 500
                
    except Exception as e:
        print(f"🔥 Server Error: {e}")
        return jsonify({"error": "The AI is having trouble. Check terminal."}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)