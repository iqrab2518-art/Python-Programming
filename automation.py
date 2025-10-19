import os
import shutil

print("=== Image Organizer Script ===")
print("This tool will move all .jpg and other image files from one folder to another.\n")

base_folder = r"D:\Internship work"
source_folder = os.path.join(base_folder, "images")
target_folder = os.path.join(base_folder, "sorted_images")

os.makedirs(target_folder, exist_ok=True)

if not os.path.exists(source_folder):
    print(f"Source folder not found at: {source_folder}")
else:
    moved = 0
    for file_name in os.listdir(source_folder):
        if file_name.lower().endswith((".jpg", ".jpeg", ".png", ".jfif", ".webp")):
            source_path = os.path.join(source_folder, file_name)
            target_path = os.path.join(target_folder, file_name)
            shutil.move(source_path, target_path)
            moved += 1
            print(f"Moved: {file_name}")

    if moved == 0:
        print("No image files found in the source folder.")
    else:
        print(f"\n✅ Done! {moved} image(s) moved to {target_folder}")
