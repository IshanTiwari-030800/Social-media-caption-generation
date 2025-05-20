from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
from io import BytesIO
from neural_capgen import pred_step
from models.llama_instruct import generate_llama_caption
from pyngrok import ngrok, conf

# Paste your token here
authtoken = "2xBfj5NvyZ0u5dqzubepx5HfxYs_2Xn6ztZ54ythfVmToYvBq"
conf.get_default().auth_token = authtoken

app = Flask(__name__)
CORS(app)

def prompt_generation(option: str):

    """Returns the caption styling option"""

    if option=='long-caption':
        return 'Rewrite the text above as an instagram caption and add emojis. Elaborate the caption (around 100 words) and describe it in detail. ONLY RETURN THE REWRITTEN CAPTION, NO OTHER OUTPUT.'
    elif option == 'short-caption':
        return 'Rewrite the text above as an instagram caption and add emojis. Keep the caption short and concise.'
    else:
        return 'Generate hashtags like an instagram caption for the text above.'

@app.route('/generate', methods=['POST'])
def generate_caption():
    if 'image' not in request.files or 'option' not in request.form:
        return jsonify({"error": "Missing image or option"}), 400

    image_file = request.files['image']
    option = request.form['option']

    try:
        pred = pred_step(image_file)
        prompt = prompt_generation(option)
        response = generate_llama_caption(pred, prompt)
        return jsonify({'caption': response})

    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500

if __name__ == '__main__':
    public_url = ngrok.connect(5000)
    print(" * ngrok tunnel:", public_url)
    app.run(port=5000)