import os
import random
import shutil

# paths
images_path = "train/images"
labels_path = "train/labels"

val_images_path = "valid/images"
val_labels_path = "valid/labels"

# create valid folders if not exist
os.makedirs(val_images_path, exist_ok=True)
os.makedirs(val_labels_path, exist_ok=True)

# get all images
images = os.listdir(images_path)

# shuffle
random.shuffle(images)

# take 20%
split_size = int(0.2 * len(images))
val_images = images[:split_size]

# move files
for img in val_images:
    img_path = os.path.join(images_path, img)
    label_path = os.path.join(labels_path, img.replace(".jpg", ".txt"))

    shutil.move(img_path, os.path.join(val_images_path, img))

    if os.path.exists(label_path):
        shutil.move(label_path, os.path.join(val_labels_path, os.path.basename(label_path)))

print(f"Moved {len(val_images)} images to validation set.")