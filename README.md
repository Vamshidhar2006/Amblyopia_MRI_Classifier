# Amblyopia MRI Classifier

## Overview

The Amblyopia MRI Classifier is a machine learning-based web application developed to classify structural brain MRI scans as either **Normal** or **Amblyopia**. The application accepts MRI scans in NIfTI (`.nii.gz`) format, extracts statistical features from the image, and predicts the diagnosis using a trained Random Forest classifier.

The project demonstrates the complete workflow of a medical imaging application, from MRI preprocessing and feature extraction to prediction through a Flask-based web interface.

---

## Features

- Upload structural MRI scans (`.nii` / `.nii.gz`)
- Automatic feature extraction from MRI images
- Classification using a Random Forest model
- Prediction with confidence score
- Simple web interface built with Flask and Bootstrap
- MRI slice visualization

---

## Technologies Used

**Programming Language**
- Python

**Machine Learning**
- Scikit-learn
- Random Forest Classifier

**Medical Image Processing**
- NiBabel
- NumPy

**Visualization**
- Matplotlib

**Web Development**
- Flask
- HTML
- Bootstrap 5

---

## Project Workflow

```
MRI Scan (.nii.gz)
        │
        ▼
Load MRI using NiBabel
        │
        ▼
Extract Features
(Mean, Standard Deviation, Minimum, Maximum)
        │
        ▼
Random Forest Classifier
        │
        ▼
Prediction
(Normal / Amblyopia)
```

---

## Project Structure

```
Amblyopia_MRI_Classifier/
│
├── app.py
├── models/
│   └── baseline_model.pkl
├── src/
│   ├── load_data.py
│   ├── feature_extraction.py
│   ├── train.py
│   ├── predict.py
│   └── visualize.py
├── static/
├── templates/
├── requirements.txt
└── README.md
```

---

## Model Details

**Algorithm**

- Random Forest Classifier

**Extracted Features**

- Mean Intensity
- Standard Deviation
- Minimum Intensity
- Maximum Intensity

**Current Accuracy**

66.67%

---

## Dataset

The model is trained using structural MRI scans stored in NIfTI (`.nii.gz`) format.

The dataset is not included in this repository because of its size.

Expected folder structure:

```
dataset/
├── Normal_fMRIdata/
└── Amblyopia_fMRIdata/
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Vamshidhar2006/Amblyopia_MRI_Classifier.git
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## Future Improvements

- Train deep learning models using 3D CNNs
- Integrate functional MRI (fMRI) data
- Support multimodal MRI analysis
- Add Explainable AI techniques
- Improve feature engineering
- Deploy the application to the cloud

---

## Author

**Vamshidhar Reddy**

B.Tech in Computer Science and Engineering (Artificial Intelligence & Machine Learning)

Alliance University, Bangalore

GitHub: https://github.com/Vamshidhar2006

---

## Disclaimer

This project was developed for educational and research purposes only. It is not intended to replace professional medical diagnosis or clinical decision-making.
