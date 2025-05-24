from flask import Flask, request, jsonify
import base64
import os, re
from google.cloud import vision
from utils import datetime_to_millis, extract_eta_dates

app = Flask(__name__)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'vision_key.json'

def detect_text(content):
    client = vision.ImageAnnotatorClient()
    image = vision.Image(content=content)
    response = client.document_text_detection(image=image)

    full_text = response.full_text_annotation.text
    print("Full OCR Text:\n", full_text)
    print("======================================== 2222")
    result = extract_eta_dates(full_text)
    print("Extracted Dates:\n", result)

    if result:
        dates_start = result["start_date_str"]
        dates_end = result["end_date_str"]
        end_millisecond = datetime_to_millis(result["end_date"])
        return {
            'start_date': dates_start,
            'end_date': dates_end,
            'end_millisecond': end_millisecond
        }
    else:
        return {"error": "No valid ETA date found."}

    # if response.error.message:
    #     raise Exception(
    #         f"{response.error.message}\nFor more info on error messages, check: "
    #         "https://cloud.google.com/apis/design/errors"
    #     )

@app.route('/detect', methods=['POST'])
def detect():
    data = request.json
    if 'image' not in data:
        return jsonify({"error": "No image provided."}), 400

    image_data = data['image']
    try:
        image_content = base64.b64decode(image_data)
        result = detect_text(image_content)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)