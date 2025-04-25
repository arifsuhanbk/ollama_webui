from flask import Flask, render_template, request, jsonify, Response
from ollama import chat
from ollama import list as list_models

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/models')
def get_models():
    try:
        models = list_models()
        model_names = [model['model'] for model in models['models']]
        return jsonify(model_names)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/chat', methods=['POST'])
def process():
    data = request.json
    user_message = data['message']
    model = data.get('model', 'gemma3:1b')  # Fallback if not provided

    def generate():
        response = chat(model=model, messages=[{
            'role': 'user',
            'content': user_message
        }], stream=True)

        for chunk in response:
            if 'message' in chunk and 'content' in chunk['message']:
                yield chunk['message']['content']
    
    return Response(generate(), content_type='text/plain')

if __name__ == '__main__':
    app.run(debug=True)
