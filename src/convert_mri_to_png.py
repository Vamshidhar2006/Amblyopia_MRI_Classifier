import nibabel as nib
import matplotlib.pyplot as plt
from pathlib import Path

# -----------------------------
# CHANGE THESE PATHS
# -----------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

NORMAL_MRI = PROJECT_ROOT / "dataset" / "Normal_fMRIdata" / "sbj01" / "anat.nii.gz"

AMBLYOPIA_MRI = PROJECT_ROOT / "dataset" / "Amblyopia_fMRIdata" / "sbj01" / "anat.nii.gz"

OUTPUT_FOLDER = PROJECT_ROOT / "static" / "images"

OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)


# -----------------------------
# Function to Save Middle Slice
# -----------------------------

def save_middle_slice(input_file, output_file):

    img = nib.load(str(input_file))
    data = img.get_fdata()

    # Middle axial slice
    z = data.shape[2] // 2

    plt.figure(figsize=(6, 6))

    plt.imshow(
        data[:, :, z].T,
        cmap="gray",
        origin="lower"
    )

    plt.axis("off")

    plt.savefig(
        output_file,
        dpi=300,
        bbox_inches="tight",
        pad_inches=0
    )

    plt.close()


# -----------------------------
# Convert Images
# -----------------------------

save_middle_slice(
    NORMAL_MRI,
    OUTPUT_FOLDER / "normal.png"
)

save_middle_slice(
    AMBLYOPIA_MRI,
    OUTPUT_FOLDER / "amblyopia.png"
)

print("=" * 50)
print("Images Created Successfully")
print("=" * 50)
print("Normal     :", OUTPUT_FOLDER / "normal.png")
print("Amblyopia  :", OUTPUT_FOLDER / "amblyopia.png")