import nibabel as nib
import numpy as np
import pandas as pd
from pathlib import Path

# -------------------------
# Project Path
# -------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATASET_PATH = PROJECT_ROOT / "dataset"

features = []

# -------------------------
# Loop through classes
# -------------------------
for class_name in ["Normal_fMRIdata", "Amblyopia_fMRIdata"]:

    class_path = DATASET_PATH / class_name

    # Label
    label = 0 if class_name == "Normal_fMRIdata" else 1

    # Loop through every subject
    for subject in class_path.iterdir():

        anat_path = subject / "anat.nii.gz"

        if anat_path.exists():

            img = nib.load(str(anat_path))
            data = img.get_fdata()

            feature = {

                "Subject": subject.name,

                "Class": class_name,

                "Mean": np.mean(data),

                "Std": np.std(data),

                "Min": np.min(data),

                "Max": np.max(data),

                "Label": label

            }

            features.append(feature)

# -------------------------
# Create DataFrame
# -------------------------

df = pd.DataFrame(features)

print(df)

print("\nTotal Subjects :", len(df))

# Save

df.to_csv(PROJECT_ROOT / "outputs" / "mri_features.csv", index=False)

print("\nDataset saved successfully!")