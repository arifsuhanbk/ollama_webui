from ollama import list as list_models

models = list_models()
model_names = [model['model'] for model in models['models']]
print(model_names)

# import ollama

# def list_models():
#     models = ollama.list()
#     print("Available Ollama Models:")
#     for model in models['models']:
#         name = model.get('name')
#         size = model.get('size', 0) / (1024 ** 2)  # Size in MB
#         modified = model.get('modified_at')
#         print(f"- {name} (Modified: {modified}, Size: {size:.2f} MB)")

# if __name__ == "__main__":
#     list_models()
