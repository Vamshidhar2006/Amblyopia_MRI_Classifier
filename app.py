from flask import Flask, render_template, request
from pathlib import Path
import shutil

from src.predict import predict_mri

app = Flask(__name__)

# ---------------------------------------
# Project Paths
# ---------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent

UPLOAD_FOLDER = PROJECT_ROOT / "uploads"

UPLOAD_FOLDER.mkdir(exist_ok=True)


# ---------------------------------------
# Home Page
# ---------------------------------------

@app.route("/")
def home():
    return render_template("index.html")


# ---------------------------------------
# Predict
# ---------------------------------------

@app.route("/predict", methods=["POST"])
def predict():

    if "mri_file" not in request.files:
        return "No file uploaded."

    file = request.files["mri_file"]

    if file.filename == "":
        return "Please choose a file."

    # Save uploaded file
    uploaded_file = UPLOAD_FOLDER / file.filename

    with open(uploaded_file, "wb") as buffer:
        shutil.copyfileobj(file.stream, buffer)

    # Run Prediction
    result = predict_mri(uploaded_file)

    return render_template(
        "result.html",
        filename=file.filename,
        prediction=result["prediction"],
        confidence=result["confidence"]
    )


# ---------------------------------------
# Run Server
# ---------------------------------------

if __name__ == "__main__":
    app.run(debug=True)