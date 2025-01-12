import os
import shutil
import csv

# Initialize an empty list to store file names
files = []

# Initialize a counter for the number of files
file_count = 0

# Open the CSV file (replace 'your_file.csv' with the actual file path)
with open('CHB-MIT DB timestamp.csv', mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    
    # Skip the header if there's one
    next(reader, None)
    
    for row in reader:
        # Check if the row has at least 30 columns to avoid index errors
        if len(row) >= 30:
            # Add files from the 2nd, 24th, and 30th columns (indexing starts at 0)
            files.append(row[1])  # 2nd column
            files.append(row[23])  # 24th column
            files.append(row[29])  # 30th column
            
            # Increment the file count for each added file name
            file_count += 3  # Each row adds 3 files to the list

# Sort the files list
files = sorted(files)

# Print the sorted list of files
print("Sorted Files:", files)
print("Total Number of Files:", file_count)

# Path to the original dataset folder
original_folder = 'chb_edf_dataset'  # Replace this with the path of the 'dataset' folder
# Path to the new folder where you want to copy the files
new_folder = 'final_data'  # Replace with your desired path for the new folder

# Ensure the new folder exists, if not create it
if not os.path.exists(new_folder):
    os.makedirs(new_folder)

# Function to copy files and create missing variants
for file in files:
    file_parts = file.split('_')
    # Check if the file exists in the original folder and has the .edf extension
    if f"{file}.edf" in os.listdir(original_folder):
        file_name = f"{file}.edf"
        source_path = os.path.join(original_folder, f"{file}.edf")
        dest_path = os.path.join(new_folder, file_name)
        shutil.copy(source_path, dest_path)
        print(f"Copying the same file: {file_name}")
    else:
        length = len(file_parts)
        if length == 3:
            variant_name = f"{file}.edf"
            base_name = file_parts[0]+'_'+file_parts[1]
            source_path = os.path.join(original_folder, f"{base_name}.edf")
            dest_path = os.path.join(new_folder, variant_name)
            shutil.copy(source_path, dest_path)
            print(f"Created missing file: {variant_name}")


print("All missing files have been added, and the dataset has been updated.")
