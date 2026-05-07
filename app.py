from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

api_key = os.getenv("GEMINI_API_KEY")

print("=" * 50)
print(f"API key loaded: '{api_key}'")
print(f"Key length: {len(api_key) if api_key else 0}")
print("=" * 50)

app = Flask(__name__)
genai.configure(api_key=api_key)

PERSONALITY_PROMPTS = {
    "friendly": "You are a warm, friendly, and enthusiastic chatbot. Use casual language, be encouraging, and add a personal touch to every response. Use occasional emojis.",
    "professional": "You are a professional and formal assistant. Provide structured, concise, and accurate responses. Maintain a respectful and business-like tone at all times.",
    "funny": "You are a witty and humorous chatbot. Use jokes, puns, and playful language. Keep things light-hearted while still being helpful.",
    "sarcastic": "You are a sarcastic chatbot with dry humor. Respond with wit and irony, but remain ultimately helpful. Don't be mean, just playfully sarcastic.",
    "custom": None  
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get('message', '').strip()
    personality_key = data.get('personality_key', 'friendly')
    custom_personality = data.get('custom_personality', '')
    history = data.get('history', [])

    if not message:
        return jsonify({'reply': 'Please enter a message.'}), 400

    if personality_key == 'custom' and custom_personality:
        system_prompt = f"You are a chatbot with the following personality: {custom_personality}. Stay in character throughout the conversation."
    else:
        system_prompt = PERSONALITY_PROMPTS.get(personality_key, PERSONALITY_PROMPTS['friendly'])

    conversation = system_prompt + "\n\nConversation so far:\n"
    for turn in history:
        conversation += f"User: {turn['user']}\nChatbot: {turn['bot']}\n"
    conversation += f"User: {message}\nChatbot:"

    try:
        model = genai.GenerativeModel('gemini-2.5-flash')
        response = model.generate_content(conversation)
        reply = response.text.strip()
    except Exception as e:
        reply = f"Sorry, I encountered an error: {str(e)}"

    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True)