import os
import shutil

# Update these paths to your actual folders
source_folder = r"C:\Users\nitu\Pictures\source"
destination_folder = r"C:\Users\nitu\Pictures\destination"

# Ensure both paths exist
if not os.path.exists(source_folder):
    print(f"Source folder does not exist: {source_folder}")
    exit()

# Create destination folder if it doesn't exist
os.makedirs(destination_folder, exist_ok=True)

# Move .jpg files
for filename in os.listdir(source_folder):
    if filename.lower().endswith(".jpg"):
        source_path = os.path.join(source_folder, filename)
        dest_path = os.path.join(destination_folder, filename)
        shutil.move(source_path, dest_path)
        print(f"Moved: {filename}")

print("All .jpg files moved.")
