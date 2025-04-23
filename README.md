# Student Score Prediction End-to-End ML Pipeline

## Overview
This project is an end-to-end machine learning pipeline for predicting student math scores based on demographic and academic features. It includes data ingestion, preprocessing, model training, and a Flask-based web application for real-time predictions. The project is designed for modularity, reproducibility, and ease of deployment. **Note:** This project does not use MLFlow.

## Features
- **Data Ingestion:** Loads and splits raw data into training and test sets.
- **Data Transformation:** Handles preprocessing (imputation, scaling, encoding) and saves the preprocessor.
- **Model Training:** Trains a Decision Tree regressor (with extensibility for other models) and evaluates model performance.
- **Prediction Pipeline:** Loads trained model and preprocessor for batch or single predictions.
- **Web Application:** Flask app with HTML templates for user-friendly predictions.
- **Logging & Exception Handling:** Modular logging and custom exception classes for robust debugging.

## Project Structure
```
Student Score Prediction End-to-End ML Pipeline/
│	app.py                  # Flask web application entry point
│	setup.py                # Project packaging
│	requirements.txt        # Python dependencies
│	README.md               # Project documentation
│	src/
│		components/         # Data ingestion, transformation, and training modules
│		pipeline/           # Prediction pipeline and data classes
│		logger.py           # Logging setup
│		exceptions.py       # Custom exception classes
│		util.py             # Utility functions
│	templates/              # HTML templates for the web app
│	notebook/               # Jupyter notebooks and data
│	artifacts/              # Saved models, preprocessors, and datasets
```

## Installation
1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd "Student Score Prediction End-to-End ML Pipeline"
   ```
2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # source venv/bin/activate  # On Linux/Mac
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage
### 1. Train the Model
- Run the data ingestion, transformation, and training scripts (can be triggered via main blocks in respective modules).
- Artifacts (model, preprocessor, datasets) are saved in the `artifacts/` directory.

### 2. Run the Web Application
```bash
python app.py
```
- Open your browser and go to `http://localhost:5000`.
- Enter student details to predict the math score.

## Technologies Used
- Python 3.7+
- Flask
- Pandas, NumPy, scikit-learn
- HTML/CSS (Jinja2 templates)

**Note:** MLFlow is not used in this project.

## Customization
- To add new models, extend the `ModelTrainer` class in `src/components/data_trainer.py`.
- Adjust preprocessing in `DataTransformation` as needed.

## Contributing
1. Fork the repository
2. Create a new branch (`git checkout -b feature-xyz`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature-xyz`)
5. Open a Pull Request

## Author
Pranav Suryawanshi
