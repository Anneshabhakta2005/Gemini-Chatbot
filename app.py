import os
import google.generativeai as genai
from flask import Flask, request, render_template, jsonify
from dotenv import load_dotenv
import markdown2

# Load API Key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    response = model.generate_content(user_input)
    
    # Convert Markdown to HTML (for LaTeX and formatting)
    response_text = markdown2.markdown(response.text)

    return jsonify({'response': response_text})

if __name__ == '__main__':
    app.run(debug=True)
