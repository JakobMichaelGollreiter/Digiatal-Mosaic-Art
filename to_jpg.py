from PIL import Image
import os

input_folder = "bilderProjekt "
output_folder = "bilderProjektJpg"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(".png"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".jpg")

        try:
            with Image.open(input_path) as img:
                img.convert("RGB").save(output_path)
                print(f"Converted: {input_path}")
        except Exception as e:
            print(f"Error converting {input_path}: {e}")
    else:
        print(f"Skipped: {filename} (not a PNG file)")
