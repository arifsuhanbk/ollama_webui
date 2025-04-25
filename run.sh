pip install ollama
python app.py

# docker run -d \
#   -p 3000:3000 \
#   -e OLLAMA_BASE_URL=http://127.0.0.1:11434 \
#   --name open-webui \
#   ghcr.io/open-webui/open-webui:main
# docker start open-webui
# docker start open-webui
# http://localhost:3000
# du -sh $(pip show open-webui | grep Location | cut -d' ' -f2)/open_webui
# pip install huggingface_hub[hf_xet]` or `pip install hf_xet`

# http://localhost:8080/
# admin/admin

# ollama list
# sudo systemctl stop ollama
# ollama run gemma3:1b
# open-webui serve

# ollama stop gemma3:1b
# sudo systemctl stop ollama 