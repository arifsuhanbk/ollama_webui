from ollama import chat

def main():
    user_message = input("You: ")

    response = chat(
        model='gemma3:1b',
        messages=[{
            'role': 'user',
            'content': user_message
        }],
        stream=True
    )

    print("Assistant: ", end="", flush=True)
    for chunk in response:
        if 'message' in chunk and 'content' in chunk['message']:
            print(chunk['message']['content'], end="", flush=True)

if __name__ == '__main__':
    main()
