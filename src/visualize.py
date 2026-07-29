import nibabel as nib
import matplotlib.pyplot as plt
from pathlib import Path

# Project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# MRI file
mri_path = PROJECT_ROOT / "dataset" / "Normal_fMRIdata" / "sbj01" / "anat.nii.gz"

# Load MRI
img = nib.load(str(mri_path))
data = img.get_fdata()

print("MRI Shape:", data.shape)

# Middle slices
x = data.shape[0] // 2
y = data.shape[1] // 2
z = data.shape[2] // 2

plt.figure(figsize=(15,5))

# Sagittal
plt.subplot(1,3,1)
plt.imshow(data[x,:,:].T, cmap="gray", origin="lower")
plt.title("Sagittal")

# Coronal
plt.subplot(1,3,2)
plt.imshow(data[:,y,:].T, cmap="gray", origin="lower")
plt.title("Coronal")

# Axial
plt.subplot(1,3,3)
plt.imshow(data[:,:,z].T, cmap="gray", origin="lower")
plt.title("Axial")

plt.tight_layout()
plt.show()