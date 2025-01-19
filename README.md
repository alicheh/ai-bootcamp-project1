# AI Bootcamp Project 1

## Project Overview
This repository hosts our project1 in Quera AI Bootcamp. It uses Python and Jupyter notebooks for data processing, model training, and performance evaluation.


## Repository Structure
```
.
├── data/
│   ├── raw_band_data/ (.parquets, locally processed.)
│   ├── HBN.csv (data of tests, ...)
│   ├── data_dictionary.csv
│   └── all_data_steps_light.csv (result of processing raw_band_data)
├── notebooks/
│   ├── ds_q17.ipynb (Descriptive Statistics Questions)
│   ├── hypo_test13.ipynb (Hypothesis Tests)
│   ├── ml_classification_ssi.ipynb (Machine Learning part)
│   └── eda_hbn.ipynb (Exploratory Data Analysis of HBN.csv)
├── scripts/
│   └── process_parquets.py
├── .gitignore
└── README.md
```
- **data/**: Contains small CSV files (and resulting processed files).
- **notebooks/**: Jupyter notebooks for exploratory data analysis, cleaning, and modeling.
- **scripts/**: Python scripts with reusable functions and data processing routines.
- **.gitignore**: Ensures large files (e.g., parquet files) and virtual environment folders are not committed.

## Getting Started

### 1. Cloning the Repository
```bash
git clone https://github.com/alicheh/ai-bootcamp-project1.git
cd your-repo-name
```

### 2. Creating a Virtual Environment
**Option A: Using `pip` + `venv`**
```bash
# Create a virtual environment
python -m venv venv

# Activate it (Linux/Mac)
source venv/bin/activate

# Activate it (Windows)
.\venv\Scripts\activate
```

**Option B: Using `conda`**
```bash
# Create a conda environment
conda create -n myenv python=3.9

# Activate environment
conda activate myenv
```

### 3. Installing Dependencies
Once your environment is active, install required packages:
```bash
pip install -r requirements.txt
```
(or `conda install --file requirements.txt` if using conda)

> **Note**: Keep your `requirements.txt` up-to-date whenever you add or remove packages.

## Usage

### Running Jupyter Notebooks
1. Activate your virtual/conda environment.
2. Launch Jupyter Lab or Notebook:
   ```bash
   jupyter lab
   # or
   jupyter notebook
   ```
3. Navigate to the `notebooks/` directory and open any `.ipynb` file to run the cells.

### Running Python Scripts
- **Example**: To clean data
  ```bash
  python scripts/data_cleaning.py
  ```
- **Example**: To train a model
  ```bash
  python scripts/model_training.py
  ```
> **Tip**: Make sure file paths in scripts/notebooks use **relative paths** (`../data/...`) so they work on all team members' machines.

## Contributing Guidelines

### Branching & Pull Requests
1. **Create a new branch** for each feature or fix:
   ```bash
   git checkout -b feature/new-model
   ```
2. **Commit and push** your changes:
   ```bash
   git add .
   git commit -m "Add new model script"
   git push origin feature/new-model
   ```
3. **Open a Pull Request (PR)** on GitHub:
   - Describe your changes and their rationale.
   - Request review from a teammate.
   - Resolve any feedback before merging.

### Committing Changes
- **Use clear commit messages**: `git commit -m "Fix data cleaning function to handle missing values"`.
- **Add meaningful comments** in code and notebooks to explain your work.

### Things to Keep in Mind
- **Do not commit large files** (e.g., original parquet ~6GB). Make sure they’re in `.gitignore`.
- **Update your local branch** frequently by pulling the latest main or master branch:
  ```bash
  git checkout main
  git pull origin main
  ```
- **Synchronize environments** by updating `requirements.txt` whenever new libraries are added.


