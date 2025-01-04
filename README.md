# Meta-EEG of CHB-MIT Scalp EEG Database v1.0.0.0

## Overview

The **CHB-MIT Scalp EEG Database** is a well-known dataset containing EEG recordings from pediatric patients diagnosed with epilepsy. These records provide an essential resource for the study of seizure activity and the development of automated methods for epilepsy detection, prediction, and management.

The **CHB-MIT Meta EEG Dataset** released here contains **balanced, annotated, fixed-time, and length meta-data** of the CHB-MIT Scalp EEG database v1.0.0.0, focused on patient-specific (inter and intra) and patient non-specific EEG data. The dataset includes key segments from **ictal**, **pre-ictal**, **post-ictal**, **peri-ictal**, and **non-seizure** periods. These segments have been extracted from the original CHB-MIT dataset using specific time stamps and annotations.

The metadata generated from this dataset will help researchers and practitioners working with AI-based seizure detection models by providing them with standardized, non-redundant EEG data.

### The metadata includes:
- **Patient-Specific Data**: Contains inter- and intra-patient EEG data.
- **Patient Non-Specific Data**: Includes non-patient-specific segments.
- **Time Stamps**: Includes ictal, pre-ictal, post-ictal, peri-ictal, and non-seizure time segments.
- **Exclusions**: Data for channels ch06, ch12, ch23, ch24 in patient-specific and chb24_11 in patient non-specific have not been included.
  ![](database_details.png)

---

## Steps to Generate Meta Data

Follow the steps below to generate the **CHB-MIT Meta EEG Dataset** from the original CHB-MIT Scalp EEG database using this GitHub repository.

### Step 1: Download CHB-MIT EEG Data
1. Download the **CHB-MIT Scalp EEG dataset** (available from the [CHB-MIT database website](https://physionet.org/content/chbmit/1.0.0/)).
2. Place all the **EDF files** (electroencephalogram data) in a folder named `chb_edf_dataset`.
3. Place the **CHB-MIT DB timestamp.csv** (which contains the relevant time stamps), **code.ipynb** (Jupyter Notebook) and **data.py** files in the **same directory** as the above folder.

### Step 2: Data Preprocessing
1. Run the `data.py` file to preprocess the EEG data. This script will load the raw EEG data, perform any necessary cleaning, and prepare the data in a structure ready for metadata generation.
2. After running `data.py`, the processed data will be saved in a folder called `final_data`.

### Step 3: Set Up the Directory
Ensure that the following directory structure exists in your workspace:
   - `final_data/` — Folder containing data will be stored.
   - `Main Dataset/` — Directory where the final meta-data will be created.
   - `chb_csv/` — A temporary folder used during the metadata generation process.

### Step 4: Run the Jupyter Notebook
1. Open and run the **code.ipynb** Jupyter Notebook.
   - The notebook will process the preprocessed data and generate the meta-data (including time stamps for ictal, pre-ictal, post-ictal, peri-ictal, and non-seizure events) from the original CHB-MIT dataset.
   - The final **meta-data** will be saved in the `Main Dataset/` directory.

### Final Output:
- After running the notebook, the meta-data files will be available in the **Main Dataset** folder in **CSV** format. The class labels will be included in the last row of each CSV file.

---

## File Structure

The repository contains the following key files and directories:

- **`data.py`**: Python script for preprocessing the raw EEG data.
- **`code.ipynb`**: Jupyter notebook for generating the meta-data.
- **`CHB-MIT DB timestamp.csv`**: CSV file containing the time stamps for ictal, pre-ictal, post-ictal, peri-ictal, and non-seizure segments.
- 
---

## References

- Handa, P., & Goel, N. (2021). Peri‐ictal and non‐seizure EEG event detection using generated metadata. *Expert Systems*, e12929.

---

Feel free to contribute, raise issues, or suggest improvements via GitHub!
