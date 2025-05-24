# Tourist Backend Project

This project provides an API for detecting text in images using the Google Cloud Vision API. It includes functionality to extract ETA dates from the detected text.

## Project Structure

```
tourist-backend
├── main.py          # Core functionality for detecting text in images
├── api              # Contains the API implementation
│   └── app.py      # Entry point for the Flask API
├── utils.py         # Utility functions for date extraction and conversion
├── requirements.txt  # Project dependencies
└── README.md        # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd tourist-backend
   ```

2. **Install dependencies:**
   Make sure you have Python installed, then run:
   ```
   pip install -r requirements.txt
   ```

3. **Set up Google Cloud Vision API:**
   - Create a Google Cloud project.
   - Enable the Vision API.
   - Create a service account and download the JSON key file.
   - Set the environment variable for the credentials:
     ```
     export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/vision_key.json"
     ```

## Usage

To start the API, run the following command:

```
python -m api.app
```

### API Endpoint

- **POST /detect-text**
  - **Description:** Accepts a base64 image URL and processes it to extract text.
  - **Request Body:**
    ```json
    {
      "image_data": "base64_encoded_image_string"
    }
    ```
  - **Response:**
    - On success:
      ```json
      {
        "start_date": "extracted_start_date",
        "end_date": "extracted_end_date",
        "millisecond": "extracted_millisecond"
      }
      ```
    - On error:
      ```json
      {
        "error": "Error message"
      }
      ```

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.