import joblib
import nibabel as nib
import numpy as np
from pathlib import Path

# -------------------------------------------------
# Project Paths
# -------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent

MODEL_PATH = PROJECT_ROOT / "models" / "baseline_model.pkl"


# -------------------------------------------------
# Load trained model
# -------------------------------------------------
model = joblib.load(MODEL_PATH)


# -------------------------------------------------
# Extract Features
# -------------------------------------------------
def extract_features(mri_path):

    img = nib.load(str(mri_path))
    data = img.get_fdata()

    features = np.array([[
        np.mean(data),
        np.std(data),
        np.min(data),
        np.max(data)
    ]])

    return features


# -------------------------------------------------
# Predict
# -------------------------------------------------
def predict_mri(mri_path):

    features = extract_features(mri_path)

    prediction = model.predict(features)[0]

    probability = model.predict_proba(features)[0]

    confidence = probability.max() * 100

    if prediction == 0:
        diagnosis = "Normal"
    else:
        diagnosis = "Amblyopia"

    return {
        "prediction": diagnosis,
        "confidence": round(confidence, 2)
    }


# -------------------------------------------------
# Run from Terminal
# -------------------------------------------------
if __name__ == "__main__":

    test_file = PROJECT_ROOT / "dataset" / "Normal_fMRIdata" / "sbj01" / "anat.nii.gz"

    result = predict_mri(test_file)

    print("=" * 40)
    print("MRI Prediction")
    print("=" * 40)
    print("Diagnosis :", result["prediction"])
    print("Confidence:", result["confidence"], "%")