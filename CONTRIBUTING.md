# CONTRIBUTING

## How to run the Dockerfile locally

'''
docker run -dp 5000:5000 -w /app -v "/c/Documents/yourproject:/app" IMAGE_NAME sh -c "flask run"
'''