import nibabel as nib
from pathlib import Path

# Project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Change this if you want another subject
mri_path = PROJECT_ROOT / "dataset" / "Normal_fMRIdata" / "sbj01" / "anat.nii.gz"

# Load MRI
img = nib.load(str(mri_path))

# Get MRI data
data = img.get_fdata()

print("=" * 50)
print("MRI Loaded Successfully")
print("=" * 50)

print(f"File Name      : {mri_path.name}")
print(f"Shape          : {data.shape}")
print(f"Dimensions     : {data.ndim}")
print(f"Data Type      : {data.dtype}")
print(f"Voxel Size     : {img.header.get_zooms()}")

print("=" * 50)