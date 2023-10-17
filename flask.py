
from flask import flask, request, jsonify
import main  

app = flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('D:\HACKATHONS\python stuff\chatbot\bot.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('user_input')
    bot_response = main.py.get_response(user_input)
    return jsonify({'bot_response': bot_response})

if __name__ == '__main__':
    app.run()
