from flask import Flask, render_template, request, jsonify
from ollama import chat
from ollama import ChatResponse

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def process():
    data = request.json  # Get the data from the frontend
    
    # Prepare the messages for the model
    user_message = data['message']
    print(user_message)

    try:
        # Use the Ollama chat function to get a response from the model
        response: ChatResponse = chat(model='gemma3:1b', messages=[
            {
                'role': 'user',
                'content': user_message
            }
        ])
        
        message_content = response['message']['content']
        print(message_content)

        return jsonify({
            "message": "Ollama API responded successfully",
            "response_data": message_content
        })
    
    except Exception as e:
        return jsonify({"message": "Failed to get a response from Ollama API", "error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
