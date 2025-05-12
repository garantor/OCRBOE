import os
import re
from google.cloud import vision

from utils import datetime_to_millis, extract_eta_dates

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'vision_key.json'





def detect_text(path):
    client = vision.ImageAnnotatorClient()

    with open(path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.document_text_detection(image=image)

    # Extract full document text
    full_text = response.full_text_annotation.text
    print("Full OCR Text:\n", full_text)
    result = extract_eta_dates(full_text)

    if result:
        dates_start = result["start_date_str"]
        dates_end = result["end_date_str"]
        end_millisecond = datetime_to_millis(result["end_date"])
        print('Start Date: ', dates_start, '\nEnd dates: ', dates_end, '\nMillisecond:', end_millisecond)


    else:
        print("❌ No valid ETA date found.")
    if response.error.message:
        raise Exception(
            f"{response.error.message}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors"
        )

# Example call
detect_text('ETA-APPROVAL001.png')
