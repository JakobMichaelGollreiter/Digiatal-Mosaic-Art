import os
from PIL import Image

input_folder = "marietest"
output_folder = "marietest_output"
min_size = (500, 500)

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

for input_file in os.listdir(input_folder):
    if input_file.lower().endswith(".jpg"):
        input_path = os.path.join(input_folder, input_file)
        output_file = os.path.join(output_folder, f"{os.path.splitext(input_file)[0]}_output.jpg")

        try:
            with Image.open(input_path) as img:
                if img.size != min_size:
                    img = img.resize(min_size, Image.LANCZOS)
                    img.save(output_file)
                    print(f"Processed: {input_file}")
                else:
                    print(f"Image {input_file} is already {min_size}, no need to process.")
        except Exception as e:
            print(f"Error processing {input_file}: {e}")
    else:
        print(f"Skipped: {input_file} (not a JPEG file)")
