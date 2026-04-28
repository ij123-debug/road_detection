import os

def convert_labels(folder):
    for filename in os.listdir(folder):
        if filename.endswith(".txt"):
            path = os.path.join(folder, filename)

            new_lines = []

            with open(path, "r") as f:
                lines = f.readlines()

            for line in lines:
                parts = line.strip().split()
                class_id = int(parts[0])

                # mapping
                if class_id == 0:
                    parts[0] = "0"   # crack
                elif class_id in [2, 3, 4]:
                    parts[0] = "1"   # pothole
                else:
                    continue  # remove damage

                new_lines.append(" ".join(parts))

            with open(path, "w") as f:
                f.write("\n".join(new_lines))

# run for all folders
convert_labels("train/labels")
convert_labels("valid/labels")


print("✅ Conversion done")