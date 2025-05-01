import subprocess

# Get the output of `ollama ps`
result = subprocess.run(['ollama', 'ps'], capture_output=True, text=True)

# Extract running model names
lines = result.stdout.strip().split('\n')
model_lines = lines[1:]  # Skip header

for line in model_lines:
    if not line.strip():
        continue
    model_name = line.split()[0]
    print(f"Stopping model: {model_name}")
    subprocess.run(['ollama', 'stop', model_name])