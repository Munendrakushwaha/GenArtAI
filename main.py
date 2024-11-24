from flask import Flask, jsonify, render_template
import os
from openai import OpenAI

# Set up OpenAI client
my_secret = os.environ['DALLE_KEY']
client = OpenAI(api_key=my_secret)

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generateimages/<prompt>')
def generate(prompt):
    print("Prompt:", prompt)
    response = client.images.generate(
        model="dall-e-2",
        prompt=prompt,
        size="256x256",
        quality="standard",
        n=2,
    )
    print(response)
    images = [{"url": image.url} for image in response.data]
    print("images are:::::::",images)
    return jsonify({"prompt": prompt, "images": images})

# Run the app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)
