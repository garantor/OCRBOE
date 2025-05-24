from flask import Flask, request, jsonify
import base64
import io
from PIL import Image
from main import detect_text

app = Flask(__name__)

@app.route('/detect-text', methods=['POST'])
def detect_text_endpoint():
    data = request.get_json()

    if 'image' not in data:
        return jsonify({'error': 'No image provided'}), 400

    image_data = data['image']

    try:
        # Decode the base64 image
        image_bytes = base64.b64decode(image_data)
        image = Image.open(io.BytesIO(image_bytes))

        # Save the image temporarily
        temp_image_path = 'temp_image.png'
        image.save(temp_image_path)

        # Call the existing detect_text function
        detect_text(temp_image_path)

        return jsonify({'message': 'Text detection completed successfully'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)